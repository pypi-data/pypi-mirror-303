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

"""Utilities for unit tests."""
import datetime

# Matches the entire XML output. Captures all <testcase> tags except for the
# last closing </testcase> in a single group.
OUTPUT_STRING = r"""<\?xml version="1.0"\?>
<testsuites name="" tests="%(tests)d" failures="%(failures)d" errors="%(errors)d" time="%(run_time).3f" timestamp="%(start_time)s">
<testsuite name="%(suite_name)s" tests="%(tests)d" failures="%(failures)d" errors="%(errors)d" time="%(run_time).3f" timestamp="%(start_time)s">
(  <testcase [.\S\s]*)
  </testcase>
</testsuite>
</testsuites>
"""

# Matches a single <testcase> tag and its contents, without the closing
# </testcase>, which we use as a separator to split multiple <testcase> tags.
TESTCASE_STRING_WITH_PROPERTIES = r"""  <testcase name="%(test_name)s" status="%(status)s" result="%(result)s" time="%(run_time).3f" classname="%(class_name)s" timestamp="%(start_time)s">
    <properties>
%(properties)s
    </properties>%(message)s"""

# Matches a single <testcase> tag and its contents, without the closing
# </testcase>, which we use as a separator to split multiple <testcase> tags.
TESTCASE_STRING_WITH_ERRORS = r"""  <testcase name="%(test_name)s" status="%(status)s" result="%(result)s" time="%(run_time).3f" classname="%(class_name)s" timestamp="%(start_time)s">
  <error message="%(message)s" type="%(error_type)s"><\!\[CDATA\[%(error_msg)s\]\]></error>"""

# Matches a single <testcase> tag and its contents, without the closing
# </testcase>, which we use as a separator to split multiple <testcase> tags.
TESTCASE_STRING = r"""  <testcase name="%(test_name)s" status="%(status)s" result="%(result)s" time="%(run_time).3f" classname="%(class_name)s" timestamp="%(start_time)s">"""


def iso_timestamp(timestamp: float) -> str:
  """Makes timestamp in iso format for unit tests.

  Args:
    timestamp: Time value in float.

  Returns:
    Formatted time according to ISO.
  """
  return datetime.datetime.fromtimestamp(
      timestamp, tz=datetime.timezone.utc
  ).isoformat()


def make_summary(
    test_date: str | None = None,
    duration: str | None = None,
    total_runs: int = 0,
    total_successful_runs: int = 0,
    report_info: dict[str, str] | None = None,
) -> str:
  """Makes test summary produced by `test_reporter` for unit tests.

  Args:
    test_date: Test time for running regression tests.
    duration: The duration for running regression tests.
    total_runs: The number of runs for regression tests.
    total_successful_runs: The number of successful runs for regression tests.
    report_info: Versions and device info displayed in generated txt report.
      Versions includes GHA, GMSCore, hub and device firmware. Device info is in
      <model, type, protocol> format, e.g. <X123123, LIGHT, Matter>.

  Returns:
    Test summary.
  """
  dut = report_info.get('dut', 'n/a') if report_info else 'n/a'
  gha = report_info.get('gha_version', 'n/a') if report_info else 'n/a'
  test_date = test_date or 'n/a'
  duration = duration or 'n/a'
  gms_core = (
      report_info.get('gms_core_version', 'n/a') if report_info else 'n/a'
  )
  hub = report_info.get('hub_version', 'n/a') if report_info else 'n/a'
  device = report_info.get('device_firmware', 'n/a') if report_info else 'n/a'
  success_rate = round(100.0 * float(total_successful_runs) / float(total_runs))
  rows: list[list[str]] = []
  rows.append(['Summary', '', 'Version Info', ''])
  rows.append(['DUT:', dut, 'GHA', gha])
  rows.append(['Test Time:', test_date, 'GMSCore', gms_core])
  rows.append(['Duration:', duration, 'Hub', hub])
  rows.append(['Number of runs:', str(total_runs), 'Device', device])
  rows.append([
      'Success Rate:',
      f'{success_rate}%({total_successful_runs}/{total_runs})',
  ])
  summary = []
  data_indents = (
      max(max(map(len, report_info.values())) + 2, 25) if report_info else 25
  )
  for row in rows:
    for i, element in enumerate(row):
      if i % 2 == 0:
        # Writes header.
        summary.append(element.ljust(25))
      else:
        # Writes data, add 2 extra spaces to separate data and next header.
        summary.append(element.ljust(data_indents))
    summary.append('\n')

  return ''.join(summary)


def make_test_case_result(
    total_runs: int,
    res_of_test_commission: list[str] | None,
    res_of_test_decommission: list[str] | None,
) -> str:
  """Makes test case result produced by `test_reporter` for unit tests.

  Args:
    total_runs: Total cycles for regression tests.
    res_of_test_commission: Elements in list should be `PASS`, `FAIL` or `N/A`,
      which indicates the test result for each test case `test_commission`.
    res_of_test_decommission: Elements in list should be `PASS`, `FAIL` or
      `N/A`, which indicates the test result for each test case
      `test_decommission`.

  Returns:
    Test case result.
  """
  test_case_result = ['Test Case/Test Run'.ljust(25)]
  for i in range(total_runs):
    test_case_result.append(f'#{i + 1}'.ljust(8))
  if res_of_test_commission:
    test_case_result.append('\n')
    test_case_result.append('Commission to GHA'.ljust(25))
    for res in res_of_test_commission:
      test_case_result.append(res.ljust(8))
  if res_of_test_decommission:
    test_case_result.append('\n')
    test_case_result.append('Removing from GHA'.ljust(25))
    for res in res_of_test_decommission:
      test_case_result.append(res.ljust(8))

  return ''.join(test_case_result)
