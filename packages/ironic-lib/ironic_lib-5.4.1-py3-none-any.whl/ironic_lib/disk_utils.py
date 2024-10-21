# Copyright 2014 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import os
import re
import stat
import time
import warnings

from oslo_concurrency import processutils
from oslo_config import cfg
from oslo_utils import excutils
from oslo_utils import imageutils
from oslo_utils import units
import tenacity

from ironic_lib.common.i18n import _
from ironic_lib import disk_partitioner
from ironic_lib import exception
from ironic_lib import utils


opts = [
    cfg.IntOpt('efi_system_partition_size',
               default=200,
               help='Size of EFI system partition in MiB when configuring '
                    'UEFI systems for local boot.'),
    cfg.IntOpt('bios_boot_partition_size',
               default=1,
               help='Size of BIOS Boot partition in MiB when configuring '
                    'GPT partitioned systems for local boot in BIOS.'),
    cfg.StrOpt('dd_block_size',
               default='1M',
               help='Block size to use when writing to the nodes disk.'),
    cfg.IntOpt('partition_detection_attempts',
               default=3,
               min=1,
               help='Maximum attempts to detect a newly created partition.'),
    cfg.IntOpt('partprobe_attempts',
               default=10,
               help='Maximum number of attempts to try to read the '
                    'partition.'),
    cfg.IntOpt('image_convert_memory_limit',
               default=2048,
               help='Memory limit for "qemu-img convert" in MiB. Implemented '
                    'via the address space resource limit.'),
    cfg.IntOpt('image_convert_attempts',
               default=3,
               help='Number of attempts to convert an image.'),
]

CONF = cfg.CONF
CONF.register_opts(opts, group='disk_utils')

LOG = logging.getLogger(__name__)

_PARTED_PRINT_RE = re.compile(r"^(\d+):([\d\.]+)MiB:"
                              r"([\d\.]+)MiB:([\d\.]+)MiB:(\w*):(.*):(.*);")
_PARTED_TABLE_TYPE_RE = re.compile(r'^.*partition\s+table\s*:\s*(gpt|msdos)',
                                   re.IGNORECASE | re.MULTILINE)

CONFIGDRIVE_LABEL = "config-2"
MAX_CONFIG_DRIVE_SIZE_MB = 64

GPT_SIZE_SECTORS = 33

# Maximum disk size supported by MBR is 2TB (2 * 1024 * 1024 MB)
MAX_DISK_SIZE_MB_SUPPORTED_BY_MBR = 2097152

# Limit the memory address space to 1 GiB when running qemu-img
QEMU_IMG_LIMITS = None


def _qemu_img_limits():
    global QEMU_IMG_LIMITS
    if QEMU_IMG_LIMITS is None:
        QEMU_IMG_LIMITS = processutils.ProcessLimits(
            address_space=CONF.disk_utils.image_convert_memory_limit
            * units.Mi)
    return QEMU_IMG_LIMITS


def list_partitions(device):
    """Get partitions information from given device.

    :param device: The device path.
    :returns: list of dictionaries (one per partition) with keys:
              number, start, end, size (in MiB), filesystem, partition_name,
              flags, path.
    """
    output = utils.execute(
        'parted', '-s', '-m', device, 'unit', 'MiB', 'print',
        use_standard_locale=True, run_as_root=True)[0]
    if isinstance(output, bytes):
        output = output.decode("utf-8")
    lines = [line for line in output.split('\n') if line.strip()][2:]
    # Example of line: 1:1.00MiB:501MiB:500MiB:ext4::boot
    fields = ('number', 'start', 'end', 'size', 'filesystem', 'partition_name',
              'flags')
    result = []
    for line in lines:
        match = _PARTED_PRINT_RE.match(line)
        if match is None:
            LOG.warning("Partition information from parted for device "
                        "%(device)s does not match "
                        "expected format: %(line)s",
                        dict(device=device, line=line))
            continue
        # Cast int fields to ints (some are floats and we round them down)
        groups = [int(float(x)) if i < 4 else x
                  for i, x in enumerate(match.groups())]
        item = dict(zip(fields, groups))
        item['path'] = partition_index_to_path(device, item['number'])
        result.append(item)
    return result


