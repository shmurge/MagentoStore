import allure
from pages.header_page import HeaderPage
from config.links import Links
from elements.base_element import BaseElement
from locators.locs_account_page import AccountPageLocators


class AccountPage(HeaderPage):
    PAGE_URL = Links.ACCOUNT_PAGE

    def __init__(self, browser):
        super().__init__(browser)

        self.contact_information = BaseElement(
            self.browser, 'Контактная информация', *AccountPageLocators.CONTACT_INFORMATION)

    @allure.step('Имя пользователя и почта на странице аккаунта корректны')
    def correct_username_and_email_in_contact_info(self, firstname, lastname, user_email):
        self.contact_information.scroll_to_element()
        act_res = self.contact_information.get_text_of_element().strip()
        exp_res = (f'{firstname} {lastname}\n'
                   f'{user_email}')

        self.base_assertions.assert_data_equal_data(act_res, exp_res)

