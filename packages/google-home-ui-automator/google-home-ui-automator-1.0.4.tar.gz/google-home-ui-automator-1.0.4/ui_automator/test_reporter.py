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

"""A helper to create reports in TXT and XML from running regression tests.

The helper inherits from absl/testing/xml_reporter.py and provides two
additional properties, including producing a xml file even when test is
interrupted and producing a txt file of test summary.
"""

import collections
from collections.abc import Mapping
import io
import logging
import os
import time
from typing import NotRequired, TypedDict
import unittest

from absl.testing import xml_reporter
import immutabledict


_REPORT_TEST_CASE_TITLE_TO_TEST_NAME = immutabledict.immutabledict({
    'Commission to GHA': 'test_commission',
    'Removing from GHA': 'test_decommission',
})
_NA = 'n/a'
_MINIMUM_SUMMARY_COL_INDENTS = 25
_TEST_CASE_TITLE_INDENTS = 25
_TEST_RESULT_INDENTS = 8


def duration_formatter(duration_in_seconds: float) -> str:
  hour_count, remainder = divmod(duration_in_seconds, 3600)
  minute_count, second_count = divmod(remainder, 60)
  return (
      f'{int(hour_count)} hrs, {int(minute_count)} mins,'
      f' {int(second_count)} secs'
  )


class ReportInfo(TypedDict):
  """Type guard for summary of running unit tests."""

  gha_version: NotRequired[str]
  gms_core_version: NotRequired[str]
  hub_version: NotRequired[str]
  device_firmware: NotRequired[str]
  dut: NotRequired[str]


# pylint: disable=protected-access
class _TestCaseResult(xml_reporter._TestCaseResult):
  """Private helper for TestResult."""

  def __init__(self, test):
    super().__init__(test)
    self.status = None
    self.result = None

  def print_xml_summary(self, stream: io.TextIOWrapper):
    """Prints an XML summary of a TestCase.

    Status and result are populated as per JUnit XML test result reporter.
    A test that has been skipped will always have a skip reason,
    as every skip method in Python's unittest requires the reason arg to be
    passed.

    Args:
      stream: output stream to write test report XML to.
    """
    if self.skip_reason is None:
      self.status = 'run'
      self.result = 'PASS' if not self.errors else 'FAIL'
    else:
      self.status = 'notrun'
      self.result = 'N/A'

    test_case_attributes = [
        ('name', self.name),
        ('status', self.status),
        ('result', self.result),
        ('time', f'{self.run_time:.3f}'),
        ('classname', self.full_class_name),
        ('timestamp', xml_reporter._iso8601_timestamp(self.start_time)),
    ]
    xml_reporter._print_xml_element_header(
        'testcase', test_case_attributes, stream, indentation='  '
    )
    self._print_testcase_details(stream)
    if self.skip_reason:
      stream.write('    <properties>\n')
      stream.write(
          '      <property name="%s" value="%s"></property>\n'
          % (
              xml_reporter._escape_xml_attr('skip_reason'),
              xml_reporter._escape_xml_attr(self.skip_reason),
          )
      )
      stream.write('    </properties>\n')
    stream.write('  </testcase>\n')


class _TestSuiteResult(xml_reporter._TestSuiteResult):
  """Private helper for TestResult.

  The `print_xml_summary` function has been overridden to present test cases in
  the XML file in ascending order by their start time. This modification is
  implemented solely at line 168, where the sorting criterion has been changed
  from `t.name` to `t.start_time`. All other lines remain identical to those in
  the original `xml_reporter`.
  """

  def print_xml_summary(self, stream: io.TextIOWrapper):
    """Prints an XML Summary of a TestSuite.

    Args:
      stream: output stream to write test report XML to.
    """
    overall_test_count = sum(len(x) for x in self.suites.values())
    overall_failures = sum(self.failure_counts.values())
    overall_errors = sum(self.error_counts.values())
    overall_attributes = [
        ('name', ''),
        ('tests', f'{overall_test_count}'),
        ('failures', f'{overall_failures}'),
        ('errors', f'{overall_errors}'),
        ('time', f'{(self.overall_end_time - self.overall_start_time):.3f}'),
        ('timestamp', xml_reporter._iso8601_timestamp(self.overall_start_time)),
    ]
    xml_reporter._print_xml_element_header(
        'testsuites', overall_attributes, stream
    )
    if self._testsuites_properties:
      stream.write('    <properties>\n')
      for name, value in sorted(self._testsuites_properties.items()):
        stream.write(
            '      <property name="%s" value="%s"></property>\n'
            % (
                xml_reporter._escape_xml_attr(name),
                xml_reporter._escape_xml_attr(str(value)),
            )
        )
      stream.write('    </properties>\n')

    for suite_name in self.suites:
      suite = self.suites[suite_name]
      suite_end_time = max(x.start_time + x.run_time for x in suite)
      suite_start_time = min(x.start_time for x in suite)
      failures = self.failure_counts[suite_name]
      errors = self.error_counts[suite_name]
      suite_attributes = [
          ('name', f'{suite_name}'),
          ('tests', f'{len(suite)}'),
          ('failures', f'{failures}'),
          ('errors', f'{errors}'),
          ('time', f'{(suite_end_time - suite_start_time):.3f}'),
          ('timestamp', xml_reporter._iso8601_timestamp(suite_start_time)),
      ]
      xml_reporter._print_xml_element_header(
          'testsuite', suite_attributes, stream
      )

      # test_case_result entries are not guaranteed to be in any user-friendly
      # order, especially when using subtests. So sort them.
      for test_case_result in sorted(suite, key=lambda t: t.start_time):
        test_case_result.print_xml_summary(stream)
      stream.write('</testsuite>\n')
    stream.write('</testsuites>\n')


