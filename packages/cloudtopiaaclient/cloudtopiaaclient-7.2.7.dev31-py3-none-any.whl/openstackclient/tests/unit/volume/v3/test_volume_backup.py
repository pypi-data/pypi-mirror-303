#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

from unittest.mock import call

from osc_lib import exceptions

from openstackclient.tests.unit.volume.v3 import fakes as volume_fakes
from openstackclient.volume.v3 import volume_backup


class TestBackupLegacy(volume_fakes.TestVolume):
    def setUp(self):
        super().setUp()

        self.backups_mock = self.volume_client.backups
        self.backups_mock.reset_mock()
        self.volumes_mock = self.volume_client.volumes
        self.volumes_mock.reset_mock()
        self.snapshots_mock = self.volume_client.volume_snapshots
        self.snapshots_mock.reset_mock()
        self.restores_mock = self.volume_client.restores
        self.restores_mock.reset_mock()


class TestBackupCreate(volume_fakes.TestVolume):
    volume = volume_fakes.create_one_volume()
    snapshot = volume_fakes.create_one_snapshot()
    new_backup = volume_fakes.create_one_backup(
        attrs={'volume_id': volume.id, 'snapshot_id': snapshot.id}
    )

    columns = (
        'id',
        'name',
        'volume_id',
    )
    data = (
        new_backup.id,
        new_backup.name,
        new_backup.volume_id,
    )

    def setUp(self):
        super().setUp()

        self.volume_sdk_client.find_volume.return_value = self.volume
        self.volume_sdk_client.find_snapshot.return_value = self.snapshot
        self.volume_sdk_client.create_backup.return_value = self.new_backup

        # Get the command object to test
        self.cmd = volume_backup.CreateVolumeBackup(self.app, None)

    def test_backup_create(self):
        arglist = [
            "--name",
            self.new_backup.name,
            "--description",
            self.new_backup.description,
            "--container",
            self.new_backup.container,
            "--force",
            "--incremental",
            "--snapshot",
            self.new_backup.snapshot_id,
            self.new_backup.volume_id,
        ]
        verifylist = [
            ("name", self.new_backup.name),
            ("description", self.new_backup.description),
            ("container", self.new_backup.container),
            ("force", True),
            ("incremental", True),
            ("snapshot", self.new_backup.snapshot_id),
            ("volume", self.new_backup.volume_id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        columns, data = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.create_backup.assert_called_with(
            volume_id=self.new_backup.volume_id,
            container=self.new_backup.container,
            name=self.new_backup.name,
            description=self.new_backup.description,
            force=True,
            is_incremental=True,
            snapshot_id=self.new_backup.snapshot_id,
        )
        self.assertEqual(self.columns, columns)
        self.assertEqual(self.data, data)

    def test_backup_create_with_properties(self):
        self.set_volume_api_version('3.43')

        arglist = [
            "--property",
            "foo=bar",
            "--property",
            "wow=much-cool",
            self.new_backup.volume_id,
        ]
        verifylist = [
            ("properties", {"foo": "bar", "wow": "much-cool"}),
            ("volume", self.new_backup.volume_id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        columns, data = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.create_backup.assert_called_with(
            volume_id=self.new_backup.volume_id,
            container=None,
            name=None,
            description=None,
            force=False,
            is_incremental=False,
            metadata={"foo": "bar", "wow": "much-cool"},
        )
        self.assertEqual(self.columns, columns)
        self.assertEqual(self.data, data)

    def test_backup_create_with_properties_pre_v343(self):
        self.set_volume_api_version('3.42')

        arglist = [
            "--property",
            "foo=bar",
            "--property",
            "wow=much-cool",
            self.new_backup.volume_id,
        ]
        verifylist = [
            ("properties", {"foo": "bar", "wow": "much-cool"}),
            ("volume", self.new_backup.volume_id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        exc = self.assertRaises(
            exceptions.CommandError, self.cmd.take_action, parsed_args
        )
        self.assertIn("--ct-volume-api-version 3.43 or greater", str(exc))

    def test_backup_create_with_availability_zone(self):
        self.set_volume_api_version('3.51')

        arglist = [
            "--availability-zone",
            "my-az",
            self.new_backup.volume_id,
        ]
        verifylist = [
            ("availability_zone", "my-az"),
            ("volume", self.new_backup.volume_id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        columns, data = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.create_backup.assert_called_with(
            volume_id=self.new_backup.volume_id,
            container=None,
            name=None,
            description=None,
            force=False,
            is_incremental=False,
            availability_zone="my-az",
        )
        self.assertEqual(self.columns, columns)
        self.assertEqual(self.data, data)

    def test_backup_create_with_availability_zone_pre_v351(self):
        self.set_volume_api_version('3.50')

        arglist = [
            "--availability-zone",
            "my-az",
            self.new_backup.volume_id,
        ]
        verifylist = [
            ("availability_zone", "my-az"),
            ("volume", self.new_backup.volume_id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        exc = self.assertRaises(
            exceptions.CommandError, self.cmd.take_action, parsed_args
        )
        self.assertIn("--ct-volume-api-version 3.51 or greater", str(exc))

    def test_backup_create_without_name(self):
        arglist = [
            "--description",
            self.new_backup.description,
            "--container",
            self.new_backup.container,
            self.new_backup.volume_id,
        ]
        verifylist = [
            ("description", self.new_backup.description),
            ("container", self.new_backup.container),
            ("volume", self.new_backup.volume_id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        columns, data = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.create_backup.assert_called_with(
            volume_id=self.new_backup.volume_id,
            container=self.new_backup.container,
            name=None,
            description=self.new_backup.description,
            force=False,
            is_incremental=False,
        )
        self.assertEqual(self.columns, columns)
        self.assertEqual(self.data, data)


class TestBackupDelete(volume_fakes.TestVolume):
    backups = volume_fakes.create_backups(count=2)

    def setUp(self):
        super().setUp()

        self.volume_sdk_client.find_backup = volume_fakes.get_backups(
            self.backups
        )
        self.volume_sdk_client.delete_backup.return_value = None

        # Get the command object to mock
        self.cmd = volume_backup.DeleteVolumeBackup(self.app, None)

    def test_backup_delete(self):
        arglist = [self.backups[0].id]
        verifylist = [("backups", [self.backups[0].id])]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.delete_backup.assert_called_with(
            self.backups[0].id, ignore_missing=False, force=False
        )
        self.assertIsNone(result)

    def test_backup_delete_with_force(self):
        arglist = [
            '--force',
            self.backups[0].id,
        ]
        verifylist = [('force', True), ("backups", [self.backups[0].id])]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.delete_backup.assert_called_with(
            self.backups[0].id, ignore_missing=False, force=True
        )
        self.assertIsNone(result)

    def test_delete_multiple_backups(self):
        arglist = []
        for b in self.backups:
            arglist.append(b.id)
        verifylist = [
            ('backups', arglist),
        ]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        result = self.cmd.take_action(parsed_args)

        calls = []
        for b in self.backups:
            calls.append(call(b.id, ignore_missing=False, force=False))
        self.volume_sdk_client.delete_backup.assert_has_calls(calls)
        self.assertIsNone(result)

    def test_delete_multiple_backups_with_exception(self):
        arglist = [
            self.backups[0].id,
            'unexist_backup',
        ]
        verifylist = [
            ('backups', arglist),
        ]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        find_mock_result = [self.backups[0], exceptions.CommandError]
        self.volume_sdk_client.find_backup.side_effect = find_mock_result

        try:
            self.cmd.take_action(parsed_args)
            self.fail('CommandError should be raised.')
        except exceptions.CommandError as e:
            self.assertEqual('1 of 2 backups failed to delete.', str(e))

        self.volume_sdk_client.find_backup.assert_any_call(
            self.backups[0].id, ignore_missing=False
        )
        self.volume_sdk_client.find_backup.assert_any_call(
            'unexist_backup', ignore_missing=False
        )

        self.assertEqual(2, self.volume_sdk_client.find_backup.call_count)
        self.volume_sdk_client.delete_backup.assert_called_once_with(
            self.backups[0].id,
            ignore_missing=False,
            force=False,
        )


class TestBackupList(volume_fakes.TestVolume):
    volume = volume_fakes.create_one_volume()
    backups = volume_fakes.create_backups(
        attrs={'volume_id': volume.name}, count=3
    )

    columns = (
        'ID',
        'Name',
        'Description',
        'Status',
        'Size',
        'Incremental',
    )
    columns_long = columns + (
        'Availability Zone',
        'Volume',
        'Container',
    )

    data = []
    for b in backups:
        data.append(
            (
                b.id,
                b.name,
                b.description,
                b.status,
                b.size,
                b.is_incremental,
            )
        )
    data_long = []
    for b in backups:
        data_long.append(
            (
                b.id,
                b.name,
                b.description,
                b.status,
                b.size,
                b.is_incremental,
                b.availability_zone,
                volume_backup.VolumeIdColumn(b.volume_id),
                b.container,
            )
        )

    def setUp(self):
        super().setUp()

        self.volume_sdk_client.volumes.return_value = [self.volume]
        self.volume_sdk_client.backups.return_value = self.backups
        self.volume_sdk_client.find_volume.return_value = self.volume
        self.volume_sdk_client.find_backup.return_value = self.backups[0]

        # Get the command to test
        self.cmd = volume_backup.ListVolumeBackup(self.app, None)

    def test_backup_list_without_options(self):
        arglist = []
        verifylist = [
            ("long", False),
            ("name", None),
            ("status", None),
            ("volume", None),
            ("marker", None),
            ("limit", None),
            ('all_projects', False),
        ]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.find_volume.assert_not_called()
        self.volume_sdk_client.find_backup.assert_not_called()
        self.volume_sdk_client.backups.assert_called_with(
            name=None,
            status=None,
            volume_id=None,
            all_tenants=False,
            marker=None,
            limit=None,
        )
        self.assertEqual(self.columns, columns)
        self.assertCountEqual(self.data, list(data))

    def test_backup_list_with_options(self):
        arglist = [
            "--long",
            "--name",
            self.backups[0].name,
            "--status",
            "error",
            "--volume",
            self.volume.id,
            "--marker",
            self.backups[0].id,
            "--all-projects",
            "--limit",
            "3",
        ]
        verifylist = [
            ("long", True),
            ("name", self.backups[0].name),
            ("status", "error"),
            ("volume", self.volume.id),
            ("marker", self.backups[0].id),
            ('all_projects', True),
            ("limit", 3),
        ]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        self.volume_sdk_client.find_volume.assert_called_once_with(
            self.volume.id, ignore_missing=False
        )
        self.volume_sdk_client.find_backup.assert_called_once_with(
            self.backups[0].id, ignore_missing=False
        )
        self.volume_sdk_client.backups.assert_called_with(
            name=self.backups[0].name,
            status="error",
            volume_id=self.volume.id,
            all_tenants=True,
            marker=self.backups[0].id,
            limit=3,
        )
        self.assertEqual(self.columns_long, columns)
        self.assertCountEqual(self.data_long, list(data))


class TestBackupRestore(volume_fakes.TestVolume):
    volume = volume_fakes.create_one_volume()
    backup = volume_fakes.create_one_backup(
        attrs={'volume_id': volume.id},
    )

    def setUp(self):
        super().setUp()

        self.volume_sdk_client.find_backup.return_value = self.backup
        self.volume_sdk_client.find_volume.return_value = self.volume
        self.volume_sdk_client.restore_backup.return_value = (
            volume_fakes.create_one_volume(
                {'id': self.volume['id']},
            )
        )

        # Get the command object to mock
        self.cmd = volume_backup.RestoreVolumeBackup(self.app, None)

    def test_backup_restore(self):
        self.volume_sdk_client.find_volume.side_effect = (
            exceptions.CommandError()
        )
        arglist = [self.backup.id]
        verifylist = [
            ("backup", self.backup.id),
            ("volume", None),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)
        self.volume_sdk_client.restore_backup.assert_called_with(
            self.backup.id,
            volume_id=None,
            name=None,
        )
        self.assertIsNotNone(result)

    def test_backup_restore_with_volume(self):
        self.volume_sdk_client.find_volume.side_effect = (
            exceptions.CommandError()
        )
        arglist = [
            self.backup.id,
            self.backup.volume_id,
        ]
        verifylist = [
            ("backup", self.backup.id),
            ("volume", self.backup.volume_id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)
        self.volume_sdk_client.restore_backup.assert_called_with(
            self.backup.id,
            volume_id=None,
            name=self.backup.volume_id,
        )
        self.assertIsNotNone(result)

    def test_backup_restore_with_volume_force(self):
        arglist = [
            "--force",
            self.backup.id,
            self.volume.name,
        ]
        verifylist = [
            ("force", True),
            ("backup", self.backup.id),
            ("volume", self.volume.name),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)
        self.volume_sdk_client.restore_backup.assert_called_with(
            self.backup.id,
            volume_id=self.volume.id,
            name=None,
        )
        self.assertIsNotNone(result)

    def test_backup_restore_with_volume_existing(self):
        arglist = [
            self.backup.id,
            self.volume.name,
        ]
        verifylist = [
            ("backup", self.backup.id),
            ("volume", self.volume.name),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.assertRaises(
            exceptions.CommandError,
            self.cmd.take_action,
            parsed_args,
        )


class TestBackupSet(TestBackupLegacy):
    backup = volume_fakes.create_one_backup(
        attrs={'metadata': {'wow': 'cool'}},
    )

    def setUp(self):
        super().setUp()

        self.backups_mock.get.return_value = self.backup

        # Get the command object to test
        self.cmd = volume_backup.SetVolumeBackup(self.app, None)

    def test_backup_set_name(self):
        self.set_volume_api_version('3.9')

        arglist = [
            '--name',
            'new_name',
            self.backup.id,
        ]
        verifylist = [
            ('name', 'new_name'),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        # In base command class ShowOne in cliff, abstract method take_action()
        # returns nothing
        result = self.cmd.take_action(parsed_args)
        self.backups_mock.update.assert_called_once_with(
            self.backup.id, **{'name': 'new_name'}
        )
        self.assertIsNone(result)

    def test_backup_set_name_pre_v39(self):
        self.set_volume_api_version('3.8')

        arglist = [
            '--name',
            'new_name',
            self.backup.id,
        ]
        verifylist = [
            ('name', 'new_name'),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        exc = self.assertRaises(
            exceptions.CommandError, self.cmd.take_action, parsed_args
        )
        self.assertIn("--ct-volume-api-version 3.9 or greater", str(exc))

    def test_backup_set_description(self):
        self.set_volume_api_version('3.9')

        arglist = [
            '--description',
            'new_description',
            self.backup.id,
        ]
        verifylist = [
            ('name', None),
            ('description', 'new_description'),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)

        # Set expected values
        kwargs = {'description': 'new_description'}
        self.backups_mock.update.assert_called_once_with(
            self.backup.id, **kwargs
        )
        self.assertIsNone(result)

    def test_backup_set_description_pre_v39(self):
        self.set_volume_api_version('3.8')

        arglist = [
            '--description',
            'new_description',
            self.backup.id,
        ]
        verifylist = [
            ('name', None),
            ('description', 'new_description'),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        exc = self.assertRaises(
            exceptions.CommandError, self.cmd.take_action, parsed_args
        )
        self.assertIn("--ct-volume-api-version 3.9 or greater", str(exc))

    def test_backup_set_state(self):
        arglist = ['--state', 'error', self.backup.id]
        verifylist = [('state', 'error'), ('backup', self.backup.id)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)
        self.backups_mock.reset_state.assert_called_once_with(
            self.backup.id, 'error'
        )
        self.assertIsNone(result)

    def test_backup_set_state_failed(self):
        self.backups_mock.reset_state.side_effect = exceptions.CommandError()
        arglist = ['--state', 'error', self.backup.id]
        verifylist = [('state', 'error'), ('backup', self.backup.id)]

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        try:
            self.cmd.take_action(parsed_args)
            self.fail('CommandError should be raised.')
        except exceptions.CommandError as e:
            self.assertEqual(
                'One or more of the set operations failed', str(e)
            )
        self.backups_mock.reset_state.assert_called_with(
            self.backup.id, 'error'
        )

    def test_backup_set_no_property(self):
        self.set_volume_api_version('3.43')

        arglist = [
            '--no-property',
            self.backup.id,
        ]
        verifylist = [
            ('no_property', True),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)

        # Set expected values
        kwargs = {
            'metadata': {},
        }
        self.backups_mock.update.assert_called_once_with(
            self.backup.id, **kwargs
        )
        self.assertIsNone(result)

    def test_backup_set_no_property_pre_v343(self):
        self.set_volume_api_version('3.42')

        arglist = [
            '--no-property',
            self.backup.id,
        ]
        verifylist = [
            ('no_property', True),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        exc = self.assertRaises(
            exceptions.CommandError, self.cmd.take_action, parsed_args
        )
        self.assertIn("--ct-volume-api-version 3.43 or greater", str(exc))

    def test_backup_set_property(self):
        self.set_volume_api_version('3.43')

        arglist = [
            '--property',
            'foo=bar',
            self.backup.id,
        ]
        verifylist = [
            ('properties', {'foo': 'bar'}),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)

        # Set expected values
        kwargs = {
            'metadata': {'wow': 'cool', 'foo': 'bar'},
        }
        self.backups_mock.update.assert_called_once_with(
            self.backup.id, **kwargs
        )
        self.assertIsNone(result)

    def test_backup_set_property_pre_v343(self):
        self.set_volume_api_version('3.42')

        arglist = [
            '--property',
            'foo=bar',
            self.backup.id,
        ]
        verifylist = [
            ('properties', {'foo': 'bar'}),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        exc = self.assertRaises(
            exceptions.CommandError, self.cmd.take_action, parsed_args
        )
        self.assertIn("--ct-volume-api-version 3.43 or greater", str(exc))


class TestBackupUnset(TestBackupLegacy):
    backup = volume_fakes.create_one_backup(
        attrs={'metadata': {'foo': 'bar'}},
    )

    def setUp(self):
        super().setUp()

        self.backups_mock.get.return_value = self.backup

        # Get the command object to test
        self.cmd = volume_backup.UnsetVolumeBackup(self.app, None)

    def test_backup_unset_property(self):
        self.set_volume_api_version('3.43')

        arglist = [
            '--property',
            'foo',
            self.backup.id,
        ]
        verifylist = [
            ('properties', ['foo']),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        result = self.cmd.take_action(parsed_args)

        # Set expected values
        kwargs = {
            'metadata': {},
        }
        self.backups_mock.update.assert_called_once_with(
            self.backup.id, **kwargs
        )
        self.assertIsNone(result)

    def test_backup_unset_property_pre_v343(self):
        self.set_volume_api_version('3.42')

        arglist = [
            '--property',
            'foo',
            self.backup.id,
        ]
        verifylist = [
            ('properties', ['foo']),
            ('backup', self.backup.id),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        exc = self.assertRaises(
            exceptions.CommandError, self.cmd.take_action, parsed_args
        )
        self.assertIn("--ct-volume-api-version 3.43 or greater", str(exc))


class TestBackupShow(volume_fakes.TestVolume):
    backup = volume_fakes.create_one_backup()

    columns = (
        "availability_zone",
        "container",
        "created_at",
        "data_timestamp",
        "description",
        "encryption_key_id",
        "fail_reason",
        "has_dependent_backups",
        "id",
        "is_incremental",
        "metadata",
        "name",
        "object_count",
        "project_id",
        "size",
        "snapshot_id",
        "status",
        "updated_at",
        "user_id",
        "volume_id",
    )
    data = (
        backup.availability_zone,
        backup.container,
        backup.created_at,
        backup.data_timestamp,
        backup.description,
        backup.encryption_key_id,
        backup.fail_reason,
        backup.has_dependent_backups,
        backup.id,
        backup.is_incremental,
        backup.metadata,
        backup.name,
        backup.object_count,
        backup.project_id,
        backup.size,
        backup.snapshot_id,
        backup.status,
        backup.updated_at,
        backup.user_id,
        backup.volume_id,
    )

    def setUp(self):
        super().setUp()

        self.volume_sdk_client.get_backup.return_value = self.backup
        # Get the command object to test
        self.cmd = volume_backup.ShowVolumeBackup(self.app, None)

    def test_backup_show(self):
        arglist = [self.backup.id]
        verifylist = [("backup", self.backup.id)]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        columns, data = self.cmd.take_action(parsed_args)
        self.volume_sdk_client.get_backup.assert_called_with(self.backup.id)

        self.assertEqual(self.columns, columns)
        self.assertEqual(self.data, data)
