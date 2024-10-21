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

import os
import stat
from unittest import mock

from oslo_concurrency import processutils
from oslo_config import cfg
from oslo_utils import imageutils

from ironic_lib import disk_utils
from ironic_lib import exception
from ironic_lib.tests import base
from ironic_lib import utils

CONF = cfg.CONF


@mock.patch.object(utils, 'execute', autospec=True)
class ListPartitionsTestCase(base.IronicLibTestCase):

    def test_correct(self, execute_mock):
        output = """
BYT;
/dev/sda:500107862016B:scsi:512:4096:msdos:ATA HGST HTS725050A7:;
1:1.00MiB:501MiB:500MiB:ext4::boot;
2:501MiB:476940MiB:476439MiB:::;
"""
        expected = [
            {'number': 1, 'start': 1, 'end': 501, 'size': 500,
             'filesystem': 'ext4', 'partition_name': '', 'flags': 'boot',
             'path': '/dev/fake1'},
            {'number': 2, 'start': 501, 'end': 476940, 'size': 476439,
             'filesystem': '', 'partition_name': '', 'flags': '',
             'path': '/dev/fake2'},
        ]
        execute_mock.return_value = (output, '')
        result = disk_utils.list_partitions('/dev/fake')
        self.assertEqual(expected, result)
        execute_mock.assert_called_once_with(
            'parted', '-s', '-m', '/dev/fake', 'unit', 'MiB', 'print',
            use_standard_locale=True, run_as_root=True)

    @mock.patch.object(disk_utils.LOG, 'warning', autospec=True)
    def test_incorrect(self, log_mock, execute_mock):
        output = """
BYT;
/dev/sda:500107862016B:scsi:512:4096:msdos:ATA HGST HTS725050A7:;
1:XX1076MiB:---:524MiB:ext4::boot;
"""
        execute_mock.return_value = (output, '')
        self.assertEqual([], disk_utils.list_partitions('/dev/fake'))
        self.assertEqual(1, log_mock.call_count)

    def test_correct_gpt_nvme(self, execute_mock):
        output = """
BYT;
/dev/vda:40960MiB:virtblk:512:512:gpt:Virtio Block Device:;
2:1.00MiB:2.00MiB:1.00MiB::Bios partition:bios_grub;
1:4.00MiB:5407MiB:5403MiB:ext4:Root partition:;
3:5407MiB:5507MiB:100MiB:fat16:Boot partition:boot, esp;
"""
        expected = [
            {'end': 2, 'number': 2, 'start': 1, 'flags': 'bios_grub',
             'filesystem': '', 'partition_name': 'Bios partition', 'size': 1,
             'path': '/dev/fake0p2'},
            {'end': 5407, 'number': 1, 'start': 4, 'flags': '',
             'filesystem': 'ext4', 'partition_name': 'Root partition',
             'size': 5403, 'path': '/dev/fake0p1'},
            {'end': 5507, 'number': 3, 'start': 5407,
             'flags': 'boot, esp', 'filesystem': 'fat16',
             'partition_name': 'Boot partition', 'size': 100,
             'path': '/dev/fake0p3'},
        ]
        execute_mock.return_value = (output, '')
        result = disk_utils.list_partitions('/dev/fake0')
        self.assertEqual(expected, result)
        execute_mock.assert_called_once_with(
            'parted', '-s', '-m', '/dev/fake0', 'unit', 'MiB', 'print',
            use_standard_locale=True, run_as_root=True)

    @mock.patch.object(disk_utils.LOG, 'warning', autospec=True)
    def test_incorrect_gpt(self, log_mock, execute_mock):
        output = """
BYT;
/dev/vda:40960MiB:virtblk:512:512:gpt:Virtio Block Device:;
2:XX1.00MiB:---:1.00MiB::primary:bios_grub;
"""
        execute_mock.return_value = (output, '')
        self.assertEqual([], disk_utils.list_partitions('/dev/fake'))
        self.assertEqual(1, log_mock.call_count)


class GetUEFIDiskIdentifierTestCase(base.IronicLibTestCase):

    def setUp(self):
        super(GetUEFIDiskIdentifierTestCase, self).setUp()
        self.dev = '/dev/fake'

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_get_uefi_disk_identifier_uefi_bootable_image(self, mock_execute):
        mock_execute.return_value = ('', '')
        fdisk_output = """
Disk /dev/sda: 931.5 GiB, 1000171331584 bytes, 1953459632 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 262144 bytes / 262144 bytes
Disklabel type: gpt
Disk identifier: 73457A6C-3595-4965-8D83-2EA1BD85F327

Device          Start        End    Sectors   Size Type
/dev/fake-part1        2048    1050623    1048576   512M EFI System
/dev/fake-part2     1050624 1920172031 1919121408 915.1G Linux filesystem
/dev/fake-part3  1920172032 1953458175   33286144  15.9G Linux swap
"""
        partition_id = '/dev/fake-part1'
        lsblk_output = 'UUID="ABCD-B05B"\n'
        part_result = 'ABCD-B05B'
        mock_execute.side_effect = [(fdisk_output, ''), (lsblk_output, '')]
        result = disk_utils.get_uefi_disk_identifier(self.dev)
        self.assertEqual(part_result, result)
        execute_calls = [
            mock.call('fdisk', '-l', self.dev, run_as_root=True),
            mock.call('lsblk', partition_id, '--pairs', '--bytes', '--ascii',
                      '--output', 'UUID', use_standard_locale=True,
                      run_as_root=True)
        ]
        mock_execute.assert_has_calls(execute_calls)

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_get_uefi_disk_identifier_non_uefi_bootable_image(self,
                                                              mock_execute):
        mock_execute.return_value = ('', '')
        fdisk_output = """
Disk /dev/vda: 50 GiB, 53687091200 bytes, 104857600 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xb82b9faf

Device     Boot Start       End   Sectors Size Id Type
/dev/fake-part1  *     2048 104857566 104855519  50G 83 Linux
"""
        partition_id = None
        mock_execute.side_effect = [(fdisk_output, ''),
                                    processutils.ProcessExecutionError()]
        self.assertRaises(exception.InstanceDeployFailure,
                          disk_utils.get_uefi_disk_identifier, self.dev)
        execute_calls = [
            mock.call('fdisk', '-l', self.dev, run_as_root=True),
            mock.call('lsblk', partition_id, '--pairs', '--bytes', '--ascii',
                      '--output', 'UUID', use_standard_locale=True,
                      run_as_root=True)
        ]
        mock_execute.assert_has_calls(execute_calls)