# pylint: disable=protected-access
class TestResult(xml_reporter._TextAndXMLTestResult):
  """Test Result class to write test results even when test is terminated."""

  _TEST_SUITE_RESULT_CLASS = _TestSuiteResult
  _TEST_CASE_RESULT_CLASS = _TestCaseResult

  # Instance of TestResult class. Allows writing test results when suite is
  # terminated - use `writeAllResultsToXml` classmethod.
  # Technicaly it's possible to have more than one instance of this class but it
  # doesn't happen when running tests that write to XML file (since they'd
  # override this file results) so we can safely use only last created instance.
  _instance = None

  def __init__(self, logger=logging.getLogger(), *args, **kwargs):
    super().__init__(*args, **kwargs)
    TestResult._instance = self
    self._logger = logger

  @classmethod
  def write_summary_in_txt(
      cls,
      report_info: ReportInfo | None = None,
  ) -> None:
    """Saves summary to a txt file.

    Args:
      report_info: Versions and device info displayed in generated txt report.
        Versions includes GHA, GMSCore, hub and device firmware. Device info is
        in <model, type, protocol> format, e.g. <X123123, LIGHT, Matter>.
    """
    if not cls._instance:
      return

    summary_file_path = (
        f"summary_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.txt"
    )

    test_results_by_test_name: dict[str, list[_TestCaseResult]] = (
        collections.defaultdict(list)
    )
    # Groups test cases by its name for later sorting.
    # It is to avoid incorrect sorting as different suites may run same test
    # cases, but those test cases do not run in order.
    for suite_name in cls._instance.suite.suites:
      suite = cls._instance.suite.suites[suite_name]
      for test_case_result in suite:
        test_results_by_test_name[test_case_result.name].append(
            test_case_result
        )

    if not test_results_by_test_name:
      cls._instance._logger.info('Summary can not be saved without test runs.')
      return

    # Tests can be stopped unexpectedly, so find the maximum as total runs.
    total_runs = max(map(len, test_results_by_test_name.values()))

    is_regression_test_pass = [True for _ in range(total_runs)]

    # Save each test case result to a temp stream.
    test_case_result_stream = io.StringIO()
    test_case_result_stream.write(
        f"{'Test Case/Test Run':<{_TEST_CASE_TITLE_INDENTS}}"
    )
    for i in range(total_runs):
      test_case_result_stream.write(f"{f'#{i + 1}':<{_TEST_RESULT_INDENTS}}")
    for test_case_title in _REPORT_TEST_CASE_TITLE_TO_TEST_NAME:
      if test_results_by_test_name[
          _REPORT_TEST_CASE_TITLE_TO_TEST_NAME[test_case_title]
      ]:
        test_case_result_stream.write('\n')
        test_case_result_stream.write(
            f'{test_case_title:<{_TEST_CASE_TITLE_INDENTS}}'
        )
        for i, test_result in enumerate(
            sorted(
                test_results_by_test_name[
                    _REPORT_TEST_CASE_TITLE_TO_TEST_NAME[test_case_title]
                ],
                key=lambda t: t.start_time,
            )
        ):
          if is_regression_test_pass[i] and test_result.result != 'PASS':
            is_regression_test_pass[i] = False
          test_case_result_stream.write(
              f'{test_result.result:<{_TEST_RESULT_INDENTS}}'
          )

    # Start writing summary.
    test_date = time.strftime(
        '%Y/%m/%d', time.localtime(cls._instance.suite.overall_start_time)
    )
    duration = duration_formatter(
        cls._instance.suite.overall_end_time
        - cls._instance.suite.overall_start_time
    )
    total_successful_runs = is_regression_test_pass.count(True)
    success_rate = round(
        100.0 * float(total_successful_runs) / float(total_runs)
    )
    report_info = report_info or {}
    data_indents = _MINIMUM_SUMMARY_COL_INDENTS
    for value in report_info.values():
      # Set indents to the maximum length of values in report info.
      # Add 2 extra spaces to separate data and next header.
      # If the value is less than minimum column indents, use the minimum.
      data_indents = max(data_indents, len(value) + 2)
    rows: list[list[str]] = []
    rows.append(['Summary', '', 'Version Info', ''])
    rows.append([
        'DUT:',
        report_info.get('dut', _NA),
        'GHA',
        report_info.get('gha_version', _NA),
    ])
    rows.append([
        'Test Time:',
        test_date,
        'GMSCore',
        report_info.get('gms_core_version', _NA),
    ])
    rows.append([
        'Duration:',
        duration,
        'Hub',
        report_info.get('hub_version', _NA),
    ])
    rows.append([
        'Number of runs:',
        str(total_runs),
        'Device',
        report_info.get('device_firmware', _NA),
    ])
    rows.append([
        'Success Rate:',
        f'{success_rate}%({total_successful_runs}/{total_runs})',
    ])

    f = open(summary_file_path, 'w', encoding='utf-8')
    for row in rows:
      for i, element in enumerate(row):
        if i % 2 == 0:
          # Writes header.
          f.write(element.ljust(_MINIMUM_SUMMARY_COL_INDENTS))
        else:
          f.write(element.ljust(data_indents))
      f.write('\n')

    f.writelines(['\n', '\n'])

    # Writes test case result saved in temp stream.
    f.write(test_case_result_stream.getvalue())

    f.close()
    cls._instance._logger.info(
        'Summary of regression tests has been written to %s.', summary_file_path
    )

  @classmethod
  def writeAllResultsToXml(cls):
    """Writes current results to XML output. Used when test is interrupted."""
    if cls._instance:
      cls._instance.writeXmlResultsForTerminatedSuite()

  def writeXmlResultsForTerminatedSuite(self):
    """Writes test results to XML output."""
    self._writeSuiteResultsToXml()
    self._logger.info('TestResult class stream written to results XML.')

  def _writeSuiteResultsToXml(self):
    self.suite.print_xml_summary(self.xml_stream)


