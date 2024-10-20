from unittest import TestCase

from movsviewer.constants import GECKODRIVER_PATH
from movsviewer.constants import MAINUI_UI_PATH
from movsviewer.constants import SETTINGSUI_UI_PATH


class TestConstants(TestCase):
    def test_paths_exist(self) -> None:
        for path in (MAINUI_UI_PATH, SETTINGSUI_UI_PATH, GECKODRIVER_PATH):
            with self.subTest(path):
                self.assertTrue(path.is_file())
