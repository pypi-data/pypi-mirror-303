from __future__ import annotations
from typing import TYPE_CHECKING
import unittest

# pylint:disable=g-import-not-at-top
if TYPE_CHECKING:
  from ui_automator import ui_automator


class CommissionRegTest(unittest.TestCase):
  """Test class for running commission regression test."""

  def __init__(
      self,
      ui_automator: ui_automator.UIAutomator,
      test_name: str,
      device_name: str | None,
      pairing_code: str | None = None,
      gha_room: str | None = None,
  ) -> None:
    super().__init__(methodName=test_name)
    self.ui_automator = ui_automator
    self.device_name = device_name
    self.pairing_code = pairing_code
    self.gha_room = gha_room

  def test_commission(self) -> None:
    self.ui_automator.commission_device(
        self.device_name, self.pairing_code, self.gha_room
    )

  def test_decommission(self) -> None:
    if not self.ui_automator.is_device_exist(self.device_name):
      self.skipTest('Device was not commissioned.')

    self.ui_automator.decommission_device(self.device_name)
