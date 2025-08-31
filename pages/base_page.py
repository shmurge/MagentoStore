import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from assertions.base_assertions import BaseAssertions


class BasePage:

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout=15, poll_frequency=1)
        self.base_assertions = BaseAssertions()

    def open(self):
        with allure.step(f'Открыть страницу: {self.PAGE_URL}'):
            self.browser.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f'Страница {self.PAGE_URL} открыта'):
            print()
            print(self.PAGE_URL)
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def open_link_in_new_tab(self, element):
        with allure.step('Открыть в новой вкладке'):
            action = AC(self.browser)
            action.key_down(Keys.COMMAND)
            action.click(element)
            action.key_up(Keys.COMMAND)
            action.perform()

    def switch_to_new_tab(self):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

    def switch_to_previous_tab(self):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[0])

    def should_be_correct_page(self, path):
        assert path in self.browser.current_url, (f'Некорректный URL!'
                                                  f'URL должен содержать "{path}"'
                                                  f'Текущий URL: {self.browser.current_url}')
