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

"""UI Automator controller in python layer.

A python controller that can trigger mobly UI automator snippet to achieve some
automated UI operations on Android phones.
"""
import collections
from concurrent import futures
import enum
import functools
import logging
import os
import re
import time
from typing import Any, Callable
import unittest

from absl import app
from absl import flags
import inflection
from mobly.controllers import android_device
from mobly.controllers.android_device_lib import adb
from mobly.snippet import errors as snippet_errors

from ui_automator import android_device as ad
from ui_automator import commission_reg_test
from ui_automator import errors
from ui_automator import test_reporter
from ui_automator import version


_GOOGLE_HOME_APP = {
    'id': 'gha',
    'name': 'Google Home Application (GHA)',
    'minVersion': '3.1.18.1',
    'minMatter': '231456000',
    'minThread': '231456000',
}
_MOBLY_SNIPPET_APK: str = 'com.chip.interop.moblysnippet'
_MOBLY_SNIPPET_APK_NAME: str = 'mbs'
_REGRESSION_TESTS_TIMEOUT_IN_SECS = 1
_COMMISSION_FLAG_USAGE_GUIDE = (
    'Use --commission {DeviceName},{PairingCode},{GHARoom} to commission a'
    ' device to google fabric on GHA.'
)
_REGRESSION_TESTS_FLAG_USAGE_GUIDE = (
    'Use --regtest to run regression tests infinitely. Add --repeat'
    ' <repeat-times> to stop after repeat-times. `--regtest` must be'
    ' used with `--commission`.'
)
_COMMISSION = flags.DEFINE_list(
    name='commission',
    default=None,
    help=_COMMISSION_FLAG_USAGE_GUIDE,
)
_DECOMMISSION = flags.DEFINE_string(
    name='decommission',
    default='',
    help='Use --decommission {DeviceName} to remove the device on GHA.',
)
_RUN_REGRESSION_TESTS = flags.DEFINE_boolean(
    name='regtest',
    default=False,
    help=_REGRESSION_TESTS_FLAG_USAGE_GUIDE,
)
_REPEAT = flags.DEFINE_integer(
    name='repeat',
    default=None,
    help=_REGRESSION_TESTS_FLAG_USAGE_GUIDE,
)
_DUT = flags.DEFINE_list(
    name='dut',
    default=None,
    help=(
        'Use --dut {model},{type},{protocol} to include this field in'
        ' test report. e.g. `--dut X123123123,LIGHT,Matter`.'
    ),
)
_HUB_VERSION_KEY = 'hub_version'
_HUB = flags.DEFINE_string(
    name='hub',
    default=None,
    help=(
        'Use --hub {HubVersion} to include this field in'
        ' regression test report. e.g. `--hub 10.1.3`.'
    ),
)
_DEVICE_FIRMWARE_KEY = 'device_firmware'
_DEVICE_FIRMWARE = flags.DEFINE_string(
    name='fw',
    default=None,
    help=(
        'Use --fw {DeviceFirmware} to include this field in regression test'
        ' report. e.g. `--fw 10.20.12`.'
    ),
)


class RegTestSuiteType(enum.Enum):
  COMMISSION = 'Commission'


def _validate_commission_arg(
    device_name: str, pairing_code: str, gha_room: str
) -> None:
  """Returns None if arguments passed in `commission` are valid.

  Args:
      device_name: Display name of commissioned device on GHA.
      pairing_code: An 11-digit or 21-digit numeric code which contains the
        information needed to commission a matter device.
      gha_room: Assigned room of commissioned device on GHA.

  Raises:
      ValueError: When any of passed arguments is invalid.
  """
  device_name_match = re.fullmatch(r'\S{1,24}', device_name)
  pairing_code_match = re.fullmatch(r'^(\d{11}|\d{21})$', pairing_code)
  gha_room_match = re.fullmatch(
      r'Attic|Back door|Backyard|Basement|Bathroom|Bedroom|Den|Dining'
      r' Room|Entryway|Family Room|Front door|Front'
      r' Yard|Garage|Hallway|Kitchen|Living Room|Master'
      r' Bedroom|Office|Shed|Side door',
      gha_room,
  )

  if not device_name_match:
    raise ValueError(
        'Value of DeviceName is invalid. Device name should be no more than 24'
        ' characters.'
    )
  if not pairing_code_match:
    raise ValueError(
        'Value of PairingCode is invalid. Paring code should be 11-digit or'
        ' 21-digit numeric code.'
    )
  if not gha_room_match:
    raise ValueError(
        'Value of GHARoom is invalid. Valid values for GHARoom: Attic|Back'
        ' door|Backyard|Basement|Bathroom|Bedroom|Den|Dining'
        ' Room|Entryway|Family Room|Front door|Front'
        ' Yard|Garage|Hallway|Kitchen|Living Room|Master'
        ' Bedroom|Office|Shed|Side door'
    )


