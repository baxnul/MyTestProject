import math
from selenium.common.exceptions import *
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, locator) -> bool:
        """Find an element given a By strategy and locator"""
        try:
            self.browser.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True

    def get_element(self, by, locator, timeout=2):
        """Find an element given a By strategy and locator"""
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {locator} not found: {e}")
            return None

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
