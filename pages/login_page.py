import allure
import pytest
from pages.base_page import BasePage
from config.links import Links


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE