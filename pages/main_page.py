import allure
import pytest
from pages.header_page import HeaderPage
from config.links import Links
from elements.button import Button
from locators.locs_main_page import MainPageLocators


class MainPage(HeaderPage):
    PAGE_URL = Links.MAIN_PAGE

    def __init__(self, browser):
        super().__init__(browser)
