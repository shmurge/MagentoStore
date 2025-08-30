from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException


class Wait:

    def __init__(self, browser, timeout=10, poll_frequency=1):
        self.browser = browser
        self.timeout = timeout
        self.poll_frequency = poll_frequency

    def is_element_present(self, how, what):
        try:
            WebDriverWait(
                self.browser,
                self.timeout,
                self.poll_frequency
            ).until(
                EC.presence_of_element_located((how, what))
            )
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(
                self.browser,
                self.timeout,
                self.poll_frequency
            ).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, how, what):
        try:
            WebDriverWait(
                self.browser,
                self.timeout,
                self.poll_frequency).until(
                EC.visibility_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def is_not_element_visible(self, how, what):
        try:
            WebDriverWait(
                self.browser,
                self.timeout,
                self.poll_frequency).until_not(EC.visibility_of_element_located((how, what))
                                               )
        except TimeoutException:
            return False
        return True
