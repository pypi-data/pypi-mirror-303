# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unittest Lab exercise to test implementation of "Synonym Dictionary"."""
import io
import os
import re
import subprocess
import sys
import time
import traceback
import unittest
from unittest import mock

from absl import flags
from absl.testing import flagsaver
from absl.testing import xml_reporter
from mobly.controllers import android_device
from mobly.controllers.android_device_lib import adb
from mobly.snippet import errors as snippet_errors

from ui_automator import errors
from ui_automator import test_reporter
from ui_automator import ui_automator
from ui_automator import unit_test_utils
from ui_automator import version

_FAKE_MATTER_DEVICE_NAME = 'fake-matter-device-name'
_FAKE_GHA_ROOM = 'Office'
_FAKE_PAIRING_CODE = '34970112332'
_GOOGLE_HOME_APP = {
    'id': 'gha',
    'name': 'Google Home Application (GHA)',
    'minVersion': '3.1.18.1',
    'minMatter': '231456000',
    'minThread': '231456000',
}
_PYTHON_PATH = subprocess.check_output(['which', 'python']).decode('utf-8')
_PYTHON_BIN_PATH = _PYTHON_PATH.removesuffix('python')
_FAKE_VALID_SYS_ARGV_FOR_COMMISSION = [
    _PYTHON_BIN_PATH + 'ui-automator',
    '--commission',
    'm5stack,34970112332,Office',
]
_FAKE_VALID_SYS_ARGV_FOR_DECOMMISSION = [
    _PYTHON_BIN_PATH + 'ui-automator',
    '--decommission',
    'm5stack',
]
_FAKE_VALID_SYS_ARGV_FOR_REGRESSION_TESTS = [
    _PYTHON_BIN_PATH + 'ui-automator',
    '--commission',
    'm5stack,34970112332,Office',
    '--regtest',
    '--repeat',
    '3',
]
_FAKE_INVALID_SYS_ARGV_FOR_REGRESSION_TESTS = [
    _PYTHON_BIN_PATH + 'ui-automator',
    '--regtest',
    '--repeat',
    '5',
]
_FAKE_SYS_ARGV_FOR_COMMISSION_WITH_INVALID_LENGTH = [
    _PYTHON_BIN_PATH + 'ui-automator',
    '--commission',
    'm5',
]
_FAKE_SYS_ARGV_FOR_COMMISSION_WITH_EMPTY_VALUE = [
    _PYTHON_BIN_PATH + 'ui-automator',
    '--commission',
]
_FAKE_PROJECT_FOLDER = '/path/to/'
_EXPECTED_APK_PATH = f'{_FAKE_PROJECT_FOLDER}android/app/snippet.apk'


