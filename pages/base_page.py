import math
from selenium.common.exceptions import *
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        """Открыть ссылку"""
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, by, locator, timeout=4) -> bool:
        """Проверка на присутсвие элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False
        return True

    def get_element(self, by, locator, timeout=10) -> object:
        """Найти и получить элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {locator} not found: {e}")
            return None

    def is_not_element_present(self, by, locator, timeout=4) -> bool:
        """Элемент не появляется на странице в течение заданного времени.
        Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by, locator, timeout=4) -> bool:
        """Проверить, что какой-то элемент исчезает.
         Будет ждать до тех пор, пока элемент не исчезнет."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False
        return True

    def go_to_basket_page(self):
        """Переходит в корзину по кнопке в шапке сайта"""
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        """Функция для вычисления задачи из алерта"""
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
