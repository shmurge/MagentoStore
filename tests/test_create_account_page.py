import allure
import pytest
from time import sleep
from config.base_test import BaseTest


@allure.suite('Пользователь')
@pytest.mark.positive
class TestCreateAccountPagePositive(BaseTest):

    @allure.title('Регистрация пользователя с валидными данными')
    def test_create_account(self):
        self.create_account_page.open()
        f_name, l_name, user_email = self.create_account_page.fill_registration_form()

        self.create_account_page.should_be_message_success_registration()
        self.header_page.account_link_contains_a_greeting_user(f_name, l_name)
        self.account_page.is_opened()
        self.account_page.correct_username_and_email_in_contact_info(f_name, l_name, user_email)

