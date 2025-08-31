import allure
import pytest
from pages.base_page import BasePage
from config.links import Links
from elements.button import Button
from locators.locs_header_page import HeaderPageLocators


class HeaderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

        self.login_link = Button(self.browser, 'Войти', *HeaderPageLocators.LOGIN_LINK)
        self.account_tink = Button(self.browser, 'Аккаунт', *HeaderPageLocators.ACCOUNT_LINK)

    @allure.step('Перейти на страницу авторизации')
    def goto_login_page(self):
        self.login_link.click()

    @allure.step('Перейти на страницу аккаунта')
    def goto_account_page(self):
        self.account_tink.click()

    @allure.step('Ссылка на аккаунт приветствует пользователя')
    def account_link_contains_a_greeting_user(self, firstname, lastname):
        act_res = f'Welcome, {firstname} {lastname}!'
        exp_res = self.account_tink.get_text_of_element()

        self.base_assertions.assert_data_equal_data(act_res, exp_res)
