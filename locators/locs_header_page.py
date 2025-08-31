from selenium.webdriver.common.by import By


class HeaderPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '[class="panel header"] [class="authorization-link"]')
    ACCOUNT_LINK = (By.CSS_SELECTOR, '[class="panel header"] [class="logged-in"]')