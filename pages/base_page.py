from selenium.common.exceptions import *


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, locator):
        """Find an element given a By strategy and locator"""
        try:
            self.browser.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True
