"""Android device related methods which extend from UI Automator.

Android device class is defined in `mobly.controller`.
"""

from mobly import utils
from mobly.controllers import android_device


def is_apk_installed(
    device: android_device.AndroidDevice, package_name: str
) -> bool:
  """Checks if given package is already installed on the Android device.

  Args:
    device: An AndroidDevice object.
    package_name: The Android app package name.

  Raises:
    adb.AdbError: When executing adb command fails.

  Returns:
    True if package is installed. False otherwise.
  """
  out = device.adb.shell(['pm', 'list', 'package'])
  return bool(utils.grep('^package:%s$' % package_name, out))


def install_apk(device: android_device.AndroidDevice, apk_path: str) -> None:
  """Installs required apk snippet to the given Android device.

  Args:
    device: An AndroidDevice object.
    apk_path: The absolute file path where the apk is located.
  """
  device.adb.install(['-r', '-g', apk_path])


def uninstall_apk(
    device: android_device.AndroidDevice, package_name: str
) -> None:
  """Uninstalls required apk snippet on given Android device.

  Args:
    device: An AndroidDevice object.
    package_name: The Android app package name.
  """
  device.adb.uninstall(package_name)


def is_apk_version_correct(
    device: android_device.AndroidDevice, package_name: str, version: str
) -> bool:
  """Checks if the version of package is given version on the Android device.

  Args:
    device: An AndroidDevice object.
    package_name: The Android app package name.
    version: The specific version of app package.

  Returns:
    True if the version of package matches given version. False otherwise.

  Raises:
    adb.AdbError: When executing adb command fails.
  """
  installed_version = get_apk_version(device, package_name)

  return installed_version == version


def get_apk_version(
    device: android_device.AndroidDevice, package_name: str
) -> str | None:
  """Gets Android app version on given Android device.

  Args:
    device: An AndroidDevice object.
    package_name: The Android app package name.

  Returns:
    The version of given package.

  Raises:
    adb.AdbError: When executing adb command fails.
  """
  grep_version_name = utils.grep(
      'versionName', device.adb.shell(['dumpsys', 'package', package_name])
  )

  return grep_version_name[0].split('=')[1] if grep_version_name else None
