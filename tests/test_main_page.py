import pytest
from time import sleep
from config.base_test import BaseTest


class TestMainPagePositive(BaseTest):

    def test_open(self):
        self.main_page.open()
        self.main_page.goto_login_page()
        self.login_page.is_opened()
        sleep(20)