class TestRunner(xml_reporter.TextAndXMLTestRunner):
  """A test runner that can produce both formatted text results and XML.

  It prints out a summary of the results in XML and a summary of results in TXT
  at the end of the test run even if the test is interrupted.
  """

  _TEST_RESULT_CLASS = TestResult

  def __init__(
      self, xml_file_path=None, logger=logging.getLogger(), *args, **kwargs
  ):
    """Initializes a TestRunner.

    Args:
      xml_file_path: XML-formatted test results are output to this file path. If
        None (the default), xml file will be written to default path.
      logger: Logger instance.
      *args: passed unmodified to xml_reporter.TextAndXMLTestRunner.__init__.
      **kwargs: passed unmodified to xml_reporter.TextAndXMLTestRunner.__init__.
    """
    self._logger = logger
    cur_path = os.path.abspath(os.path.dirname(__file__))
    default_xml_file_path = os.path.join(
        cur_path,
        f"summary_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.xml",
    )
    self._xml_file_path = xml_file_path or default_xml_file_path
    super().__init__(xml_stream=open(self._xml_file_path, 'w'), *args, **kwargs)

  def run(
      self,
      suite: unittest.TestSuite,
      report_info: Mapping[str, str | None] | None = None,
  ) -> None:
    """Runs tests and generates reports in XML and TXT.

    Args:
      suite: TestSuite should be run for regression testing.
      report_info: Versions and device info displayed in generated txt report.
        Versions includes GHA, GMSCore, hub and device firmware. Device info is
        in <model, type, protocol> format, e.g. <X123123, LIGHT, Matter>.
    """
    try:
      super().run(suite)
    except KeyboardInterrupt:
      # In case tests are interrupted, xml file won't be written by TestRunner.
      # Hence, call `writeAllResultsToXml` to write data to given xml path.
      TestResult.writeAllResultsToXml()
    finally:
      self._logger.info(f'Xml file saved to {self._xml_file_path}.')
      TestResult.write_summary_in_txt(report_info=report_info)

  def _makeResult(self):
    return self._TEST_RESULT_CLASS(
        logger=self._logger,
        xml_stream=self._xml_stream,
        stream=self.stream,
        descriptions=self.descriptions,
        verbosity=self.verbosity,
        time_getter=time.time,
        testsuites_properties=self._testsuites_properties,
    )
