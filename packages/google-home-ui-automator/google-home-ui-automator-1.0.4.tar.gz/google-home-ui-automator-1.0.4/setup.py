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

"""Build the google_home_ui_automator Python package."""
import os

import setuptools

from ui_automator import version

_CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
_README_FILE = 'README.md'
_REQUIREMENTS_FILE = 'requirements.txt'
_SOURCE_CODE_DIR_NAME = 'ui_automator'


def _get_readme() -> str:
  """Returns contents of README.md."""
  readme_file = os.path.join(_CURRENT_DIR, _README_FILE)
  with open(readme_file) as open_file:
    return open_file.read()


def _get_requirements() -> list[str]:
  """Returns package requirements from requirements.txt."""
  requirements_file = os.path.join(_CURRENT_DIR, _REQUIREMENTS_FILE)
  with open(requirements_file) as open_file:
    requirements = open_file.read()
    if requirements:
      return requirements.splitlines()
  raise RuntimeError(
      'Unable to find package requirements in {}'.format(requirements_file)
  )


def _get_version() -> str:
  """Returns version from version.py."""
  return version.VERSION


setuptools.setup(
    name='google-home-ui-automator',
    version=_get_version(),
    description='Google Home UI Automator',
    long_description=_get_readme(),
    long_description_content_type='text/markdown',
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    # project's homepage
    url='https://testsuite-smarthome-matter.googlesource.com/ui-automator/',
    # author details
    author='Google LLC',
    author_email='google-home-testsuite-dev+ui-automator@google.com',
    license='Apache 2.0',
    # define list of packages included in distribution
    packages=setuptools.find_packages(exclude=['ui_automator.tests*']),
    package_dir={'ui_automator': _SOURCE_CODE_DIR_NAME},
    package_data={
        'ui_automator': ['android/**'],
    },
    # runtime dependencies that are installed by pip during install
    install_requires=_get_requirements(),
    entry_points={
        'console_scripts': ['ui-automator = ui_automator.ui_automator:run'],
    },
)