def count_mbr_partitions(device):
    """Count the number of primary and logical partitions on a MBR

    :param device: The device path.
    :returns: A tuple with the number of primary partitions and logical
              partitions.
    :raise: ValueError if the device does not have a valid MBR partition
            table.
    """
    # -d do not update the kernel table
    # -s print a summary of the partition table
    output, err = utils.execute('partprobe', '-d', '-s', device,
                                run_as_root=True, use_standard_locale=True)
    if 'msdos' not in output:
        raise ValueError('The device %s does not have a valid MBR '
                         'partition table' % device)
    # Sample output: /dev/vdb: msdos partitions 1 2 3 <5 6 7>
    # The partitions with number > 4 (and inside <>) are logical partitions
    output = output.replace('<', '').replace('>', '')
    partitions = [int(s) for s in output.split() if s.isdigit()]

    return(sum(i < 5 for i in partitions), sum(i > 4 for i in partitions))


def get_disk_identifier(dev):
    """Get the disk identifier from the disk being exposed by the ramdisk.

    This disk identifier is appended to the pxe config which will then be
    used by chain.c32 to detect the correct disk to chainload. This is helpful
    in deployments to nodes with multiple disks.

    http://www.syslinux.org/wiki/index.php/Comboot/chain.c32#mbr:

    :param dev: Path for the already populated disk device.
    :raises OSError: When the hexdump binary is unavailable.
    :returns: The Disk Identifier.
    """
    disk_identifier = utils.execute('hexdump', '-s', '440', '-n', '4',
                                    '-e', '''\"0x%08x\"''',
                                    dev, run_as_root=True,
                                    attempts=5, delay_on_retry=True)
    return disk_identifier[0]


def get_partition_table_type(device):
    """Get partition table type, msdos or gpt.

    :param device: the name of the device
    :return: dos, gpt or None
    """
    out = utils.execute('parted', '--script', device, '--', 'print',
                        run_as_root=True, use_standard_locale=True)[0]
    m = _PARTED_TABLE_TYPE_RE.search(out)
    if m:
        return m.group(1)

    LOG.warning("Unable to get partition table type for device %s", device)
    return 'unknown'


def _blkid(device, probe=False, fields=None):
    args = []
    if probe:
        args.append('-p')
    if fields:
        args += sum((['-s', field] for field in fields), [])

    output, err = utils.execute('blkid', device, *args,
                                use_standard_locale=True, run_as_root=True)
    if output.strip():
        return output.split(': ', 1)[1]
    else:
        return ""


def _lsblk(device, deps=True, fields=None):
    args = ['--pairs', '--bytes', '--ascii']
    if not deps:
        args.append('--nodeps')
    if fields:
        args.extend(['--output', ','.join(fields)])
    else:
        args.append('--output-all')

    output, err = utils.execute('lsblk', device, *args,
                                use_standard_locale=True, run_as_root=True)
    return output.strip()


def get_device_information(device, probe=False, fields=None):
    """Get information about a device using blkid.

    Can be applied to all block devices: disks, RAID, partitions.

    :param device: Device name.
    :param probe: DEPRECATED, do not use.
    :param fields: A list of fields to request (all by default).
    :return: A dictionary with requested fields as keys.
    :raises: ProcessExecutionError
    """
    if probe:
        output = _blkid(device, probe=True, fields=fields)
    else:
        output = _lsblk(device, fields=fields, deps=False)

    if output:
        return next(utils.parse_device_tags(output))
    else:
        return {}


def find_efi_partition(device):
    """Looks for the EFI partition on a given device.

    A boot partition on a GPT disk is assumed to be an EFI partition as well.

    :param device: the name of the device
    :return: the EFI partition record from `list_partitions` or None
    """
    is_gpt = get_partition_table_type(device) == 'gpt'
    for part in list_partitions(device):
        flags = {x.strip() for x in part['flags'].split(',')}
        if 'esp' in flags or ('boot' in flags and is_gpt):
            LOG.debug("Found EFI partition %s on device %s", part, device)
            return part
    else:
        LOG.debug("No efi partition found on device %s", device)