@mock.patch.object(utils, 'execute', autospec=True)
class MakePartitionsTestCase(base.IronicLibTestCase):

    def setUp(self):
        super(MakePartitionsTestCase, self).setUp()
        self.dev = 'fake-dev'
        self.root_mb = 1024
        self.swap_mb = 512
        self.ephemeral_mb = 0
        self.configdrive_mb = 0
        self.node_uuid = "12345678-1234-1234-1234-1234567890abcxyz"
        self.efi_size = CONF.disk_utils.efi_system_partition_size
        self.bios_size = CONF.disk_utils.bios_boot_partition_size

    def _get_parted_cmd(self, dev, label=None):
        if label is None:
            label = 'msdos'

        return ['parted', '-a', 'optimal', '-s', dev,
                '--', 'unit', 'MiB', 'mklabel', label]

    def _add_efi_sz(self, x):
        return str(x + self.efi_size)

    def _add_bios_sz(self, x):
        return str(x + self.bios_size)

    def _test_make_partitions(self, mock_exc, boot_option, boot_mode='bios',
                              disk_label=None, cpu_arch=""):
        mock_exc.return_value = ('', '')
        disk_utils.make_partitions(self.dev, self.root_mb, self.swap_mb,
                                   self.ephemeral_mb, self.configdrive_mb,
                                   self.node_uuid, boot_option=boot_option,
                                   boot_mode=boot_mode, disk_label=disk_label,
                                   cpu_arch=cpu_arch)

        if boot_option == "local" and boot_mode == "uefi":
            expected_mkpart = ['mkpart', 'primary', 'fat32', '1',
                               self._add_efi_sz(1),
                               'set', '1', 'boot', 'on',
                               'mkpart', 'primary', 'linux-swap',
                               self._add_efi_sz(1), self._add_efi_sz(513),
                               'mkpart', 'primary', '', self._add_efi_sz(513),
                               self._add_efi_sz(1537)]
        else:
            if boot_option == "local":
                if disk_label == "gpt":
                    if cpu_arch.startswith('ppc64'):
                        expected_mkpart = ['mkpart', 'primary', '', '1', '9',
                                           'set', '1', 'prep', 'on',
                                           'mkpart', 'primary', 'linux-swap',
                                           '9', '521', 'mkpart', 'primary',
                                           '', '521', '1545']
                    else:
                        expected_mkpart = ['mkpart', 'primary', '', '1',
                                           self._add_bios_sz(1),
                                           'set', '1', 'bios_grub', 'on',
                                           'mkpart', 'primary', 'linux-swap',
                                           self._add_bios_sz(1),
                                           self._add_bios_sz(513),
                                           'mkpart', 'primary', '',
                                           self._add_bios_sz(513),
                                           self._add_bios_sz(1537)]
                elif cpu_arch.startswith('ppc64'):
                    expected_mkpart = ['mkpart', 'primary', '', '1', '9',
                                       'set', '1', 'boot', 'on',
                                       'set', '1', 'prep', 'on',
                                       'mkpart', 'primary', 'linux-swap',
                                       '9', '521', 'mkpart', 'primary',
                                       '', '521', '1545']
                else:
                    expected_mkpart = ['mkpart', 'primary', 'linux-swap', '1',
                                       '513', 'mkpart', 'primary', '', '513',
                                       '1537', 'set', '2', 'boot', 'on']
            else:
                expected_mkpart = ['mkpart', 'primary', 'linux-swap', '1',
                                   '513', 'mkpart', 'primary', '', '513',
                                   '1537']
        self.dev = 'fake-dev'
        parted_cmd = (self._get_parted_cmd(self.dev, disk_label)
                      + expected_mkpart)
        parted_call = mock.call(*parted_cmd, use_standard_locale=True,
                                run_as_root=True)
        fuser_cmd = ['fuser', 'fake-dev']
        fuser_call = mock.call(*fuser_cmd, run_as_root=True,
                               check_exit_code=[0, 1])

        sync_calls = [mock.call('sync'),
                      mock.call('udevadm', 'settle'),
                      mock.call('partprobe', self.dev, attempts=10,
                                run_as_root=True),
                      mock.call('sgdisk', '-v', self.dev, run_as_root=True)]

        mock_exc.assert_has_calls([parted_call, fuser_call] + sync_calls)

    def test_make_partitions(self, mock_exc):
        self._test_make_partitions(mock_exc, boot_option="netboot")

    def test_make_partitions_local_boot(self, mock_exc):
        self._test_make_partitions(mock_exc, boot_option="local")

    def test_make_partitions_local_boot_uefi(self, mock_exc):
        self._test_make_partitions(mock_exc, boot_option="local",
                                   boot_mode="uefi", disk_label="gpt")

    def test_make_partitions_local_boot_gpt_bios(self, mock_exc):
        self._test_make_partitions(mock_exc, boot_option="local",
                                   disk_label="gpt")

    def test_make_partitions_disk_label_gpt(self, mock_exc):
        self._test_make_partitions(mock_exc, boot_option="netboot",
                                   disk_label="gpt")

    def test_make_partitions_mbr_with_prep(self, mock_exc):
        self._test_make_partitions(mock_exc, boot_option="local",
                                   disk_label="msdos", cpu_arch="ppc64le")

    def test_make_partitions_gpt_with_prep(self, mock_exc):
        self._test_make_partitions(mock_exc, boot_option="local",
                                   disk_label="gpt", cpu_arch="ppc64le")

    def test_make_partitions_with_ephemeral(self, mock_exc):
        self.ephemeral_mb = 2048
        expected_mkpart = ['mkpart', 'primary', '', '1', '2049',
                           'mkpart', 'primary', 'linux-swap', '2049', '2561',
                           'mkpart', 'primary', '', '2561', '3585']
        self.dev = 'fake-dev'
        cmd = self._get_parted_cmd(self.dev) + expected_mkpart
        mock_exc.return_value = ('', '')
        disk_utils.make_partitions(self.dev, self.root_mb, self.swap_mb,
                                   self.ephemeral_mb, self.configdrive_mb,
                                   self.node_uuid)

        parted_call = mock.call(*cmd, use_standard_locale=True,
                                run_as_root=True)
        mock_exc.assert_has_calls([parted_call])

    def test_make_partitions_with_iscsi_device(self, mock_exc):
        self.ephemeral_mb = 2048
        expected_mkpart = ['mkpart', 'primary', '', '1', '2049',
                           'mkpart', 'primary', 'linux-swap', '2049', '2561',
                           'mkpart', 'primary', '', '2561', '3585']
        self.dev = '/dev/iqn.2008-10.org.openstack:%s.fake-9' % self.node_uuid
        ep = '/dev/iqn.2008-10.org.openstack:%s.fake-9-part1' % self.node_uuid
        swap = ('/dev/iqn.2008-10.org.openstack:%s.fake-9-part2'
                % self.node_uuid)
        root = ('/dev/iqn.2008-10.org.openstack:%s.fake-9-part3'
                % self.node_uuid)
        expected_result = {'ephemeral': ep,
                           'swap': swap,
                           'root': root}
        cmd = self._get_parted_cmd(self.dev) + expected_mkpart
        mock_exc.return_value = ('', '')
        result = disk_utils.make_partitions(
            self.dev, self.root_mb, self.swap_mb, self.ephemeral_mb,
            self.configdrive_mb, self.node_uuid)

        parted_call = mock.call(*cmd, use_standard_locale=True,
                                run_as_root=True)
        mock_exc.assert_has_calls([parted_call])
        self.assertEqual(expected_result, result)

    def test_make_partitions_with_nvme_device(self, mock_exc):
        self.ephemeral_mb = 2048
        expected_mkpart = ['mkpart', 'primary', '', '1', '2049',
                           'mkpart', 'primary', 'linux-swap', '2049', '2561',
                           'mkpart', 'primary', '', '2561', '3585']
        self.dev = '/dev/nvmefake-9'
        ep = '/dev/nvmefake-9p1'
        swap = '/dev/nvmefake-9p2'
        root = '/dev/nvmefake-9p3'
        expected_result = {'ephemeral': ep,
                           'swap': swap,
                           'root': root}
        cmd = self._get_parted_cmd(self.dev) + expected_mkpart
        mock_exc.return_value = ('', '')
        result = disk_utils.make_partitions(
            self.dev, self.root_mb, self.swap_mb, self.ephemeral_mb,
            self.configdrive_mb, self.node_uuid)

        parted_call = mock.call(*cmd, use_standard_locale=True,
                                run_as_root=True)
        mock_exc.assert_has_calls([parted_call])
        self.assertEqual(expected_result, result)

    def test_make_partitions_with_local_device(self, mock_exc):
        self.ephemeral_mb = 2048
        expected_mkpart = ['mkpart', 'primary', '', '1', '2049',
                           'mkpart', 'primary', 'linux-swap', '2049', '2561',
                           'mkpart', 'primary', '', '2561', '3585']
        self.dev = 'fake-dev'
        expected_result = {'ephemeral': 'fake-dev1',
                           'swap': 'fake-dev2',
                           'root': 'fake-dev3'}
        cmd = self._get_parted_cmd(self.dev) + expected_mkpart
        mock_exc.return_value = ('', '')
        result = disk_utils.make_partitions(
            self.dev, self.root_mb, self.swap_mb, self.ephemeral_mb,
            self.configdrive_mb, self.node_uuid)

        parted_call = mock.call(*cmd, use_standard_locale=True,
                                run_as_root=True)
        mock_exc.assert_has_calls([parted_call])
        self.assertEqual(expected_result, result)


