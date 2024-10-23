# Copyright 2023 Google LLC
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

"""Module for UI Automator related errors.

The error subclasses are intended to make it easier to distinguish between and
handle different types of error exceptions.
"""
DEFAULT_ERROR_CODE = 0


class NoAndroidDeviceError(Exception):
  """Raised when no Android device connected to the host computer."""

  err_code = 1


class AndroidDeviceNotReadyError(Exception):
  """Raised when a Android device is not ready to be controlled."""

  err_code = 2


class AdbError(Exception):
  """Raised when adb command fails."""

  err_code = 3


class MoblySnippetError(Exception):
  """Raised when running a method in loaded snippet throws an error."""

  err_code = 4