def get_uefi_disk_identifier(dev):
    """Get the uuid from the disk being exposed by the ramdisk.

    DEPRECATED: use find_efi_partition with get_device_information instead.

    :param dev: Path for the already populated disk device.
    :raises InstanceDeployFailure: Image is not UEFI bootable.
    :returns: The UUID of the partition.
    """
    warnings.warn("get_uefi_disk_identifier is deprecated, use "
                  "find_efi_partition and get_partition_information instead",
                  DeprecationWarning)

    partition_id = None
    try:
        report, _ = utils.execute('fdisk', '-l', dev, run_as_root=True)
    except processutils.ProcessExecutionError as e:
        msg = _('Failed to find the partition on the disk %s ') % e
        LOG.error(msg)
        raise exception.InstanceDeployFailure(msg)
    for line in report.splitlines():
        if line.startswith(dev) and 'EFI System' in line:
            vals = line.split()
            partition_id = vals[0]
    try:
        lsblk_output = _lsblk(partition_id, fields=['UUID'])
        disk_identifier = lsblk_output.split("=")[1].strip()
        disk_identifier = disk_identifier.strip('"')
    except processutils.ProcessExecutionError as e:
        raise exception.InstanceDeployFailure("Image is not UEFI bootable. "
                                              "Error: %s " % e)
    return disk_identifier


_ISCSI_PREFIX = "iqn.2008-10.org.openstack:"


# TODO(dtantsur): deprecate node_uuid here, it's not overly useful (any iSCSI
# device should get the same treatment).
def is_iscsi_device(dev, node_uuid=None):
    """Check whether the device path belongs to an iSCSI device.

    If node UUID is provided, checks that the device belongs to this UUID.
    """
    if node_uuid:
        return (_ISCSI_PREFIX + node_uuid) in dev
    else:
        return _ISCSI_PREFIX in dev


def is_last_char_digit(dev):
    """check whether device name ends with a digit"""
    if len(dev) >= 1:
        return dev[-1].isdigit()
    return False


def partition_index_to_path(device, index):
    """Guess a partition path based on its device and index.

    :param device: Device path.
    :param index: Partition index.
    """
    # the actual device names in the baremetal are like /dev/sda, /dev/sdb etc.
    # While for the iSCSI device, the naming convention has a format which has
    # iqn also embedded in it.
    # When this function is called by ironic-conductor, the iSCSI device name
    # should be appended by "part%d". While on the baremetal, it should name
    # the device partitions as /dev/sda1 and not /dev/sda-part1.
    if is_iscsi_device(device):
        part_template = '%s-part%d'
    elif is_last_char_digit(device):
        part_template = '%sp%d'
    else:
        part_template = '%s%d'
    return part_template % (device, index)