@mock.patch.object(utils, 'execute', autospec=True)
class DestroyMetaDataTestCase(base.IronicLibTestCase):

    def setUp(self):
        super(DestroyMetaDataTestCase, self).setUp()
        self.dev = 'fake-dev'
        self.node_uuid = "12345678-1234-1234-1234-1234567890abcxyz"

    def test_destroy_disk_metadata(self, mock_exec):
        # Note(TheJulia): This list will get-reused, but only the second
        # execution returning a string is needed for the test as otherwise
        # command output is not used.
        mock_exec.side_effect = iter([
            (None, None),
            ('1024\n', None),
            (None, None),
            (None, None),
            (None, None),
            (None, None)])

        expected_calls = [mock.call('wipefs', '--force', '--all', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('blockdev', '--getsz', 'fake-dev',
                                    run_as_root=True),
                          mock.call('dd', 'bs=512', 'if=/dev/zero',
                                    'of=fake-dev', 'count=33',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('dd', 'bs=512', 'if=/dev/zero',
                                    'of=fake-dev', 'count=33', 'seek=991',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('sgdisk', '-Z', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('fuser', self.dev,
                                    check_exit_code=[0, 1],
                                    run_as_root=True)]
        disk_utils.destroy_disk_metadata(self.dev, self.node_uuid)
        mock_exec.assert_has_calls(expected_calls)

    def test_destroy_disk_metadata_wipefs_fail(self, mock_exec):
        mock_exec.side_effect = processutils.ProcessExecutionError

        expected_call = [mock.call('wipefs', '--force', '--all', 'fake-dev',
                                   run_as_root=True,
                                   use_standard_locale=True)]
        self.assertRaises(processutils.ProcessExecutionError,
                          disk_utils.destroy_disk_metadata,
                          self.dev,
                          self.node_uuid)
        mock_exec.assert_has_calls(expected_call)

    def test_destroy_disk_metadata_sgdisk_fail(self, mock_exec):
        expected_calls = [mock.call('wipefs', '--force', '--all', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('blockdev', '--getsz', 'fake-dev',
                                    run_as_root=True),
                          mock.call('dd', 'bs=512', 'if=/dev/zero',
                                    'of=fake-dev', 'count=33',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('dd', 'bs=512', 'if=/dev/zero',
                                    'of=fake-dev', 'count=33', 'seek=991',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('sgdisk', '-Z', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True)]
        mock_exec.side_effect = iter([
            (None, None),
            ('1024\n', None),
            (None, None),
            (None, None),
            processutils.ProcessExecutionError()])
        self.assertRaises(processutils.ProcessExecutionError,
                          disk_utils.destroy_disk_metadata,
                          self.dev,
                          self.node_uuid)
        mock_exec.assert_has_calls(expected_calls)

    def test_destroy_disk_metadata_wipefs_not_support_force(self, mock_exec):
        mock_exec.side_effect = iter([
            processutils.ProcessExecutionError(description='--force'),
            (None, None),
            ('1024\n', None),
            (None, None),
            (None, None),
            (None, None),
            (None, None)])

        expected_call = [mock.call('wipefs', '--force', '--all', 'fake-dev',
                                   run_as_root=True,
                                   use_standard_locale=True),
                         mock.call('wipefs', '--all', 'fake-dev',
                                   run_as_root=True,
                                   use_standard_locale=True)]
        disk_utils.destroy_disk_metadata(self.dev, self.node_uuid)
        mock_exec.assert_has_calls(expected_call)

    def test_destroy_disk_metadata_ebr(self, mock_exec):
        expected_calls = [mock.call('wipefs', '--force', '--all', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('blockdev', '--getsz', 'fake-dev',
                                    run_as_root=True),
                          mock.call('dd', 'bs=512', 'if=/dev/zero',
                                    'of=fake-dev', 'count=2',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('sgdisk', '-Z', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True)]
        mock_exec.side_effect = iter([
            (None, None),
            ('2\n', None),  # an EBR is 2 sectors
            (None, None),
            (None, None),
            (None, None),
            (None, None)])
        disk_utils.destroy_disk_metadata(self.dev, self.node_uuid)
        mock_exec.assert_has_calls(expected_calls)

    def test_destroy_disk_metadata_tiny_partition(self, mock_exec):
        expected_calls = [mock.call('wipefs', '--force', '--all', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('blockdev', '--getsz', 'fake-dev',
                                    run_as_root=True),
                          mock.call('dd', 'bs=512', 'if=/dev/zero',
                                    'of=fake-dev', 'count=33',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('dd', 'bs=512', 'if=/dev/zero',
                                    'of=fake-dev', 'count=33', 'seek=9',
                                    run_as_root=True,
                                    use_standard_locale=True),
                          mock.call('sgdisk', '-Z', 'fake-dev',
                                    run_as_root=True,
                                    use_standard_locale=True)]
        mock_exec.side_effect = iter([
            (None, None),
            ('42\n', None),
            (None, None),
            (None, None),
            (None, None),
            (None, None)])
        disk_utils.destroy_disk_metadata(self.dev, self.node_uuid)
        mock_exec.assert_has_calls(expected_calls)


@mock.patch.object(utils, 'execute', autospec=True)
class GetDeviceBlockSizeTestCase(base.IronicLibTestCase):

    def setUp(self):
        super(GetDeviceBlockSizeTestCase, self).setUp()
        self.dev = 'fake-dev'
        self.node_uuid = "12345678-1234-1234-1234-1234567890abcxyz"

    def test_get_dev_block_size(self, mock_exec):
        mock_exec.return_value = ("64", "")
        expected_call = [mock.call('blockdev', '--getsz', self.dev,
                                   run_as_root=True)]
        disk_utils.get_dev_block_size(self.dev)
        mock_exec.assert_has_calls(expected_call)


@mock.patch.object(disk_utils, 'dd', autospec=True)
@mock.patch.object(disk_utils, 'qemu_img_info', autospec=True)
@mock.patch.object(disk_utils, 'convert_image', autospec=True)
class PopulateImageTestCase(base.IronicLibTestCase):

    def test_populate_raw_image(self, mock_cg, mock_qinfo, mock_dd):
        type(mock_qinfo.return_value).file_format = mock.PropertyMock(
            return_value='raw')
        disk_utils.populate_image('src', 'dst')
        mock_dd.assert_called_once_with('src', 'dst', conv_flags=None)
        self.assertFalse(mock_cg.called)

    def test_populate_raw_image_with_convert(self, mock_cg, mock_qinfo,
                                             mock_dd):
        type(mock_qinfo.return_value).file_format = mock.PropertyMock(
            return_value='raw')
        disk_utils.populate_image('src', 'dst', conv_flags='sparse')
        mock_dd.assert_called_once_with('src', 'dst', conv_flags='sparse')
        self.assertFalse(mock_cg.called)

    def test_populate_qcow2_image(self, mock_cg, mock_qinfo, mock_dd):
        type(mock_qinfo.return_value).file_format = mock.PropertyMock(
            return_value='qcow2')
        disk_utils.populate_image('src', 'dst')
        mock_cg.assert_called_once_with('src', 'dst', 'raw', True,
                                        sparse_size='0')
        self.assertFalse(mock_dd.called)


@mock.patch('time.sleep', lambda sec: None)
class OtherFunctionTestCase(base.IronicLibTestCase):

    @mock.patch.object(os, 'stat', autospec=True)
    @mock.patch.object(stat, 'S_ISBLK', autospec=True)
    def test_is_block_device_works(self, mock_is_blk, mock_os):
        device = '/dev/disk/by-path/ip-1.2.3.4:5678-iscsi-iqn.fake-lun-9'
        mock_is_blk.return_value = True
        mock_os().st_mode = 10000
        self.assertTrue(disk_utils.is_block_device(device))
        mock_is_blk.assert_called_once_with(mock_os().st_mode)

    @mock.patch.object(os, 'stat', autospec=True)
    def test_is_block_device_raises(self, mock_os):
        device = '/dev/disk/by-path/ip-1.2.3.4:5678-iscsi-iqn.fake-lun-9'
        mock_os.side_effect = OSError
        self.assertRaises(exception.InstanceDeployFailure,
                          disk_utils.is_block_device, device)
        mock_os.assert_has_calls([mock.call(device)] * 3)

    @mock.patch.object(os, 'stat', autospec=True)
    def test_is_block_device_attempts(self, mock_os):
        CONF.set_override('partition_detection_attempts', 2,
                          group='disk_utils')
        device = '/dev/disk/by-path/ip-1.2.3.4:5678-iscsi-iqn.fake-lun-9'
        mock_os.side_effect = OSError
        self.assertRaises(exception.InstanceDeployFailure,
                          disk_utils.is_block_device, device)
        mock_os.assert_has_calls([mock.call(device)] * 2)

    @mock.patch.object(imageutils, 'QemuImgInfo', autospec=True)
    @mock.patch.object(os.path, 'exists', return_value=False, autospec=True)
    def test_qemu_img_info_path_doesnt_exist(self, path_exists_mock,
                                             qemu_img_info_mock):
        disk_utils.qemu_img_info('noimg')
        path_exists_mock.assert_called_once_with('noimg')
        qemu_img_info_mock.assert_called_once_with()

    @mock.patch.object(utils, 'execute', return_value=('out', 'err'),
                       autospec=True)
    @mock.patch.object(imageutils, 'QemuImgInfo', autospec=True)
    @mock.patch.object(os.path, 'exists', return_value=True, autospec=True)
    def test_qemu_img_info_path_exists(self, path_exists_mock,
                                       qemu_img_info_mock, execute_mock):
        disk_utils.qemu_img_info('img')
        path_exists_mock.assert_called_once_with('img')
        execute_mock.assert_called_once_with('env', 'LC_ALL=C', 'LANG=C',
                                             'qemu-img', 'info', 'img',
                                             '--output=json',
                                             prlimit=mock.ANY)
        qemu_img_info_mock.assert_called_once_with('out', format='json')

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_convert_image(self, execute_mock):
        disk_utils.convert_image('source', 'dest', 'out_format')
        execute_mock.assert_called_once_with(
            'qemu-img', 'convert', '-O',
            'out_format', 'source', 'dest',
            run_as_root=False,
            prlimit=mock.ANY,
            use_standard_locale=True,
            env_variables={'MALLOC_ARENA_MAX': '3'})

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_convert_image_flags(self, execute_mock):
        disk_utils.convert_image('source', 'dest', 'out_format',
                                 cache='directsync', out_of_order=True,
                                 sparse_size='0')
        execute_mock.assert_called_once_with(
            'qemu-img', 'convert', '-O',
            'out_format', '-t', 'directsync',
            '-S', '0', '-W', 'source', 'dest',
            run_as_root=False,
            prlimit=mock.ANY,
            use_standard_locale=True,
            env_variables={'MALLOC_ARENA_MAX': '3'})

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_convert_image_retries(self, execute_mock):
        ret_err = 'qemu: qemu_thread_create: Resource temporarily unavailable'
        execute_mock.side_effect = [
            processutils.ProcessExecutionError(stderr=ret_err), ('', ''),
            processutils.ProcessExecutionError(stderr=ret_err), ('', ''),
            ('', ''),
        ]

        disk_utils.convert_image('source', 'dest', 'out_format')
        convert_call = mock.call('qemu-img', 'convert', '-O',
                                 'out_format', 'source', 'dest',
                                 run_as_root=False,
                                 prlimit=mock.ANY,
                                 use_standard_locale=True,
                                 env_variables={'MALLOC_ARENA_MAX': '3'})
        execute_mock.assert_has_calls([
            convert_call,
            mock.call('sync'),
            convert_call,
            mock.call('sync'),
            convert_call,
        ])

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_convert_image_retries_alternate_error(self, execute_mock):
        ret_err = 'Failed to allocate memory: Cannot allocate memory\n'
        execute_mock.side_effect = [
            processutils.ProcessExecutionError(stderr=ret_err), ('', ''),
            processutils.ProcessExecutionError(stderr=ret_err), ('', ''),
            ('', ''),
        ]

        disk_utils.convert_image('source', 'dest', 'out_format')
        convert_call = mock.call('qemu-img', 'convert', '-O',
                                 'out_format', 'source', 'dest',
                                 run_as_root=False,
                                 prlimit=mock.ANY,
                                 use_standard_locale=True,
                                 env_variables={'MALLOC_ARENA_MAX': '3'})
        execute_mock.assert_has_calls([
            convert_call,
            mock.call('sync'),
            convert_call,
            mock.call('sync'),
            convert_call,
        ])

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_convert_image_retries_and_fails(self, execute_mock):
        ret_err = 'qemu: qemu_thread_create: Resource temporarily unavailable'
        execute_mock.side_effect = [
            processutils.ProcessExecutionError(stderr=ret_err), ('', ''),
            processutils.ProcessExecutionError(stderr=ret_err), ('', ''),
            processutils.ProcessExecutionError(stderr=ret_err), ('', ''),
            processutils.ProcessExecutionError(stderr=ret_err),
        ]

        self.assertRaises(processutils.ProcessExecutionError,
                          disk_utils.convert_image,
                          'source', 'dest', 'out_format')
        convert_call = mock.call('qemu-img', 'convert', '-O',
                                 'out_format', 'source', 'dest',
                                 run_as_root=False,
                                 prlimit=mock.ANY,
                                 use_standard_locale=True,
                                 env_variables={'MALLOC_ARENA_MAX': '3'})
        execute_mock.assert_has_calls([
            convert_call,
            mock.call('sync'),
            convert_call,
            mock.call('sync'),
            convert_call,
        ])

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_convert_image_just_fails(self, execute_mock):
        ret_err = 'Aliens'
        execute_mock.side_effect = [
            processutils.ProcessExecutionError(stderr=ret_err),
        ]

        self.assertRaises(processutils.ProcessExecutionError,
                          disk_utils.convert_image,
                          'source', 'dest', 'out_format')
        convert_call = mock.call('qemu-img', 'convert', '-O',
                                 'out_format', 'source', 'dest',
                                 run_as_root=False,
                                 prlimit=mock.ANY,
                                 use_standard_locale=True,
                                 env_variables={'MALLOC_ARENA_MAX': '3'})
        execute_mock.assert_has_calls([
            convert_call,
        ])

    @mock.patch.object(os.path, 'getsize', autospec=True)
    @mock.patch.object(disk_utils, 'qemu_img_info', autospec=True)
    def test_get_image_mb(self, mock_qinfo, mock_getsize):
        mb = 1024 * 1024

        mock_getsize.return_value = 0
        type(mock_qinfo.return_value).virtual_size = mock.PropertyMock(
            return_value=0)
        self.assertEqual(0, disk_utils.get_image_mb('x', False))
        self.assertEqual(0, disk_utils.get_image_mb('x', True))
        mock_getsize.return_value = 1
        type(mock_qinfo.return_value).virtual_size = mock.PropertyMock(
            return_value=1)
        self.assertEqual(1, disk_utils.get_image_mb('x', False))
        self.assertEqual(1, disk_utils.get_image_mb('x', True))
        mock_getsize.return_value = mb
        type(mock_qinfo.return_value).virtual_size = mock.PropertyMock(
            return_value=mb)
        self.assertEqual(1, disk_utils.get_image_mb('x', False))
        self.assertEqual(1, disk_utils.get_image_mb('x', True))
        mock_getsize.return_value = mb + 1
        type(mock_qinfo.return_value).virtual_size = mock.PropertyMock(
            return_value=mb + 1)
        self.assertEqual(2, disk_utils.get_image_mb('x', False))
        self.assertEqual(2, disk_utils.get_image_mb('x', True))

    def _test_count_mbr_partitions(self, output, mock_execute):
        mock_execute.return_value = (output, '')
        out = disk_utils.count_mbr_partitions('/dev/fake')
        mock_execute.assert_called_once_with('partprobe', '-d', '-s',
                                             '/dev/fake', run_as_root=True,
                                             use_standard_locale=True)
        return out

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_count_mbr_partitions(self, mock_execute):
        output = "/dev/fake: msdos partitions 1 2 3 <5 6>"
        pp, lp = self._test_count_mbr_partitions(output, mock_execute)
        self.assertEqual(3, pp)
        self.assertEqual(2, lp)

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_count_mbr_partitions_no_logical_partitions(self, mock_execute):
        output = "/dev/fake: msdos partitions 1 2"
        pp, lp = self._test_count_mbr_partitions(output, mock_execute)
        self.assertEqual(2, pp)
        self.assertEqual(0, lp)

    @mock.patch.object(utils, 'execute', autospec=True)
    def test_count_mbr_partitions_wrong_partition_table(self, mock_execute):
        output = "/dev/fake: gpt partitions 1 2 3 4 5 6"
        mock_execute.return_value = (output, '')
        self.assertRaises(ValueError, disk_utils.count_mbr_partitions,
                          '/dev/fake')
        mock_execute.assert_called_once_with('partprobe', '-d', '-s',
                                             '/dev/fake', run_as_root=True,
                                             use_standard_locale=True)

    @mock.patch.object(disk_utils, 'get_device_information', autospec=True)
    def test_block_uuid(self, mock_get_device_info):
        mock_get_device_info.return_value = {'UUID': '123',
                                             'PARTUUID': '123456'}
        self.assertEqual('123', disk_utils.block_uuid('/dev/fake'))
        mock_get_device_info.assert_called_once_with(
            '/dev/fake', fields=['UUID', 'PARTUUID'])

    @mock.patch.object(disk_utils, 'get_device_information', autospec=True)
    def test_block_uuid_fallback_to_uuid(self, mock_get_device_info):
        mock_get_device_info.return_value = {'PARTUUID': '123456'}
        self.assertEqual('123456', disk_utils.block_uuid('/dev/fake'))
        mock_get_device_info.assert_called_once_with(
            '/dev/fake', fields=['UUID', 'PARTUUID'])


@mock.patch.object(utils, 'execute', autospec=True)
class FixGptStructsTestCases(base.IronicLibTestCase):

    def setUp(self):
        super(FixGptStructsTestCases, self).setUp()
        self.dev = "/dev/fake"
        self.config_part_label = "config-2"
        self.node_uuid = "12345678-1234-1234-1234-1234567890abcxyz"

    def test_fix_gpt_structs_fix_required(self, mock_execute):
        sgdisk_v_output = """
Problem: The secondary header's self-pointer indicates that it doesn't reside
at the end of the disk. If you've added a disk to a RAID array, use the 'e'
option on the experts' menu to adjust the secondary header's and partition
table's locations.

Identified 1 problems!
"""
        mock_execute.return_value = (sgdisk_v_output, '')
        execute_calls = [
            mock.call('sgdisk', '-v', '/dev/fake', run_as_root=True),
            mock.call('sgdisk', '-e', '/dev/fake', run_as_root=True)
        ]
        disk_utils._fix_gpt_structs('/dev/fake', self.node_uuid)
        mock_execute.assert_has_calls(execute_calls)

    def test_fix_gpt_structs_fix_not_required(self, mock_execute):
        mock_execute.return_value = ('', '')

        disk_utils._fix_gpt_structs('/dev/fake', self.node_uuid)
        mock_execute.assert_called_once_with('sgdisk', '-v', '/dev/fake',
                                             run_as_root=True)

    @mock.patch.object(disk_utils.LOG, 'error', autospec=True)
    def test_fix_gpt_structs_exc(self, mock_log, mock_execute):
        mock_execute.side_effect = processutils.ProcessExecutionError
        self.assertRaisesRegex(exception.InstanceDeployFailure,
                               'Failed to fix GPT data structures on disk',
                               disk_utils._fix_gpt_structs,
                               self.dev, self.node_uuid)
        mock_execute.assert_called_once_with('sgdisk', '-v', '/dev/fake',
                                             run_as_root=True)
        self.assertEqual(1, mock_log.call_count)


@mock.patch.object(utils, 'execute', autospec=True)
class TriggerDeviceRescanTestCase(base.IronicLibTestCase):
    def test_trigger(self, mock_execute):
        self.assertTrue(disk_utils.trigger_device_rescan('/dev/fake'))
        mock_execute.assert_has_calls([
            mock.call('sync'),
            mock.call('udevadm', 'settle'),
            mock.call('partprobe', '/dev/fake', run_as_root=True, attempts=10),
            mock.call('sgdisk', '-v', '/dev/fake', run_as_root=True),
        ])

    def test_custom_attempts(self, mock_execute):
        self.assertTrue(
            disk_utils.trigger_device_rescan('/dev/fake', attempts=1))
        mock_execute.assert_has_calls([
            mock.call('sync'),
            mock.call('udevadm', 'settle'),
            mock.call('partprobe', '/dev/fake', run_as_root=True, attempts=1),
            mock.call('sgdisk', '-v', '/dev/fake', run_as_root=True),
        ])

    def test_fails(self, mock_execute):
        mock_execute.side_effect = [('', '')] * 3 + [
            processutils.ProcessExecutionError
        ]
        self.assertFalse(disk_utils.trigger_device_rescan('/dev/fake'))
        mock_execute.assert_has_calls([
            mock.call('sync'),
            mock.call('udevadm', 'settle'),
            mock.call('partprobe', '/dev/fake', run_as_root=True, attempts=10),
            mock.call('sgdisk', '-v', '/dev/fake', run_as_root=True),
        ])


BLKID_PROBE = ("""
/dev/disk/by-path/ip-10.1.0.52:3260-iscsi-iqn.2008-10.org.openstack: """
               """PTUUID="123456" PTTYPE="gpt"
               """)

LSBLK_NORMAL = (
    'UUID="123" BLOCK_SIZE="512" TYPE="vfat" '
    'PARTLABEL="EFI System Partition" PARTUUID="123456"'
)


@mock.patch.object(utils, 'execute', autospec=True)
class GetDeviceInformationTestCase(base.IronicLibTestCase):

    def test_normal(self, mock_execute):
        mock_execute.return_value = LSBLK_NORMAL, ""
        result = disk_utils.get_device_information('/dev/fake')
        self.assertEqual(
            {'UUID': '123', 'BLOCK_SIZE': '512', 'TYPE': 'vfat',
             'PARTLABEL': 'EFI System Partition', 'PARTUUID': '123456'},
            result
        )
        mock_execute.assert_called_once_with(
            'lsblk', '/dev/fake', '--pairs', '--bytes', '--ascii', '--nodeps',
            '--output-all', use_standard_locale=True, run_as_root=True)

    def test_probe(self, mock_execute):
        mock_execute.return_value = BLKID_PROBE, ""
        result = disk_utils.get_device_information('/dev/fake', probe=True)
        self.assertEqual({'PTUUID': '123456', 'PTTYPE': 'gpt'}, result)
        mock_execute.assert_called_once_with('blkid', '/dev/fake', '-p',
                                             use_standard_locale=True,
                                             run_as_root=True)

    def test_fields(self, mock_execute):
        mock_execute.return_value = LSBLK_NORMAL, ""
        result = disk_utils.get_device_information('/dev/fake',
                                                   fields=['UUID', 'LABEL'])
        # No filtering on our side, so returning all fake fields
        self.assertEqual(
            {'UUID': '123', 'BLOCK_SIZE': '512', 'TYPE': 'vfat',
             'PARTLABEL': 'EFI System Partition', 'PARTUUID': '123456'},
            result
        )
        mock_execute.assert_called_once_with(
            'lsblk', '/dev/fake', '--pairs', '--bytes', '--ascii', '--nodeps',
            '--output', 'UUID,LABEL',
            use_standard_locale=True, run_as_root=True)

    def test_empty(self, mock_execute):
        mock_execute.return_value = "\n", ""
        result = disk_utils.get_device_information('/dev/fake', probe=True)
        self.assertEqual({}, result)
        mock_execute.assert_called_once_with('blkid', '/dev/fake',
                                             '-p', use_standard_locale=True,
                                             run_as_root=True)


@mock.patch.object(utils, 'execute', autospec=True)
class GetPartitionTableTypeTestCase(base.IronicLibTestCase):
    def test_gpt(self, mocked_execute):
        self._test_by_type(mocked_execute, 'gpt', 'gpt')

    def test_msdos(self, mocked_execute):
        self._test_by_type(mocked_execute, 'msdos', 'msdos')

    def test_unknown(self, mocked_execute):
        self._test_by_type(mocked_execute, 'whatever', 'unknown')

    def _test_by_type(self, mocked_execute, table_type_output,
                      expected_table_type):
        parted_ret = PARTED_OUTPUT_UNFORMATTED.format(table_type_output)

        mocked_execute.side_effect = [
            (parted_ret, None),
        ]

        ret = disk_utils.get_partition_table_type('hello')
        mocked_execute.assert_called_once_with(
            'parted', '--script', 'hello', '--', 'print',
            run_as_root=True, use_standard_locale=True)
        self.assertEqual(expected_table_type, ret)


PARTED_OUTPUT_UNFORMATTED = '''Model: whatever
Disk /dev/sda: 450GB
Sector size (logical/physical): 512B/512B
Partition Table: {}
Disk Flags:

Number  Start   End     Size    File system  Name  Flags
14      1049kB  5243kB  4194kB                     bios_grub
15      5243kB  116MB   111MB   fat32              boot, esp
 1      116MB   2361MB  2245MB  ext4
'''


@mock.patch.object(disk_utils, 'list_partitions', autospec=True)
@mock.patch.object(disk_utils, 'get_partition_table_type', autospec=True)
class FindEfiPartitionTestCase(base.IronicLibTestCase):

    def test_find_efi_partition(self, mocked_type, mocked_parts):
        mocked_parts.return_value = [
            {'number': '1', 'flags': ''},
            {'number': '14', 'flags': 'bios_grub'},
            {'number': '15', 'flags': 'esp, boot'},
        ]
        ret = disk_utils.find_efi_partition('/dev/sda')
        self.assertEqual({'number': '15', 'flags': 'esp, boot'}, ret)

    def test_find_efi_partition_only_boot_flag_gpt(self, mocked_type,
                                                   mocked_parts):
        mocked_type.return_value = 'gpt'
        mocked_parts.return_value = [
            {'number': '1', 'flags': ''},
            {'number': '14', 'flags': 'bios_grub'},
            {'number': '15', 'flags': 'boot'},
        ]
        ret = disk_utils.find_efi_partition('/dev/sda')
        self.assertEqual({'number': '15', 'flags': 'boot'}, ret)

    def test_find_efi_partition_only_boot_flag_mbr(self, mocked_type,
                                                   mocked_parts):
        mocked_type.return_value = 'msdos'
        mocked_parts.return_value = [
            {'number': '1', 'flags': ''},
            {'number': '14', 'flags': 'bios_grub'},
            {'number': '15', 'flags': 'boot'},
        ]
        self.assertIsNone(disk_utils.find_efi_partition('/dev/sda'))

    def test_find_efi_partition_not_found(self, mocked_type, mocked_parts):
        mocked_parts.return_value = [
            {'number': '1', 'flags': ''},
            {'number': '14', 'flags': 'bios_grub'},
        ]
        self.assertIsNone(disk_utils.find_efi_partition('/dev/sda'))
