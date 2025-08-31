from selenium.webdriver.common.by import By


class AccountPageLocators:
    SUCCESS_REGISTRATION_ALERT = (By.XPATH, '//*[@data-ui-id="message-success"]')

    CONTACT_INFORMATION = (By.CSS_SELECTOR, '[class="box box-information"] [class="box-content"]')