def make_partitions(dev, root_mb, swap_mb, ephemeral_mb,
                    configdrive_mb, node_uuid, commit=True,
                    boot_option="netboot", boot_mode="bios",
                    disk_label=None, cpu_arch=""):
    """Partition the disk device.

    Create partitions for root, swap, ephemeral and configdrive on a
    disk device.

    :param dev: Path for the device to work on.
    :param root_mb: Size of the root partition in mebibytes (MiB).
    :param swap_mb: Size of the swap partition in mebibytes (MiB). If 0,
        no partition will be created.
    :param ephemeral_mb: Size of the ephemeral partition in mebibytes (MiB).
        If 0, no partition will be created.
    :param configdrive_mb: Size of the configdrive partition in
        mebibytes (MiB). If 0, no partition will be created.
    :param commit: True/False. Default for this setting is True. If False
        partitions will not be written to disk.
    :param boot_option: Can be "local" or "netboot". "netboot" by default.
    :param boot_mode: Can be "bios" or "uefi". "bios" by default.
    :param node_uuid: Node's uuid. Used for logging.
    :param disk_label: The disk label to be used when creating the
        partition table. Valid values are: "msdos", "gpt" or None; If None
        Ironic will figure it out according to the boot_mode parameter.
    :param cpu_arch: Architecture of the node the disk device belongs to.
        When using the default value of None, no architecture specific
        steps will be taken. This default should be used for x86_64. When
        set to ppc64*, architecture specific steps are taken for booting a
        partition image locally.
    :returns: A dictionary containing the partition type as Key and partition
        path as Value for the partitions created by this method.

    """
    LOG.debug("Starting to partition the disk device: %(dev)s "
              "for node %(node)s",
              {'dev': dev, 'node': node_uuid})
    part_dict = {}

    if disk_label is None:
        disk_label = 'gpt' if boot_mode == 'uefi' else 'msdos'

    dp = disk_partitioner.DiskPartitioner(dev, disk_label=disk_label)

    # For uefi localboot, switch partition table to gpt and create the efi
    # system partition as the first partition.
    if boot_mode == "uefi" and boot_option == "local":
        part_num = dp.add_partition(CONF.disk_utils.efi_system_partition_size,
                                    fs_type='fat32',
                                    boot_flag='boot')
        part_dict['efi system partition'] = partition_index_to_path(
            dev, part_num)

    if (boot_mode == "bios" and boot_option == "local" and disk_label == "gpt"
        and not cpu_arch.startswith('ppc64')):
        part_num = dp.add_partition(CONF.disk_utils.bios_boot_partition_size,
                                    boot_flag='bios_grub')
        part_dict['BIOS Boot partition'] = partition_index_to_path(
            dev, part_num)

    # NOTE(mjturek): With ppc64* nodes, partition images are expected to have
    # a PrEP partition at the start of the disk. This is an 8 MiB partition
    # with the boot and prep flags set. The bootloader should be installed
    # here.
    if (cpu_arch.startswith("ppc64") and boot_mode == "bios"
            and boot_option == "local"):
        LOG.debug("Add PReP boot partition (8 MB) to device: "
                  "%(dev)s for node %(node)s",
                  {'dev': dev, 'node': node_uuid})
        boot_flag = 'boot' if disk_label == 'msdos' else None
        part_num = dp.add_partition(8, part_type='primary',
                                    boot_flag=boot_flag, extra_flags=['prep'])
        part_dict['PReP Boot partition'] = partition_index_to_path(
            dev, part_num)
    if ephemeral_mb:
        LOG.debug("Add ephemeral partition (%(size)d MB) to device: %(dev)s "
                  "for node %(node)s",
                  {'dev': dev, 'size': ephemeral_mb, 'node': node_uuid})
        part_num = dp.add_partition(ephemeral_mb)
        part_dict['ephemeral'] = partition_index_to_path(dev, part_num)
    if swap_mb:
        LOG.debug("Add Swap partition (%(size)d MB) to device: %(dev)s "
                  "for node %(node)s",
                  {'dev': dev, 'size': swap_mb, 'node': node_uuid})
        part_num = dp.add_partition(swap_mb, fs_type='linux-swap')
        part_dict['swap'] = partition_index_to_path(dev, part_num)
    if configdrive_mb:
        LOG.debug("Add config drive partition (%(size)d MB) to device: "
                  "%(dev)s for node %(node)s",
                  {'dev': dev, 'size': configdrive_mb, 'node': node_uuid})
        part_num = dp.add_partition(configdrive_mb)
        part_dict['configdrive'] = partition_index_to_path(dev, part_num)

    # NOTE(lucasagomes): Make the root partition the last partition. This
    # enables tools like cloud-init's growroot utility to expand the root
    # partition until the end of the disk.
    LOG.debug("Add root partition (%(size)d MB) to device: %(dev)s "
              "for node %(node)s",
              {'dev': dev, 'size': root_mb, 'node': node_uuid})

    boot_val = 'boot' if (not cpu_arch.startswith("ppc64")
                          and boot_mode == "bios"
                          and boot_option == "local"
                          and disk_label == "msdos") else None

    part_num = dp.add_partition(root_mb, boot_flag=boot_val)

    part_dict['root'] = partition_index_to_path(dev, part_num)

    if commit:
        # write to the disk
        dp.commit()
        trigger_device_rescan(dev)
    return part_dict


