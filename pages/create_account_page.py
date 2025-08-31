import allure
import pytest
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from pages.base_page import BasePage
from config.links import Links
from locators.locs_create_account_page import CreateAccountPageLocators
from locators.locs_account_page import AccountPageLocators
from conftest import set_env_key


class CreateAccountPage(BasePage):
    PAGE_URL = Links.CREATE_ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.fake = Faker()
        self.registration_form = BaseElement(
            self.browser, 'Форма регистрации', *CreateAccountPageLocators.REGISTRATION_FORM
        )
        self.firstname_input = Input(self.browser, 'Имя', *CreateAccountPageLocators.INPUT_FIRSTNAME)
        self.lastname_input = Input(self.browser, 'Фамилия', *CreateAccountPageLocators.INPUT_LASTNAME)
        self.email_input = Input(self.browser, 'Email', *CreateAccountPageLocators.INPUT_EMAIL)
        self.password_input = Input(self.browser, 'Пароль', *CreateAccountPageLocators.INPUT_PASSWORD)
        self.password_confirm_input = Input(
            self.browser, 'Подтверждение пароля', *CreateAccountPageLocators.INPUT_CONFIRM_PASSWORD
        )
        self.success_registration = BaseElement(
            self.browser, 'Сообщение об успешной регистрации', *AccountPageLocators.SUCCESS_REGISTRATION_ALERT)

    @allure.step('Заполнить поле Имя')
    def fill_firstname(self, data=None):
        data = data if data else self.fake.first_name()
        self.firstname_input.fill_input(data)

        return data

    @allure.step('Заполнить поле Фамилия')
    def fill_lastname(self, data=None):
        data = data if data else self.fake.last_name()
        self.lastname_input.fill_input(data)

        return data

    @allure.step('Заполнить поле Email')
    def fill_email(self, data=None, save_to_env=True):
        data = data if data else self.fake.email()
        self.email_input.fill_input(data)

        if save_to_env:
            set_env_key('LOGIN', data)

        return data

    @allure.step('Заполнить поля Пароль и Подтверждение пароля')
    def fill_passwords(self, password=None, confirm=None, save_to_env=True):
        password = password if password else self.fake.password(length=8,
                                                                digits=True,
                                                                lower_case=True,
                                                                upper_case=True,
                                                                special_chars=True)
        confirm = confirm if confirm else password
        self.password_input.fill_input(password)
        self.password_confirm_input.fill_input(confirm)
        if save_to_env:
            set_env_key('PASSWORD', password)

    @allure.step('Заполнить поле Подтверждение пароля')
    def fill_password_confirm(self, data):
        self.password_confirm_input.fill_input(data)

    @allure.step('Заполнить форму регистрации')
    def fill_registration_form(self,
                               firstname=None,
                               lastname=None,
                               email=None,
                               password=None,
                               password_confirm=None):
        self.registration_form.scroll_to_element()
        f_name = self.fill_firstname(firstname)
        l_name = self.fill_lastname(lastname)
        email = self.fill_email(email)
        self.fill_passwords(password, password_confirm)
        self.registration_form.submit()

        return f_name, l_name, email

    @allure.step('Отображается сообщение об успешной регистрации')
    def should_be_message_success_registration(self):
        assert self.success_registration.is_visible(), 'Сообщение об успешной регистрации не отображается!'
