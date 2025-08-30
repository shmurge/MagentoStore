import allure
import pytest
from pages.base_page import BasePage
from config.links import Links
from elements.button import Button
from locators.locs_main_page import MainPageLocators


class MainPage(BasePage):
    PAGE_URL = Links.MAIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.login_link = Button(self.browser, 'Войти', *MainPageLocators.LOGIN_LINK)

    def goto_login_page(self):
        self.login_link.click()