class UIAutomatorTest(unittest.TestCase):

  def setUp(self):
    """This method will be run before each of the test methods in the class."""
    super().setUp()
    self.ui_automator = ui_automator.UIAutomator()
    self.mock_android_device = mock.patch.object(
        android_device, 'AndroidDevice'
    ).start()
    self.addCleanup(mock.patch.stopall)

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_load_device_raises_an_error_when_adb_not_installed(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.side_effect = adb.AdbError(
        cmd='adb devices',
        stdout='fake_msg',
        stderr='adb command not found',
        ret_code=1,
    )
    with self.assertRaisesRegex(
        errors.AdbError,
        r'Please install adb and add it to your PATH environment variable\.',
    ):
      self.ui_automator.load_device()

  @mock.patch.object(
      android_device, 'get_all_instances', autospec=True, return_value=[]
  )
  def test_load_device_no_android_device_error(
      self, unused_mock_get_all_instances
  ):
    with self.assertRaises(errors.NoAndroidDeviceError):
      self.ui_automator.load_device()

  @mock.patch.object(
      android_device, 'get_all_instances', autospec=True, return_value=[1, 2]
  )
  def test_load_device_success(self, unused_mock_get_all_instances):
    with self.assertLogs() as cm:
      self.ui_automator.load_device()
    self.assertEqual(cm.output, ['INFO:root:connected device: [1]'])

  def test_load_snippet_without_load_device_raises_error(self):
    with self.assertRaises(errors.NoAndroidDeviceError):
      self.ui_automator.load_snippet()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_load_snippet_success(self, mock_get_all_instances):
    mock_get_all_instances.return_value = [self.mock_android_device]

    self.ui_automator.load_device()
    self.ui_automator.load_snippet()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_load_snippet_fails_with_server_start_pre_check_error(
      self, mock_get_all_instances
  ):
    self.mock_android_device.load_snippet.side_effect = (
        snippet_errors.ServerStartPreCheckError('fake_ad', 'fake_msg')
    )
    mock_get_all_instances.return_value = [self.mock_android_device]

    self.ui_automator.load_device()

    with self.assertRaises(errors.AndroidDeviceNotReadyError):
      self.ui_automator.load_snippet()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_load_snippet_fails_with_server_start_error(
      self, mock_get_all_instances
  ):
    self.mock_android_device.load_snippet.side_effect = (
        snippet_errors.ServerStartError('fake_ad', 'fake_msg')
    )
    mock_get_all_instances.return_value = [self.mock_android_device]

    self.ui_automator.load_device()

    with self.assertRaises(errors.AndroidDeviceNotReadyError):
      self.ui_automator.load_snippet()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_load_snippet_fails_with_protocol_error(self, mock_get_all_instances):
    self.mock_android_device.load_snippet.side_effect = (
        snippet_errors.ProtocolError('fake_ad', 'fake_msg')
    )
    mock_get_all_instances.return_value = [self.mock_android_device]

    self.ui_automator.load_device()

    with self.assertRaises(errors.AndroidDeviceNotReadyError):
      self.ui_automator.load_snippet()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_load_snippet_fails_with_snippet_error(self, mock_get_all_instances):
    self.mock_android_device.load_snippet.side_effect = (
        android_device.SnippetError('fake_device', 'fake_msg')
    )
    mock_get_all_instances.return_value = [self.mock_android_device]

    self.ui_automator.load_device()

    with self.assertLogs(level='DEBUG') as cm:
      self.ui_automator.load_snippet()
    self.assertEqual(
        cm.output,
        [
            "DEBUG:root:'fake_device'::Service<SnippetManagementService>"
            ' fake_msg'
        ],
    )

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      os.path, 'dirname', autospec=True, return_value=_FAKE_PROJECT_FOLDER
  )
  def test_load_snippet_installs_apk_when_apk_is_not_installed(
      self, mock_dirname, mock_get_all_instances
  ):
    self.mock_android_device.adb.shell.return_value = b'package:installed.apk\n'
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.ui_automator.load_device()

    self.ui_automator.load_snippet()

    self.mock_android_device.adb.install.assert_called_once_with(
        ['-r', '-g', _EXPECTED_APK_PATH]
    )
    self.mock_android_device.adb.uninstall.assert_not_called()
    mock_dirname.assert_called_once()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      os.path, 'dirname', autospec=True, return_value=_FAKE_PROJECT_FOLDER
  )
  def test_load_snippet_should_not_install_apk_when_correct_apk_installed(
      self, mock_dirname, mock_get_all_instances
  ):
    self.mock_android_device.adb.shell.side_effect = [
        b'package:com.chip.interop.moblysnippet\n',
        f'versionName={version.VERSION}'.encode('utf-8'),
    ]
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.ui_automator.load_device()

    self.ui_automator.load_snippet()

    self.mock_android_device.adb.install.assert_not_called()
    self.mock_android_device.adb.uninstall.assert_not_called()
    mock_dirname.assert_not_called()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      os.path, 'dirname', autospec=True, return_value=_FAKE_PROJECT_FOLDER
  )
  def test_load_snippet_uninstalls_apk_before_installing_it_with_incorrect_apk(
      self, mock_dirname, mock_get_all_instances
  ):
    self.mock_android_device.adb.shell.side_effect = [
        b'package:com.chip.interop.moblysnippet\n',
        b'versionName=fake.version',
    ]
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.ui_automator.load_device()

    self.ui_automator.load_snippet()

    self.mock_android_device.adb.uninstall.assert_called_with(
        'com.chip.interop.moblysnippet'
    )
    self.mock_android_device.adb.install.assert_called_once_with(
        ['-r', '-g', _EXPECTED_APK_PATH]
    )
    mock_dirname.assert_called_once()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      os.path, 'dirname', autospec=True, return_value=_FAKE_PROJECT_FOLDER
  )
  def test_load_snippet_installs_apk_when_no_apk_installed(
      self, mock_dirname, mock_get_all_instances
  ):
    self.mock_android_device.adb.shell.side_effect = [
        b'package:installed.apk\n',
        b'Unable to find package\n',
    ]
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.ui_automator.load_device()

    self.ui_automator.load_snippet()

    self.mock_android_device.adb.uninstall.assert_not_called()
    self.mock_android_device.adb.install.assert_called_once_with(
        ['-r', '-g', _EXPECTED_APK_PATH]
    )
    mock_dirname.assert_called_once()

  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_android_device_ready_raises_an_error_when_load_device_throws_an_error(
      self, mock_load_snippet, mock_load_device
  ):
    mock_load_device.side_effect = errors.NoAndroidDeviceError(
        'No Android device connected to the host computer.'
    )

    @ui_automator.get_android_device_ready
    def decorated_function(self):
      del self
      pass

    with self.assertRaisesRegex(
        errors.AndroidDeviceNotReadyError, r'decorated_function failed\.'
    ):
      decorated_function(self.ui_automator)

    mock_load_device.assert_called_once()
    mock_load_snippet.assert_not_called()

  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_android_device_ready_raises_an_error_when_load_snippet_throws_an_error(
      self, mock_load_snippet, mock_load_device
  ):
    mock_load_snippet.side_effect = errors.AndroidDeviceNotReadyError(
        'Check device(fake-serial) has installed required apk.'
    )

    @ui_automator.get_android_device_ready
    def decorated_function(self):
      del self
      pass

    with self.assertRaisesRegex(
        errors.AndroidDeviceNotReadyError, r'decorated_function failed\.'
    ):
      decorated_function(self.ui_automator)

    mock_load_snippet.assert_called_once()
    mock_load_device.assert_called_once()

  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_android_device_ready_raises_no_error_on_success(
      self, mock_load_snippet, mock_load_device
  ):
    @ui_automator.get_android_device_ready
    def decorated_function(self):
      del self
      pass

    decorated_function(self.ui_automator)

    mock_load_snippet.assert_called_once()
    mock_load_device.assert_called_once()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_commission_device_raises_an_error_when_device_is_not_ready(
      self, mock_load_snippet, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    error_msg = 'Check device(fake-serial) is ready.'
    mock_load_snippet.side_effect = errors.AndroidDeviceNotReadyError(error_msg)

    with self.assertRaisesRegex(
        errors.AndroidDeviceNotReadyError, 'commission_device failed.'
    ):
      self.ui_automator.commission_device(
          _FAKE_MATTER_DEVICE_NAME, _FAKE_PAIRING_CODE, _FAKE_GHA_ROOM
      )

  @mock.patch.object(ui_automator.UIAutomator, 'unload_snippet', autospec=True)
  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_get_android_device_ready_calls_unload_snippet_on_finish(
      self, mock_get_all_instances, mock_unload_snippet
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]

    @ui_automator.get_android_device_ready
    def decorated_function(self):
      del self
      pass

    decorated_function(self.ui_automator)

    mock_unload_snippet.assert_called_once()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_commission_device_calls_a_method_in_snippet_with_desired_args(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    expected_matter_device = {
        'id': '_fake_matter_device_name',
        'name': _FAKE_MATTER_DEVICE_NAME,
        'pairingCode': _FAKE_PAIRING_CODE,
        'roomName': _FAKE_GHA_ROOM,
    }

    self.ui_automator.commission_device(
        _FAKE_MATTER_DEVICE_NAME,
        _FAKE_PAIRING_CODE,
        _FAKE_GHA_ROOM,
    )

    self.mock_android_device.mbs.commissionDevice.assert_called_once_with(
        _GOOGLE_HOME_APP, expected_matter_device
    )

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_commission_device_fails_when_snippet_method_throws_an_error(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    expected_error_message = (
        'Unable to continue automated commissioning process on'
        f' device({self.mock_android_device.device_info["serial"]}).'
    )
    self.mock_android_device.mbs.commissionDevice.side_effect = Exception(
        'Can not find next button in the page.'
    )

    with self.assertRaises(errors.MoblySnippetError) as exc:
      self.ui_automator.commission_device(
          _FAKE_MATTER_DEVICE_NAME,
          _FAKE_PAIRING_CODE,
          _FAKE_GHA_ROOM,
      )

    self.assertIn(expected_error_message, str(exc.exception))

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_commission_device_raises_an_error_when_device_name_exceeds_limit(
      self, mock_get_all_instances
  ):
    invalid_device_name = 'fakeDeviceNameWith25Chars'
    mock_get_all_instances.return_value = [self.mock_android_device]

    with self.assertRaisesRegex(
        ValueError,
        'Value of DeviceName is invalid. Device name should be no more than 24'
        ' characters.',
    ):
      self.ui_automator.commission_device(
          invalid_device_name,
          _FAKE_PAIRING_CODE,
          _FAKE_GHA_ROOM,
      )

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_commission_device_raises_an_error_when_pairing_code_is_invalid(
      self, mock_get_all_instances
  ):
    invalid_pairing_code = '123456789'
    mock_get_all_instances.return_value = [self.mock_android_device]

    with self.assertRaisesRegex(
        ValueError,
        'Value of PairingCode is invalid. Paring code should be 11-digit or'
        ' 21-digit numeric code.',
    ):
      self.ui_automator.commission_device(
          device_name=_FAKE_MATTER_DEVICE_NAME,
          pairing_code=invalid_pairing_code,
          gha_room=_FAKE_GHA_ROOM,
      )

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_commission_device_raises_an_error_when_gha_room_is_invalid(
      self, mock_get_all_instances
  ):
    invalid_gha_room = 'Attic 2'
    mock_get_all_instances.return_value = [self.mock_android_device]

    with self.assertRaisesRegex(
        ValueError,
        (
            'Value of GHARoom is invalid. Valid values for GHARoom: Attic|Back'
            ' door|Backyard|Basement|Bathroom|Bedroom|Den|Dining'
            ' Room|Entryway|Family Room|Front door|Front'
            ' Yard|Garage|Hallway|Kitchen|Living Room|Master'
            ' Bedroom|Office|Shed|Side door'
        ),
    ):
      self.ui_automator.commission_device(
          device_name=_FAKE_MATTER_DEVICE_NAME,
          pairing_code=_FAKE_PAIRING_CODE,
          gha_room=invalid_gha_room,
      )

  @flagsaver.flagsaver(
      (ui_automator._COMMISSION, ['m5stack', '34970112332', 'Office'])
  )
  @mock.patch.object(sys, 'exit', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  def test_run_calls_commission_device_with_valid_arguments(
      self, mock_commission_device, mock_exit
  ):
    with mock.patch.object(sys, 'argv', _FAKE_VALID_SYS_ARGV_FOR_COMMISSION):
      ui_automator.run()

    mock_commission_device.assert_called_once_with(
        mock.ANY, 'm5stack', '34970112332', 'Office'
    )
    mock_exit.assert_called_once()

  @flagsaver.flagsaver((ui_automator._COMMISSION, ['m5']))
  def test_commission_with_cmd_invalid_arg_should_raise_an_error(self):
    with mock.patch.object(
        sys, 'argv', _FAKE_SYS_ARGV_FOR_COMMISSION_WITH_INVALID_LENGTH
    ):
      with self.assertRaises(flags.IllegalFlagValueError):
        ui_automator.run()

    self.mock_android_device.mbs.commissionDevice.assert_not_called()

  @mock.patch.object(sys.stderr, 'write', autospec=True)
  @mock.patch.object(sys, 'exit', autospec=True)
  def test_commission_with_cmd_invalid_args_should_stderr(
      self, mock_exit, mock_stderr_write
  ):
    with mock.patch.object(
        sys, 'argv', _FAKE_SYS_ARGV_FOR_COMMISSION_WITH_EMPTY_VALUE
    ):
      ui_automator.run()

    self.assertEqual(mock_stderr_write.call_count, 2)
    first_call_args = ''.join(mock_stderr_write.call_args_list[0][0])
    self.assertEqual(
        first_call_args,
        'FATAL Flags parsing error: Missing value for flag --commission\n',
    )
    second_call_args = ''.join(mock_stderr_write.call_args_list[1][0])
    self.assertEqual(
        second_call_args,
        'Pass --helpshort or --helpfull to see help on flags.\n',
    )
    self.mock_android_device.mbs.commissionDevice.assert_not_called()
    mock_exit.assert_called()

  @flagsaver.flagsaver((ui_automator._DECOMMISSION, 'm5stack'))
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  @mock.patch.object(sys, 'exit', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'decommission_device', autospec=True
  )
  def test_run_calls_decommission_device_with_valid_arguments(
      self, mock_decommission_device, mock_exit, mock_commission_device
  ):
    with mock.patch.object(sys, 'argv', _FAKE_VALID_SYS_ARGV_FOR_DECOMMISSION):
      ui_automator.run()

    mock_commission_device.assert_not_called()
    mock_decommission_device.assert_called_once_with(mock.ANY, 'm5stack')
    mock_exit.assert_called_once()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_decommission_device_raises_an_error_with_invalid_device_name(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    expected_error_message = (
        'Value of DeviceName is invalid. Device name should be no more than 24'
        ' characters.'
    )
    with self.assertRaisesRegex(ValueError, expected_error_message):
      self.ui_automator.decommission_device('device_name_longer_than_24_chars')

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_decommission_device_fails_when_snippet_method_throws_an_error(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    expected_error_message = (
        f'Unable to remove {_FAKE_MATTER_DEVICE_NAME} from GHA'
        f' on device({self.mock_android_device.device_info["serial"]}).'
    )
    self.mock_android_device.mbs.removeDevice.side_effect = Exception(
        'Can not remove the device.'
    )

    with self.assertRaises(errors.MoblySnippetError) as exc:
      self.ui_automator.decommission_device(_FAKE_MATTER_DEVICE_NAME)

    self.assertIn(expected_error_message, str(exc.exception))

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_decommission_device_successfully_removes_a_device(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]

    with self.assertLogs() as cm:
      self.ui_automator.decommission_device(_FAKE_MATTER_DEVICE_NAME)

    self.mock_android_device.mbs.removeDevice.assert_called_once_with(
        _FAKE_MATTER_DEVICE_NAME
    )
    self.assertEqual(
        cm.output[2], 'INFO:root:Successfully remove the device on GHA.'
    )

  @flagsaver.flagsaver((ui_automator._RUN_REGRESSION_TESTS, True))
  @flagsaver.flagsaver((ui_automator._REPEAT, 5))
  @flagsaver.flagsaver(
      (ui_automator._COMMISSION, ['m5stack', '34970112332', 'Office'])
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'run_regression_tests', autospec=True
  )
  @mock.patch.object(sys, 'exit', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  def test_run_calls_run_regression_tests_with_valid_arguments(
      self, mock_commission_device, mock_exit, mock_run_regression_tests
  ):
    with mock.patch.object(
        sys, 'argv', _FAKE_VALID_SYS_ARGV_FOR_REGRESSION_TESTS
    ):
      ui_automator.run()

    mock_run_regression_tests.assert_called_once_with(
        mock.ANY,
        3,
        ui_automator.RegTestSuiteType.COMMISSION,
        device_name='m5stack',
        pairing_code='34970112332',
        gha_room='Office',
    )
    mock_commission_device.assert_not_called()
    mock_exit.assert_called_once()

  @flagsaver.flagsaver((ui_automator._RUN_REGRESSION_TESTS, True))
  @flagsaver.flagsaver((ui_automator._REPEAT, 5))
  @mock.patch.object(
      ui_automator.UIAutomator, 'run_regression_tests', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  def test_run_regression_tests_with_invalid_args_should_raise_an_error(
      self, mock_commission_device, mock_run_regression_tests
  ):
    with mock.patch.object(
        sys, 'argv', _FAKE_INVALID_SYS_ARGV_FOR_REGRESSION_TESTS
    ):
      with self.assertRaisesRegex(
          flags.IllegalFlagValueError,
          (
              'Use --regtest to run regression tests infinitely. Add --repeat'
              ' <repeat-times> to stop after repeat-times. `--regtest` must be'
              ' used with `--commission`.'
          ),
      ):
        ui_automator.run()

    mock_commission_device.assert_not_called()
    mock_run_regression_tests.assert_not_called()

  @mock.patch.object(time, 'sleep', autospec=True)
  @mock.patch('builtins.open', autospec=True)
  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'decommission_device', autospec=True
  )
  def test_run_regression_tests_should_be_conducted_for_the_designated_number_of_cycles(
      self,
      mock_decommission_device,
      mock_commission_device,
      mock_get_all_instances,
      mock_open,
      mock_sleep,
  ):
    mock_sleep.return_value = None
    mock_get_all_instances.return_value = [self.mock_android_device]

    with self.assertLogs() as cm:
      self.ui_automator.run_regression_tests(
          5,
          ui_automator.RegTestSuiteType.COMMISSION,
          device_name='m5stack',
          pairing_code='34970112332',
          gha_room='Office',
      )

    self.assertEqual(mock_commission_device.call_count, 5)
    self.assertEqual(mock_decommission_device.call_count, 5)
    self.assertEqual(
        cm.output[0], 'INFO:root:Start running regression tests 5 times.'
    )
    self.assertEqual(mock_open.call_count, 2)

  @mock.patch.object(time, 'sleep', autospec=True)
  @mock.patch('builtins.open', autospec=True)
  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'decommission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'is_device_exist', autospec=True
  )
  def test_run_regression_tests_executes_for_given_number_of_times_with_failure(
      self,
      mock_is_device_exist,
      mock_decommission_device,
      mock_commission_device,
      mock_get_all_instances,
      mock_open,
      mock_sleep,
  ):
    mock_sleep.return_value = None
    mock_commission_device.side_effect = [
        None,
        None,
        errors.MoblySnippetError('fake_error'),
        None,
        None,
    ]
    mock_is_device_exist.side_effect = [True, True, False, True, True]
    mock_get_all_instances.return_value = [self.mock_android_device]

    with self.assertLogs() as cm:
      self.ui_automator.run_regression_tests(
          5,
          ui_automator.RegTestSuiteType.COMMISSION,
          device_name='m5stack',
          pairing_code='34970112332',
          gha_room='Office',
      )

    self.assertEqual(mock_commission_device.call_count, 5)
    self.assertEqual(mock_is_device_exist.call_count, 5)
    self.assertEqual(mock_decommission_device.call_count, 4)
    self.assertEqual(
        cm.output[0], 'INFO:root:Start running regression tests 5 times.'
    )
    self.assertEqual(mock_open.call_count, 2)

  def test_run_regression_tests_raises_an_error_with_invalid_input(self):
    with self.assertRaisesRegex(
        ValueError, 'Number placed after `--repeat` must be positive.'
    ):
      self.ui_automator.run_regression_tests(
          -5,
          ui_automator.RegTestSuiteType.COMMISSION,
          device_name='m5stack',
          pairing_code='34970112332',
          gha_room='Office',
      )

  @mock.patch.object(time, 'sleep', autospec=True)
  @mock.patch('builtins.open', autospec=True)
  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'decommission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'is_device_exist', autospec=True
  )
  def test_run_regression_tests_runs_continuously_until_keyboard_interrupts(
      self,
      mock_is_device_exist,
      mock_decommission_device,
      mock_commission_device,
      mock_get_all_instances,
      mock_open,
      mock_sleep,
  ):
    mock_sleep.return_value = None
    mock_commission_device.side_effect = [
        None,
        errors.MoblySnippetError('fake_error'),
        None,
        errors.MoblySnippetError('fake_error'),
        None,
        KeyboardInterrupt(),
    ]
    mock_is_device_exist.side_effect = [True, False, True, False, True]
    mock_get_all_instances.return_value = [self.mock_android_device]

    with self.assertLogs() as cm:
      self.ui_automator.run_regression_tests(
          None,
          ui_automator.RegTestSuiteType.COMMISSION,
          device_name='m5stack',
          pairing_code='34970112332',
          gha_room='Office',
      )

    self.assertEqual(mock_commission_device.call_count, 6)
    self.assertEqual(mock_decommission_device.call_count, 3)
    self.assertEqual(mock_is_device_exist.call_count, 5)
    self.assertEqual(
        cm.output[0], 'INFO:root:Start running regression tests continuously.'
    )
    self.assertEqual(mock_open.call_count, 2)

  @flagsaver.flagsaver(
      (ui_automator._COMMISSION, ['m5stack', '34970112332', 'Office'])
  )
  @mock.patch.object(sys, 'exit', autospec=True)
  @mock.patch.object(time, 'time', autospec=True)
  @mock.patch.object(time, 'sleep', autospec=True)
  @mock.patch('builtins.open', autospec=True)
  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'decommission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'is_device_exist', autospec=True
  )
  def test_run_calls_run_regression_tests_and_produces_summary_in_txt(
      self,
      mock_is_device_exist,
      mock_decommission_device,
      mock_commission_device,
      mock_get_all_instances,
      mock_open,
      mock_sleep,
      mock_time,
      mock_exit,
  ):
    txt_stream = io.StringIO()
    mock_sleep.return_value = None
    fake_error = errors.MoblySnippetError('error')
    mock_commission_device.side_effect = [
        fake_error,
        None,
        None,
    ]
    mock_decommission_device.side_effect = [
        None,
        fake_error,
    ]
    mock_is_device_exist.side_effect = [False, True, True]
    mock_get_all_instances.return_value = [self.mock_android_device]
    mock_open.side_effect = [io.StringIO(), txt_stream]
    # mock_time called by startTestRun, startTest, stopTest, and stopTestRun.
    # startTest and stopTest will be called when running test cases.
    # There are 3 test_commission and 3 test_decommission in this test suite.
    # So 6 test cases will call mock_time for 12 times.
    mock_time.side_effect = [0] + list(range(12)) + [11]
    expected_summary = unit_test_utils.make_summary(
        test_date=time.strftime('%Y/%m/%d', time.localtime(0)),
        duration=test_reporter.duration_formatter(11),
        total_runs=3,
        total_successful_runs=1,
    )
    expected_test_case_result = unit_test_utils.make_test_case_result(
        3,
        res_of_test_commission=['FAIL', 'PASS', 'PASS'],
        res_of_test_decommission=['N/A', 'PASS', 'FAIL'],
    )
    err = (errors.MoblySnippetError, fake_error, fake_error.__traceback__)
    fake_err_msg = ''.join(traceback.format_exception(*err))

    with mock.patch.object(txt_stream, 'close'):
      with mock.patch.object(
          test_reporter.TestResult,
          '_exc_info_to_string',
          return_value=fake_err_msg,
      ):
        with mock.patch.object(
            sys, 'argv', _FAKE_VALID_SYS_ARGV_FOR_REGRESSION_TESTS
        ):
          ui_automator.run()

    self.assertEqual(mock_commission_device.call_count, 3)
    self.assertEqual(mock_is_device_exist.call_count, 3)
    self.assertEqual(mock_decommission_device.call_count, 2)
    self.assertEqual(
        expected_summary + '\n\n' + expected_test_case_result,
        txt_stream.getvalue(),
    )
    mock_exit.assert_called_once()

  @flagsaver.flagsaver(
      (ui_automator._COMMISSION, ['m5stack', '34970112332', 'Office'])
  )
  @mock.patch.object(sys, 'exit', autospec=True)
  @mock.patch.object(time, 'time', autospec=True)
  @mock.patch.object(time, 'sleep', autospec=True)
  @mock.patch('builtins.open', autospec=True)
  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(
      ui_automator.UIAutomator, 'commission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'decommission_device', autospec=True
  )
  @mock.patch.object(
      ui_automator.UIAutomator, 'is_device_exist', autospec=True
  )
  def test_run_calls_run_regression_tests_and_produces_summary_in_xml(
      self,
      mock_is_device_exist,
      mock_decommission_device,
      mock_commission_device,
      mock_get_all_instances,
      mock_open,
      mock_sleep,
      mock_time,
      mock_exit,
  ):
    xml_stream = io.StringIO()
    mock_sleep.return_value = None
    fake_error = errors.MoblySnippetError('error')
    mock_commission_device.side_effect = [
        fake_error,
        None,
        None,
    ]
    mock_is_device_exist.side_effect = [False, True, True]
    mock_decommission_device.side_effect = [
        None,
        fake_error,
    ]
    mock_get_all_instances.return_value = [self.mock_android_device]
    mock_open.side_effect = [xml_stream, io.StringIO()]
    # mock_time called by startTestRun, startTest, stopTest, and stopTestRun.
    # startTest and stopTest will be called when running test cases.
    # There are 3 test_commission and 3 test_decommission in this test suite.
    # So 6 test cases will call mock_time for 12 times.
    mock_time.side_effect = [0] + list(range(12)) + [11]
    expected_test_suite_re = unit_test_utils.OUTPUT_STRING % {
        'suite_name': 'CommissionRegTest',
        'tests': 6,
        'failures': 0,
        'errors': 2,
        'run_time': 11,
        'start_time': re.escape(unit_test_utils.iso_timestamp(0)),
    }
    err = (errors.MoblySnippetError, fake_error, fake_error.__traceback__)
    fake_err_msg = ''.join(traceback.format_exception(*err))
    expected_testcase1_re = unit_test_utils.TESTCASE_STRING_WITH_ERRORS % {
        'run_time': 1,
        'start_time': re.escape(unit_test_utils.iso_timestamp(0)),
        'test_name': 'test_commission',
        'class_name': 'google3.java.com.google.assistant.verticals.homeautomation.partners.ui_automator.commission_reg_test.CommissionRegTest',
        'status': 'run',
        'result': 'FAIL',
        'message': xml_reporter._escape_xml_attr(str(err[1])),
        'error_type': xml_reporter._escape_xml_attr(str(err[0])),
        'error_msg': xml_reporter._escape_cdata(fake_err_msg),
    }
    expected_testcase2_re = unit_test_utils.TESTCASE_STRING_WITH_PROPERTIES % {
        'run_time': 1,
        'start_time': re.escape(unit_test_utils.iso_timestamp(2)),
        'test_name': 'test_decommission',
        'class_name': 'google3.java.com.google.assistant.verticals.homeautomation.partners.ui_automator.commission_reg_test.CommissionRegTest',
        'status': 'notrun',
        'result': 'N/A',
        'properties': (
            '      <property name="skip_reason" value="%s"></property>'
            % (xml_reporter._escape_xml_attr('Device was not commissioned.'),)
        ),
        'message': '',
    }
    expected_testcase3_re = unit_test_utils.TESTCASE_STRING % {
        'run_time': 1,
        'start_time': re.escape(unit_test_utils.iso_timestamp(4)),
        'test_name': 'test_commission',
        'class_name': 'google3.java.com.google.assistant.verticals.homeautomation.partners.ui_automator.commission_reg_test.CommissionRegTest',
        'status': 'run',
        'result': 'PASS',
    }
    expected_testcase4_re = unit_test_utils.TESTCASE_STRING % {
        'run_time': 1,
        'start_time': re.escape(unit_test_utils.iso_timestamp(6)),
        'test_name': 'test_decommission',
        'class_name': 'google3.java.com.google.assistant.verticals.homeautomation.partners.ui_automator.commission_reg_test.CommissionRegTest',
        'status': 'run',
        'result': 'PASS',
    }
    expected_testcase5_re = unit_test_utils.TESTCASE_STRING % {
        'run_time': 1,
        'start_time': re.escape(unit_test_utils.iso_timestamp(8)),
        'test_name': 'test_commission',
        'class_name': 'google3.java.com.google.assistant.verticals.homeautomation.partners.ui_automator.commission_reg_test.CommissionRegTest',
        'status': 'run',
        'result': 'PASS',
    }
    expected_testcase6_re = unit_test_utils.TESTCASE_STRING_WITH_ERRORS % {
        'run_time': 1,
        'start_time': re.escape(unit_test_utils.iso_timestamp(10)),
        'test_name': 'test_decommission',
        'class_name': 'google3.java.com.google.assistant.verticals.homeautomation.partners.ui_automator.commission_reg_test.CommissionRegTest',
        'status': 'run',
        'result': 'FAIL',
        'message': xml_reporter._escape_xml_attr(str(err[1])),
        'error_type': xml_reporter._escape_xml_attr(str(err[0])),
        'error_msg': xml_reporter._escape_cdata(fake_err_msg),
    }

    with mock.patch.object(
        test_reporter.TestResult,
        '_exc_info_to_string',
        return_value=fake_err_msg,
    ):
      with mock.patch.object(
          sys, 'argv', _FAKE_VALID_SYS_ARGV_FOR_REGRESSION_TESTS
      ):
        ui_automator.run()

    self.assertEqual(mock_commission_device.call_count, 3)
    self.assertEqual(mock_is_device_exist.call_count, 3)
    self.assertEqual(mock_decommission_device.call_count, 2)
    (testcases,) = re.search(
        expected_test_suite_re, xml_stream.getvalue()
    ).groups()
    [testcase1, testcase2, testcase3, testcase4, testcase5, testcase6] = (
        testcases.split('\n  </testcase>\n')
    )
    self.assertRegex(testcase1, expected_testcase1_re)
    self.assertRegex(testcase2, expected_testcase2_re)
    self.assertRegex(testcase3, expected_testcase3_re)
    self.assertRegex(testcase4, expected_testcase4_re)
    self.assertRegex(testcase5, expected_testcase5_re)
    self.assertRegex(testcase6, expected_testcase6_re)
    mock_exit.assert_called_once()

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_includes_apk_versions_with_device_connected(
      self,
      mock_load_snippet,
      mock_get_all_instances,
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.mock_android_device.adb.shell.side_effect = [
        b'versionName=0.0.0\n',
        b'versionName=0.0.1\n',
    ]

    report_info = self.ui_automator.get_report_info()

    mock_load_snippet.assert_called_once()
    self.assertDictEqual(
        report_info, {'gha_version': '0.0.0', 'gms_core_version': '0.0.1'}
    )

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_get_report_info_raises_an_error_when_no_device_connected(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = []

    with self.assertRaisesRegex(
        errors.AndroidDeviceNotReadyError, 'get_report_info failed.'
    ):
      self.ui_automator.get_report_info()

  @mock.patch.object(time, 'sleep', autospec=True)
  @mock.patch('builtins.open', autospec=True)
  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'get_report_info', autospec=True)
  def test_run_regression_tests_should_insert_report_info_into_summary(
      self,
      mock_get_report_info,
      mock_get_all_instances,
      mock_open,
      mock_sleep,
  ):
    mock_sleep.return_value = None
    fake_report_info: test_reporter.ReportInfo = {
        'gha_version': '0.0.0',
        'gms_core_version': '0.0.1',
        'hub_version': '10.1.3',
        'dut': 'm5stack',
        'device_firmware': '10.20.12',
    }
    mock_get_report_info.return_value = fake_report_info
    mock_get_all_instances.return_value = [self.mock_android_device]

    with mock.patch.object(
        test_reporter.TestResult, 'write_summary_in_txt', autospec=True
    ) as mock_write_summary_in_txt:
      self.ui_automator.run_regression_tests(
          3,
          ui_automator.RegTestSuiteType.COMMISSION,
          device_name='m5stack',
          pairing_code='34970112332',
          gha_room='Office',
      )

    self.assertEqual(
        mock_write_summary_in_txt.call_args.kwargs.get('report_info'),
        fake_report_info,
    )
    mock_open.assert_called_once()

  @flagsaver.flagsaver((ui_automator._DUT, ['model', 'type', 'protocol']))
  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_includes_dut_value_from_flag_input(
      self, mock_load_snippet, mock_load_device
  ):
    report_info = self.ui_automator.get_report_info()

    mock_load_device.assert_called_once()
    mock_load_snippet.assert_called_once()
    self.assertDictEqual(report_info, {'dut': '<model, type, protocol>'})

  @flagsaver.flagsaver((ui_automator._DUT, None))
  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_returns_empty_dict_without_dut_flag_input(
      self, mock_load_snippet, mock_load_device
  ):
    report_info = self.ui_automator.get_report_info()

    mock_load_device.assert_called_once()
    mock_load_snippet.assert_called_once()
    self.assertDictEqual(report_info, {})

  @flagsaver.flagsaver((ui_automator._HUB, '10.1.3'))
  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_includes_hub_value_from_flag_input(
      self, mock_load_snippet, mock_load_device
  ):
    report_info = self.ui_automator.get_report_info()

    mock_load_device.assert_called_once()
    mock_load_snippet.assert_called_once()
    self.assertDictEqual(report_info, {'hub_version': '10.1.3'})

  @flagsaver.flagsaver((ui_automator._HUB, None))
  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_returns_empty_dict_without_hub_flag_input(
      self, mock_load_snippet, mock_load_device
  ):
    report_info = self.ui_automator.get_report_info()

    mock_load_device.assert_called_once()
    mock_load_snippet.assert_called_once()
    self.assertDictEqual(report_info, {})

  @flagsaver.flagsaver((ui_automator._DEVICE_FIRMWARE, '10.20.12'))
  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_includes_device_firmware_from_flag_input(
      self, mock_load_snippet, mock_load_device
  ):
    report_info = self.ui_automator.get_report_info()

    mock_load_device.assert_called_once()
    mock_load_snippet.assert_called_once()
    self.assertDictEqual(report_info, {'device_firmware': '10.20.12'})

  @flagsaver.flagsaver((ui_automator._DEVICE_FIRMWARE, None))
  @mock.patch.object(ui_automator.UIAutomator, 'load_device', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_returns_empty_dict_without_device_firmware_flag(
      self, mock_load_snippet, mock_load_device
  ):
    report_info = self.ui_automator.get_report_info()

    mock_load_device.assert_called_once()
    mock_load_snippet.assert_called_once()
    self.assertDictEqual(report_info, {})

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  @mock.patch.object(ui_automator.UIAutomator, 'load_snippet', autospec=True)
  def test_get_report_info_should_not_write_none_in_report_info(
      self,
      mock_load_snippet,
      mock_get_all_instances,
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.mock_android_device.adb.shell.side_effect = [
        # Response for getting gha version.
        b'Unable to find package\n',
        # Response for getting gms core version.
        b'Unable to find package\n',
    ]

    report_info = self.ui_automator.get_report_info()

    mock_load_snippet.assert_called_once()
    self.assertDictEqual(report_info, {})

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_is_device_exist_returns_true_when_device_exists(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.mock_android_device.mbs.isDeviceExist.return_value = True

    self.assertTrue(
        self.ui_automator.is_device_exist(_FAKE_MATTER_DEVICE_NAME)
    )

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_is_device_exist_returns_false_when_device_does_not_exist(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.mock_android_device.mbs.isDeviceExist.return_value = False

    self.assertFalse(
        self.ui_automator.is_device_exist(_FAKE_MATTER_DEVICE_NAME)
    )

  @mock.patch.object(android_device, 'get_all_instances', autospec=True)
  def test_is_device_exist_throws_an_error_when_snippet_method_throws_an_error(
      self, mock_get_all_instances
  ):
    mock_get_all_instances.return_value = [self.mock_android_device]
    self.mock_android_device.mbs.isDeviceExist.side_effect = Exception(
        'fake-error'
    )

    with self.assertRaises(errors.MoblySnippetError) as exc:
      self.ui_automator.is_device_exist(_FAKE_MATTER_DEVICE_NAME)

    expected_error_message = (
        f'Unable to check if {_FAKE_MATTER_DEVICE_NAME} exists on GHA'
        f' on device({self.mock_android_device.device_info["serial"]}).'
    )
    self.assertEqual(expected_error_message, str(exc.exception))


if __name__ == '__main__':
  unittest.main()