def is_block_device(dev):
    """Check whether a device is block or not."""
    attempts = CONF.disk_utils.partition_detection_attempts
    for attempt in range(attempts):
        try:
            s = os.stat(dev)
        except OSError as e:
            LOG.debug("Unable to stat device %(dev)s. Attempt %(attempt)d "
                      "out of %(total)d. Error: %(err)s",
                      {"dev": dev, "attempt": attempt + 1,
                       "total": attempts, "err": e})
            time.sleep(1)
        else:
            return stat.S_ISBLK(s.st_mode)
    msg = _("Unable to stat device %(dev)s after attempting to verify "
            "%(attempts)d times.") % {'dev': dev, 'attempts': attempts}
    LOG.error(msg)
    raise exception.InstanceDeployFailure(msg)


def dd(src, dst, conv_flags=None):
    """Execute dd from src to dst."""
    if conv_flags:
        extra_args = ['conv=%s' % conv_flags]
    else:
        extra_args = []

    utils.dd(src, dst, 'bs=%s' % CONF.disk_utils.dd_block_size, 'oflag=direct',
             *extra_args)


def qemu_img_info(path):
    """Return an object containing the parsed output from qemu-img info."""
    if not os.path.exists(path):
        return imageutils.QemuImgInfo()

    out, err = utils.execute('env', 'LC_ALL=C', 'LANG=C',
                             'qemu-img', 'info', path,
                             '--output=json',
                             prlimit=_qemu_img_limits())
    return imageutils.QemuImgInfo(out, format='json')


def _retry_on_res_temp_unavailable(exc):
    if (isinstance(exc, processutils.ProcessExecutionError)
            and ('Resource temporarily unavailable' in exc.stderr
                 or 'Cannot allocate memory' in exc.stderr)):
        return True
    return False


@tenacity.retry(
    retry=tenacity.retry_if_exception(_retry_on_res_temp_unavailable),
    stop=tenacity.stop_after_attempt(CONF.disk_utils.image_convert_attempts),
    reraise=True)
def convert_image(source, dest, out_format, run_as_root=False, cache=None,
                  out_of_order=False, sparse_size=None):
    """Convert image to other format."""
    cmd = ['qemu-img', 'convert', '-O', out_format]
    if cache is not None:
        cmd += ['-t', cache]
    if sparse_size is not None:
        cmd += ['-S', sparse_size]
    if out_of_order:
        cmd.append('-W')
    cmd += [source, dest]
    # NOTE(TheJulia): Staticly set the MALLOC_ARENA_MAX to prevent leaking
    # and the creation of new malloc arenas which will consume the system
    # memory. If limited to 1, qemu-img consumes ~250 MB of RAM, but when
    # another thread tries to access a locked section of memory in use with
    # another thread, then by default a new malloc arena is created,
    # which essentially balloons the memory requirement of the machine.
    # Default for qemu-img is 8 * nCPU * ~250MB (based on defaults +
    # thread/code/process/library overhead. In other words, 64 GB. Limiting
    # this to 3 keeps the memory utilization in happy cases below the overall
    # threshold which is in place in case a malicious image is attempted to
    # be passed through qemu-img.
    env_vars = {'MALLOC_ARENA_MAX': '3'}
    try:
        utils.execute(*cmd, run_as_root=run_as_root,
                      prlimit=_qemu_img_limits(),
                      use_standard_locale=True,
                      env_variables=env_vars)
    except processutils.ProcessExecutionError as e:
        if ('Resource temporarily unavailable' in e.stderr
            or 'Cannot allocate memory' in e.stderr):
            LOG.debug('Failed to convert image, retrying. Error: %s', e)
            # Sync disk caches before the next attempt
            utils.execute('sync')
        raise


def populate_image(src, dst, conv_flags=None):
    data = qemu_img_info(src)
    if data.file_format == 'raw':
        dd(src, dst, conv_flags=conv_flags)
    else:
        convert_image(src, dst, 'raw', True, sparse_size='0')


def block_uuid(dev):
    """Get UUID of a block device.

    Try to fetch the UUID, if that fails, try to fetch the PARTUUID.
    """
    info = get_device_information(dev, fields=['UUID', 'PARTUUID'])
    if info.get('UUID'):
        return info['UUID']
    else:
        LOG.debug('Falling back to partition UUID as the block device UUID '
                  'was not found while examining %(device)s',
                  {'device': dev})
        return info.get('PARTUUID', '')


