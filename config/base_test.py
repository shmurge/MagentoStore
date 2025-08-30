import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class BaseTest:
    main_page = MainPage
    login_page = LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser

        request.cls.main_page = MainPage(browser)
        request.cls.login_page = LoginPage(browser)
