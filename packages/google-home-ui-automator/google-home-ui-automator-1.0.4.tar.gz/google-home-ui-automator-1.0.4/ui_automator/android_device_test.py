"""Unittest of android device extended methods."""

import unittest
from unittest import mock

from mobly.controllers import android_device
from mobly.controllers.android_device_lib import adb

from ui_automator import android_device as ad


class UIAutomatorTest(unittest.TestCase):

  def setUp(self):
    """This method will be run before each of the test methods in the class."""
    super().setUp()
    self.mock_android_device = mock.patch.object(
        android_device, 'AndroidDevice'
    ).start()

  def test_is_apk_installed_returns_true_with_installed_apk(self):
    self.mock_android_device.adb.shell.return_value = (
        b'package:installed.apk\npackage:a.apk\npackage:b.apk\n'
    )

    is_apk_installed = ad.is_apk_installed(
        self.mock_android_device, 'installed.apk'
    )

    self.assertTrue(is_apk_installed)

  def test_is_apk_installed_returns_false_with_not_installed_apk(self):
    self.mock_android_device.adb.shell.return_value = (
        b'package:installed.apk\npackage:a.apk\npackage:b.apk\n'
    )

    is_apk_installed = ad.is_apk_installed(
        self.mock_android_device, 'notinstalled.apk'
    )

    self.assertFalse(is_apk_installed)

  def test_is_apk_installed_raises_an_error(self):
    self.mock_android_device.adb.shell.side_effect = adb.AdbError(
        cmd='adb.shell',
        stderr=b'Run adb command failed.',
        stdout=b'',
        ret_code=1,
    )

    with self.assertRaisesRegex(adb.AdbError, r'Run adb command failed\.'):
      ad.is_apk_installed(self.mock_android_device, 'fake.apk')

  def test_install_apk_installs_apk_with_correct_path(self):
    apk_path = '/path/to/fake.apk'

    ad.install_apk(self.mock_android_device, apk_path)

    self.mock_android_device.adb.install.assert_called_once_with(
        ['-r', '-g', apk_path]
    )

  def test_uninstall_apk_uninstalls_apk_with_given_package_name(self):
    package_to_be_uninstalled = 'notinstalled.apk'

    ad.uninstall_apk(self.mock_android_device, package_to_be_uninstalled)

    self.mock_android_device.adb.uninstall.assert_called_once_with(
        package_to_be_uninstalled
    )

  def test_is_apk_version_correct_returns_true(self):
    self.mock_android_device.adb.shell.return_value = b'versionName=1.2.3\n'

    self.assertTrue(
        ad.is_apk_version_correct(
            self.mock_android_device, 'installed.apk', '1.2.3'
        )
    )

  def test_is_apk_version_correct_returns_false_with_not_installed_apk(self):
    self.mock_android_device.adb.shell.return_value = (
        b'Unable to find package\n'
    )

    self.assertFalse(
        ad.is_apk_version_correct(
            self.mock_android_device, 'notinstalled.apk', '1.2.3'
        )
    )

  def test_is_apk_version_correct_returns_false_with_incorrect_version(self):
    self.mock_android_device.adb.shell.return_value = b'versionName=1.2.4\n'

    self.assertFalse(
        ad.is_apk_version_correct(
            self.mock_android_device, 'installed.apk', '1.2.3'
        )
    )

  def test_get_apk_version_returns_version(self):
    self.mock_android_device.adb.shell.return_value = b'versionName=1.2.4\n'

    self.assertEqual(
        ad.get_apk_version(self.mock_android_device, 'installed.apk'), '1.2.4'
    )

  def test_get_apk_version_returns_none_with_not_installed_apk(self):
    self.mock_android_device.adb.shell.return_value = (
        b'Unable to find package\n'
    )

    self.assertIsNone(
        ad.get_apk_version(self.mock_android_device, 'notinstalled.apk')
    )


if __name__ == '__main__':
  unittest.main()