def get_image_mb(image_path, virtual_size=True):
    """Get size of an image in Megabyte."""
    mb = 1024 * 1024
    if not virtual_size:
        image_byte = os.path.getsize(image_path)
    else:
        data = qemu_img_info(image_path)
        image_byte = data.virtual_size

    # round up size to MB
    image_mb = int((image_byte + mb - 1) / mb)
    return image_mb


def get_dev_block_size(dev):
    """Get the device size in 512 byte sectors."""
    block_sz, cmderr = utils.execute('blockdev', '--getsz', dev,
                                     run_as_root=True)
    return int(block_sz)


def destroy_disk_metadata(dev, node_uuid):
    """Destroy metadata structures on node's disk.

    Ensure that node's disk magic strings are wiped without zeroing the
    entire drive. To do this we use the wipefs tool from util-linux.

    :param dev: Path for the device to work on.
    :param node_uuid: Node's uuid. Used for logging.
    """
    # NOTE(NobodyCam): This is needed to work around bug:
    # https://bugs.launchpad.net/ironic/+bug/1317647
    LOG.debug("Start destroy disk metadata for node %(node)s.",
              {'node': node_uuid})
    try:
        utils.execute('wipefs', '--force', '--all', dev,
                      run_as_root=True,
                      use_standard_locale=True)
    except processutils.ProcessExecutionError as e:
        with excutils.save_and_reraise_exception() as ctxt:
            # NOTE(zhenguo): Check if --force option is supported for wipefs,
            # if not, we should try without it.
            if '--force' in str(e):
                ctxt.reraise = False
                utils.execute('wipefs', '--all', dev,
                              run_as_root=True,
                              use_standard_locale=True)
    # NOTE(TheJulia): sgdisk attempts to load and make sense of the
    # partition tables in advance of wiping the partition data.
    # This means when a CRC error is found, sgdisk fails before
    # erasing partition data.
    # This is the same bug as
    # https://bugs.launchpad.net/ironic-python-agent/+bug/1737556

    # Overwrite the Primary GPT, catch very small partitions (like EBRs)
    dd_device = 'of=%s' % dev
    dd_count = 'count=%s' % GPT_SIZE_SECTORS
    dev_size = get_dev_block_size(dev)
    if dev_size < GPT_SIZE_SECTORS:
        dd_count = 'count=%s' % dev_size
    utils.execute('dd', 'bs=512', 'if=/dev/zero', dd_device, dd_count,
                  run_as_root=True, use_standard_locale=True)

    # Overwrite the Secondary GPT, do this only if there could be one
    if dev_size > GPT_SIZE_SECTORS:
        gpt_backup = dev_size - GPT_SIZE_SECTORS
        dd_seek = 'seek=%i' % gpt_backup
        dd_count = 'count=%s' % GPT_SIZE_SECTORS
        utils.execute('dd', 'bs=512', 'if=/dev/zero', dd_device, dd_count,
                      dd_seek, run_as_root=True, use_standard_locale=True)

    # Go ahead and let sgdisk run as well.
    utils.execute('sgdisk', '-Z', dev, run_as_root=True,
                  use_standard_locale=True)

    try:
        utils.wait_for_disk_to_become_available(dev)
    except exception.IronicException as e:
        raise exception.InstanceDeployFailure(
            _('Destroying metadata failed on device %(device)s. '
              'Error: %(error)s')
            % {'device': dev, 'error': e})

    LOG.info("Disk metadata on %(dev)s successfully destroyed for node "
             "%(node)s", {'dev': dev, 'node': node_uuid})


def list_opts():
    """Entry point for oslo-config-generator."""
    return [('disk_utils', opts)]