def get_android_device_ready(func: Callable[..., Any]) -> Callable[..., Any]:
  """A decorator to check if an Android device can be controlled by installed apk.

  Args:
      func: The function to be wrapped.

  Returns:
      The wrapped function.

  Raises:
      NoAndroidDeviceError: When no device is connected.
      AndroidDeviceNotReadyError: When required snippet apk can not be loaded
      on device.
  """

  @functools.wraps(func)
  def wrapped_func(self, *args, **kwargs):
    try:
      self.load_device()
      self.load_snippet()
      return func(self, *args, **kwargs)
    except (
        errors.AdbError,
        errors.AndroidDeviceNotReadyError,
        errors.NoAndroidDeviceError,
    ) as e:
      raise errors.AndroidDeviceNotReadyError(f'{func.__name__} failed.') from e
    finally:
      self.unload_snippet()

  return wrapped_func


class UIAutomator:
  """UI Automator controller in python layer."""

  def __init__(self, logger: logging.Logger = logging.getLogger()):
    """Inits UIAutomator.

    Interacts with android device by pre-installed apk. Can perform
    methods provided by a snippet installed on the android device.

    Args:
        logger: Injected logger, if None, specify the default(root) one.
    """
    self._logger = logger
    self._is_reg_test_finished = False
    self._connected_device: android_device.AndroidDevice | None = None

  def load_device(self):
    """Selects the first connected android device.

    Raises:
        NoAndroidDeviceError: When no device is connected.
    """
    try:
      android_devices = android_device.get_all_instances()
    except adb.AdbError as exc:
      raise errors.AdbError(
          'Please install adb and add it to your PATH environment variable.'
      ) from exc

    if not android_devices:
      raise errors.NoAndroidDeviceError(
          'No Android device connected to the host computer.'
      )
    self._connected_device = android_devices[0]
    self._logger.info(f'connected device: [{self._connected_device}]')

  def load_snippet(self):
    """Loads needed mobly snippet installed on android device.

    Raises:
        NoAndroidDeviceError: When no device is connected.
        AndroidDeviceNotReadyError: When required snippet apk can not be loaded
        on device.
    """
    if not self._connected_device:
      raise errors.NoAndroidDeviceError(
          'No Android device connected to the host computer.'
      )

    is_apk_installed = ad.is_apk_installed(
        self._connected_device, _MOBLY_SNIPPET_APK
    )
    if not is_apk_installed or not ad.is_apk_version_correct(
        self._connected_device,
        _MOBLY_SNIPPET_APK,
        version.VERSION,
    ):
      if is_apk_installed:
        ad.uninstall_apk(self._connected_device, _MOBLY_SNIPPET_APK)
      ad.install_apk(self._connected_device, self._get_mbs_apk_path())

    try:
      self._connected_device.load_snippet(
          _MOBLY_SNIPPET_APK_NAME, _MOBLY_SNIPPET_APK
      )
    except snippet_errors.ServerStartPreCheckError as exc:
      # Raises when apk not be installed or instrumented on device.
      raise errors.AndroidDeviceNotReadyError(
          f"Check device({self._connected_device.device_info['serial']}) has"
          ' installed required apk.'
      ) from exc
    except (
        snippet_errors.ServerStartError,
        snippet_errors.ProtocolError,
    ) as exc:
      raise errors.AndroidDeviceNotReadyError(
          f"Check device({self._connected_device.device_info['serial']}) can"
          ' load required apk.'
      ) from exc
    except android_device.SnippetError as e:
      # Error raises when registering a package twice or a package with
      # duplicated name. Thus, It is okay to pass here as long as the snippet
      # has been loaded.
      self._logger.debug(str(e))

  def unload_snippet(self) -> None:
    """Unloads loaded mobly snippet on connected android device."""
    if not self._connected_device:
      return

    self._connected_device.unload_snippet(_MOBLY_SNIPPET_APK_NAME)

  @get_android_device_ready
  def commission_device(
      self, device_name: str, pairing_code: str, gha_room: str
  ) -> None:
    """Commissions a device through installed apk `mbs` on Google Home App.

    Args:
        device_name: Display name of commissioned device on GHA.
        pairing_code: An 11-digit or 21-digit numeric code which contains the
          information needed to commission a matter device.
        gha_room: Assigned room of commissioned device on GHA.

    Raises:
        ValueError: When any of passed arguments is invalid.
        MoblySnippetError: When running `commissionDevice` method in snippet apk
        encountered an error.
    """
    self._logger.info('Start commissioning the device.')

    _validate_commission_arg(device_name, pairing_code, gha_room)

    device_name_snake_case = f'_{inflection.underscore(device_name)}'
    matter_device = {
        'id': device_name_snake_case,
        'name': device_name,
        'pairingCode': pairing_code,
        'roomName': gha_room,
    }

    try:
      self._connected_device.mbs.commissionDevice(
          _GOOGLE_HOME_APP, matter_device
      )
      self._logger.info('Successfully commission the device on GHA.')
    # TODO(b/298903492): Narrow exception type.
    except Exception as e:
      raise errors.MoblySnippetError(
          'Unable to continue automated commissioning process on'
          f' device({self._connected_device.device_info["serial"]}).'
      ) from e

  @get_android_device_ready
  def decommission_device(self, device_name: str):
    """Removes given device through installed apk `mbs` on Google Home App.

    Args:
        device_name: Display name of the device needs to be removed on GHA.

    Raises:
        ValueError: When passed argument is invalid.
        MoblySnippetError: When running `removeDevice` method in snippet apk
        encountered an error.
    """
    if not re.fullmatch(r'\S{1,24}', device_name):
      raise ValueError(
          'Value of DeviceName is invalid. Device name should be no more than'
          ' 24 characters.'
      )

    self._logger.info('Start removing the device.')
    try:
      self._connected_device.mbs.removeDevice(device_name)
      self._logger.info('Successfully remove the device on GHA.')
    # TODO(b/298903492): Narrow exception type.
    except Exception as e:
      raise errors.MoblySnippetError(
          f'Unable to remove {device_name} from GHA'
          f' on device({self._connected_device.device_info["serial"]}).'
      ) from e

  @get_android_device_ready
  def is_device_exist(self, device_name: str) -> bool:
    """Checks if the device exists on Google Home App.

    Args:
        device_name: Display name of commissioned device on GHA.

    Raises:
        MoblySnippetError: When running `isDeviceExist` method in snippet apk
        encountered an error.

    Returns:
        True if the device exists on GHA.
    """
    try:
      return self._connected_device.mbs.isDeviceExist(device_name)
    except Exception as e:
      raise errors.MoblySnippetError(
          f'Unable to check if {device_name} exists on GHA'
          f' on device({self._connected_device.device_info["serial"]}).'
      ) from e

  def run_regression_tests(
      self,
      repeat: int | None,
      test_type: RegTestSuiteType,
      **kwargs,
  ) -> None:
    """Executes automated regression tests.

    A single execution of both commission and decommission constitutes one
    cycle.

    Args:
        repeat: The value of flag `repeat`. If the value is None, regression
          tests will be run repeatedly until keyboard interrupts.
        test_type: The type of test suite for running regression tests.
        **kwargs: Required args to run regression test cases.

    Raises:
        ValueError: When the value of flag `repeat` is not positive.
    """
    if repeat and repeat <= 0:
      raise ValueError('Number placed after `--repeat` must be positive.')

    self._logger.info(
        'Start running regression tests'
        f' {str(repeat) + " times" if repeat is not None else "continuously"}.'
    )

    self._is_reg_test_finished = False
    suite = unittest.TestSuite()
    # Once all tests are run, `test_reporter.TestRunner` will produce an XML
    # file and a text summary file. If regression test cycles are not predefined
    # (i.e., `repeat` is not specified), test cases should be dynamically added
    # to the running suite on the fly.
    executor = futures.ThreadPoolExecutor(max_workers=1)
    if test_type == RegTestSuiteType.COMMISSION:
      device_name = kwargs.get('device_name', None)
      pairing_code = kwargs.get('pairing_code', None)
      gha_room = kwargs.get('gha_room', None)
      executor.submit(
          self._add_test_to_commission_test_suite,
          suite=suite,
          repeat=repeat,
          device_name=device_name,
          pairing_code=pairing_code,
          gha_room=gha_room,
      )

    runner = test_reporter.TestRunner(logger=self._logger)
    try:
      runner.run(suite=suite, report_info=self.get_report_info())
    finally:
      self._is_reg_test_finished = True
      executor.shutdown(wait=False)

  @get_android_device_ready
  def get_report_info(self) -> test_reporter.ReportInfo:
    """Gets report info for regression tests.

    Returns:
        report_info: Versions and device info displayed in generated txt report.
        Versions includes GHA, GMSCore, hub and device firmware. Device info is
        in <model, type, protocol> format, e.g. <X123123, LIGHT, Matter>.
    """
    temp_info = collections.defaultdict()
    if self._connected_device:
      gha_version = ad.get_apk_version(
          self._connected_device, 'com.google.android.apps.chromecast.app'
      )
      if gha_version:
        temp_info['gha_version'] = gha_version
      gms_core_version = ad.get_apk_version(
          self._connected_device, 'com.google.android.gms'
      )
      if gms_core_version:
        temp_info['gms_core_version'] = gms_core_version

    if _DUT.value:
      temp_info['dut'] = f"<{', '.join(_DUT.value)}>"

    if _HUB.value:
      temp_info[_HUB_VERSION_KEY] = _HUB.value

    if _DEVICE_FIRMWARE.value:
      temp_info[_DEVICE_FIRMWARE_KEY] = _DEVICE_FIRMWARE.value

    report_info: test_reporter.ReportInfo = {**temp_info}

    return report_info

  def _get_mbs_apk_path(self) -> str:
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'android',
        'app',
        'snippet.apk',
    )

  def _add_test_to_commission_test_suite(
      self,
      suite: unittest.TestSuite,
      repeat: int | None,
      device_name: str,
      pairing_code: str,
      gha_room: str,
  ) -> None:
    """Adds automated regression tests for RegTestSuiteType.COMMISSION.

    Args:
        suite: TestSuite instance that tests added to.
        repeat: An integer value specifies the number of times the regression
          tests should be executed. Or None if tests should be run infinitely.
        device_name: Display name of commissioned device on GHA.
        pairing_code: An 11-digit or 21-digit numeric code which contains the
          information needed to commission a matter device.
        gha_room: Assigned room of commissioned device on GHA.
    """
    run_count = 0
    while not self._is_reg_test_finished and (not repeat or run_count < repeat):
      suite.addTest(
          commission_reg_test.CommissionRegTest(
              self,
              'test_commission',
              device_name=device_name,
              pairing_code=pairing_code,
              gha_room=gha_room,
          )
      )
      suite.addTest(
          commission_reg_test.CommissionRegTest(
              self, 'test_decommission', device_name=device_name
          )
      )
      time.sleep(_REGRESSION_TESTS_TIMEOUT_IN_SECS)
      run_count += 1

  def process_flags(self) -> None:
    """Does specific action based on given flag values."""
    if _COMMISSION.value:
      if len(_COMMISSION.value) != 3:
        raise flags.IllegalFlagValueError(_COMMISSION_FLAG_USAGE_GUIDE)
      device_name, pairing_code, gha_room = _COMMISSION.value
      if _RUN_REGRESSION_TESTS.value:
        self.run_regression_tests(
            _REPEAT.value,
            RegTestSuiteType.COMMISSION,
            device_name=device_name,
            pairing_code=pairing_code,
            gha_room=gha_room,
        )
      else:
        self.commission_device(
            device_name=device_name,
            pairing_code=pairing_code,
            gha_room=gha_room,
        )
    elif _DECOMMISSION.value:
      device_name = _DECOMMISSION.value
      self.decommission_device(device_name)
    elif _RUN_REGRESSION_TESTS.value:
      raise flags.IllegalFlagValueError(_REGRESSION_TESTS_FLAG_USAGE_GUIDE)


# TODO(b/309745485): Type of argv should be Sequence[str].
def _main(argv) -> None:
  if argv and len(argv) > 1:
    raise app.UsageError(f'Too many command-line arguments: {argv!r}')

  UIAutomator().process_flags()


def run():
  app.run(_main)


if __name__ == '__main__':
  run()
