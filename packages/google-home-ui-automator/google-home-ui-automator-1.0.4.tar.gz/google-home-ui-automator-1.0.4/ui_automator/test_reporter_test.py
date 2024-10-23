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

"""Unittest for test reporter."""
import io
import logging
import os
import re
import time
import traceback
from typing import Any, Literal
import unittest
from unittest import mock

from absl.testing import xml_reporter

from ui_automator import test_reporter
from ui_automator import unit_test_utils


class StringIOWriteLn(io.StringIO):

  def writeln(self, line):
    self.write(line + '\n')


class MockTest(unittest.TestCase):
  failureException = AssertionError

  def __init__(self, name):
    super().__init__()
    self.name = name

  def id(self):
    return self.name

  def shortDescription(self):
    return "This is this test's description."


def _run_test_from_result(
    test: MockTest,
    test_result: test_reporter.TestResult,
    result: Literal['PASS', 'N/A', 'FAIL'],
    err=None,
    skip_reason: str | None = None,
) -> None:
  test_result.startTest(test)
  if result == 'FAIL':
    test_result.addError(test, err)
  elif result == 'N/A':
    test_result.addSkip(test, skip_reason)
  else:
    test_result.addSuccess(test)
  test_result.stopTest(test)


class TestReporterTest(unittest.TestCase):

  def setUp(self):
    super().setUp()
    self.stream = StringIOWriteLn()
    self.xml_stream = io.StringIO()

  def _make_result(
      self, start_time: int, end_time: int, test_count: int
  ) -> test_reporter.TestResult:
    # Called by result.startTestRun().
    times = [start_time]
    for i in range(test_count):
      # Called by result.startTest().
      times.append(start_time)
      # Called by result.stopTest().
      times.append(end_time + i)
    # Called by result.stopTestRun().
    times.append(end_time + test_count - 1)
    with mock.patch.object(time, 'time', autospec=True, side_effect=times):
      return test_reporter.TestResult(
          xml_stream=self.xml_stream,
          stream=self.stream,
          descriptions=True,
          verbosity=0,
          time_getter=time.time,
      )

  def _assert_match(self, regex, output, flags=0) -> tuple[str | Any, ...]:
    result = re.search(regex, output, flags)
    if result is None:
      self.fail(f'{output} does not match {regex}.')
    return result.groups()

  def test_with_skipped_test(self):
    start_time = 100
    end_time = 200
    test_name = 'skipped_test_with_reason'
    result = self._make_result(start_time, end_time, 1)
    start_time_str = re.escape(unit_test_utils.iso_timestamp(start_time))
    run_time = end_time - start_time
    expected_re = unit_test_utils.OUTPUT_STRING % {
        'suite_name': 'MockTest',
        'tests': 1,
        'failures': 0,
        'errors': 0,
        'run_time': run_time,
        'start_time': start_time_str,
    }
    expected_testcase_re = unit_test_utils.TESTCASE_STRING_WITH_PROPERTIES % {
        'run_time': run_time,
        'start_time': start_time_str,
        'test_name': test_name,
        'status': 'notrun',
        'class_name': '',
        'result': 'N/A',
        'properties': (
            '      <property name="skip_reason" value="skip"></property>'
        ),
        'message': '',
    }

    test = MockTest('%s' % test_name)
    result.startTestRun()
    result.startTest(test)
    result.addSkip(test, 'skip')
    result.stopTest(test)
    result.stopTestRun()
    result.printErrors()

    (testcase,) = self._assert_match(
        expected_re, self.xml_stream.getvalue(), re.DOTALL
    )
    self.assertRegex(testcase, expected_testcase_re)

  def test_with_errored_test(self):
    start_time = 100
    end_time = 200
    test_name = 'test_with_errors'
    result = self._make_result(start_time, end_time, 1)
    fake_error = Exception('fake_error')
    err = (Exception, fake_error, fake_error.__traceback__)
    start_time_str = re.escape(unit_test_utils.iso_timestamp(start_time))
    run_time = end_time - start_time
    expected_re = unit_test_utils.OUTPUT_STRING % {
        'suite_name': 'MockTest',
        'tests': 1,
        'failures': 0,
        'errors': 1,
        'run_time': run_time,
        'start_time': start_time_str,
    }
    expected_testcase_re = unit_test_utils.TESTCASE_STRING_WITH_ERRORS % {
        'run_time': run_time,
        'start_time': start_time_str,
        'test_name': test_name,
        'status': 'run',
        'class_name': '',
        'result': 'FAIL',
        'message': xml_reporter._escape_xml_attr(str(err[1])),
        'error_type': xml_reporter._escape_xml_attr(str(err[0])),
        'error_msg': xml_reporter._escape_cdata(
            ''.join(traceback.format_exception(*err))
        ),
    }

    test = MockTest('%s' % test_name)
    result.startTestRun()
    result.startTest(test)
    result.addError(test, err)
    result.stopTest(test)
    result.stopTestRun()
    result.printErrors()

    (testcase,) = self._assert_match(
        expected_re, self.xml_stream.getvalue(), re.DOTALL
    )
    self.assertRegex(testcase, expected_testcase_re)

  @mock.patch('builtins.open', autospec=True)
  def test_write_summary_in_txt_saves_summary_to_a_file(self, mock_open):
    txt_stream = io.StringIO()
    mock_open.return_value = txt_stream
    start_time = 100
    end_time = 200
    result = self._make_result(start_time, end_time, 6)
    fake_error = Exception('fake_error')
    err = (Exception, fake_error, fake_error.__traceback__)
    # 5 is the number explicitly add in _make_result.
    run_time = end_time - start_time + 5
    now = time.localtime()
    fake_report_info = {
        'gha_version': '1',
        'gms_core_version': '2',
        'hub_version': '1',
        'device_firmware': '1',
        'dut': '1',
    }
    expected_summary = re.escape(
        unit_test_utils.make_summary(
            test_date=time.strftime('%Y/%m/%d', now),
            duration=test_reporter.duration_formatter(run_time),
            total_runs=3,
            total_successful_runs=2,
            report_info=fake_report_info,
        )
    )
    res_of_test_commission = ['FAIL', 'PASS', 'PASS']
    res_of_test_decommission = ['N/A', 'PASS', 'PASS']
    expected_test_case_result = unit_test_utils.make_test_case_result(
        3,
        res_of_test_commission=res_of_test_commission,
        res_of_test_decommission=res_of_test_decommission,
    )
    test_commission_first_round = MockTest('test_commission')
    test_decommission_first_round = MockTest('test_decommission')
    test_commission_second_round = MockTest('test_commission')
    test_decommission_second_round = MockTest('test_decommission')
    test_commission_third_round = MockTest('test_commission')
    test_decommission_third_round = MockTest('test_decommission')
    result.startTestRun()
    _run_test_from_result(
        test_commission_first_round,
        result,
        res_of_test_commission[0],
        err,
    )
    _run_test_from_result(
        test_decommission_first_round,
        result,
        res_of_test_decommission[0],
        skip_reason='skip',
    )
    _run_test_from_result(
        test_commission_second_round, result, res_of_test_commission[1]
    )
    _run_test_from_result(
        test_decommission_second_round,
        result,
        res_of_test_decommission[1],
    )
    _run_test_from_result(
        test_commission_third_round, result, res_of_test_commission[2]
    )
    _run_test_from_result(
        test_decommission_third_round, result, res_of_test_decommission[2]
    )
    result.stopTestRun()
    result.printErrors()

    with mock.patch.object(txt_stream, 'close'):
      with mock.patch.object(time, 'localtime', return_value=now):
        test_reporter.TestResult.write_summary_in_txt(fake_report_info)

    mock_open.assert_called_once_with(
        f"summary_{time.strftime('%Y%m%d%H%M%S', now)}.txt",
        'w',
        encoding='utf-8',
    )
    self.assertRegex(txt_stream.getvalue(), expected_summary)
    self.assertRegex(txt_stream.getvalue(), expected_test_case_result)

  @mock.patch.object(
      xml_reporter.TextAndXMLTestRunner,
      'run',
      autospec=True,
      side_effect=KeyboardInterrupt,
  )
  @mock.patch.object(
      test_reporter.TestResult, 'write_summary_in_txt', autospec=True
  )
  @mock.patch.object(
      test_reporter.TestResult, 'writeAllResultsToXml', autospec=True
  )
  @mock.patch('builtins.open', autospec=True)
  def test_run_writes_result_in_xml_and_txt_on_interruption(
      self,
      mock_open,
      mock_write_all_results_to_xml,
      mock_write_summary_in_txt,
      mock_run,
  ):
    fake_suite = unittest.TestSuite()
    now = time.localtime()
    expected_xml_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        f"summary_{time.strftime('%Y%m%d%H%M%S', now)}.xml",
    )

    with mock.patch.object(time, 'localtime', return_value=now):
      test_reporter.TestRunner(xml_file_path=expected_xml_path).run(fake_suite)

    mock_open.assert_called_once_with(expected_xml_path, 'w')
    mock_write_all_results_to_xml.assert_called_once()
    mock_write_summary_in_txt.assert_called_once()
    mock_run.assert_called_once()

  def test_duration_formatter_returns_correct_duration(self):
    duration_in_seconds = 3601.0

    duration = test_reporter.duration_formatter(duration_in_seconds)

    self.assertEqual(duration, '1 hrs, 0 mins, 1 secs')

  @mock.patch('builtins.open', autospec=True)
  def test_write_summary_in_txt_should_not_write_any_without_test_result(
      self, mock_open
  ):
    test_reporter.TestResult._instance = None

    test_reporter.TestResult.write_summary_in_txt()

    mock_open.assert_not_called()

  def test_write_summary_in_txt_should_not_write_any_without_test_runs(self):
    start_time = 100
    end_time = 200
    self._make_result(start_time, end_time, 0)

    with self.assertLogs() as cm:
      test_reporter.TestResult.write_summary_in_txt()

    self.assertEqual(
        cm.output[0], 'INFO:root:Summary can not be saved without test runs.'
    )

  @mock.patch('builtins.open', autospec=True)
  def test_test_runner_init_injects_correct_logger(self, mock_open):
    logger = logging.getLogger('test_reporter')
    fake_suite = unittest.TestSuite()
    now = time.localtime()
    expected_xml_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        f"summary_{time.strftime('%Y%m%d%H%M%S', now)}.xml",
    )

    with mock.patch.object(time, 'localtime', return_value=now):
      with self.assertLogs(logger) as cm:
        test_reporter.TestRunner(xml_file_path=None, logger=logger).run(
            fake_suite
        )

    mock_open.assert_called_once_with(expected_xml_path, 'w')
    self.assertEqual(
        cm.output[0],
        f'INFO:test_reporter:Xml file saved to {expected_xml_path}.',
    )


if __name__ == '__main__':
  unittest.main()