def _fix_gpt_structs(device, node_uuid):
    """Checks backup GPT data structures and moves them to end of the device

    :param device: The device path.
    :param node_uuid: UUID of the Node. Used for logging.
    :raises: InstanceDeployFailure, if any disk partitioning related
        commands fail.
    """
    try:
        output, _err = utils.execute('sgdisk', '-v', device, run_as_root=True)

        search_str = "it doesn't reside\nat the end of the disk"
        if search_str in output:
            utils.execute('sgdisk', '-e', device, run_as_root=True)
    except (processutils.UnknownArgumentError,
            processutils.ProcessExecutionError, OSError) as e:
        msg = (_('Failed to fix GPT data structures on disk %(disk)s '
                 'for node %(node)s. Error: %(error)s') %
               {'disk': device, 'node': node_uuid, 'error': e})
        LOG.error(msg)
        raise exception.InstanceDeployFailure(msg)


def fix_gpt_partition(device, node_uuid):
    """Fix GPT partition

    Fix GPT table information when image is written to a disk which
    has a bigger extend (e.g. 30GB image written on a 60Gb physical disk).

    :param device: The device path.
    :param node_uuid: UUID of the Node.
    :raises: InstanceDeployFailure if exception is caught.
    """
    try:
        disk_is_gpt_partitioned = (get_partition_table_type(device) == 'gpt')
        if disk_is_gpt_partitioned:
            _fix_gpt_structs(device, node_uuid)
    except Exception as e:
        msg = (_('Failed to fix GPT partition on disk %(disk)s '
                 'for node %(node)s. Error: %(error)s') %
               {'disk': device, 'node': node_uuid, 'error': e})
        LOG.error(msg)
        raise exception.InstanceDeployFailure(msg)


def udev_settle():
    """Wait for the udev event queue to settle.

    Wait for the udev event queue to settle to make sure all devices
    are detected once the machine boots up.

    :return: True on success, False otherwise.
    """
    LOG.debug('Waiting until udev event queue is empty')
    try:
        utils.execute('udevadm', 'settle')
    except processutils.ProcessExecutionError as e:
        LOG.warning('Something went wrong when waiting for udev '
                    'to settle. Error: %s', e)
        return False
    else:
        return True


def partprobe(device, attempts=None):
    """Probe partitions on the given device.

    :param device: The block device containing paritions that is attempting
                   to be updated.
    :param attempts: Number of attempts to run partprobe, the default is read
                     from the configuration.
    :return: True on success, False otherwise.
    """
    if attempts is None:
        attempts = CONF.disk_utils.partprobe_attempts

    try:
        utils.execute('partprobe', device, run_as_root=True, attempts=attempts)
    except (processutils.UnknownArgumentError,
            processutils.ProcessExecutionError, OSError) as e:
        LOG.warning("Unable to probe for partitions on device %(device)s, "
                    "the partitioning table may be broken. Error: %(error)s",
                    {'device': device, 'error': e})
        return False
    else:
        return True


def trigger_device_rescan(device, attempts=None):
    """Sync and trigger device rescan.

    Disk partition performed via parted, when performed on a ramdisk
    do not have to honor the fsync mechanism. In essence, fsync is used
    on the file representing the block device, which falls to the kernel
    filesystem layer to trigger a sync event. On a ramdisk using ramfs,
    this is an explicit non-operation.

    As a result of this, we need to trigger a system wide sync operation
    which will trigger cache to flush to disk, after which partition changes
    should be visible upon re-scan.

    When ramdisks are not in use, this also helps ensure that data has
    been safely flushed across the wire, such as on iscsi connections.

    :param device: The block device containing paritions that is attempting
                   to be updated.
    :param attempts: Number of attempts to run partprobe, the default is read
                     from the configuration.
    :return: True on success, False otherwise.
    """
    LOG.debug('Explicitly calling sync to force buffer/cache flush')
    utils.execute('sync')
    # Make sure any additions to the partitioning are reflected in the
    # kernel.
    udev_settle()
    partprobe(device, attempts=attempts)
    try:
        # Also verify that the partitioning is correct now.
        utils.execute('sgdisk', '-v', device, run_as_root=True)
    except processutils.ProcessExecutionError as exc:
        LOG.warning('Failed to verify partition tables on device %(dev)s: '
                    '%(err)s', {'dev': device, 'err': exc})
        return False
    else:
        return True
