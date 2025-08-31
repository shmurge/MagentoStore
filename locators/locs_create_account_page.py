from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    REGISTRATION_FORM = (By.XPATH, '//*[contains(@class, "form-create-account")]')
    INPUT_FIRSTNAME = (By.XPATH, '//*[@id="firstname"]')
    INPUT_LASTNAME = (By.XPATH, '//*[@id="lastname"]')
    INPUT_EMAIL = (By.XPATH, '//*[@id="email_address"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@id="password"]')
    INPUT_CONFIRM_PASSWORD = (By.XPATH, '//*[@id="password-confirmation"]')

