from selenium.webdriver.common.by import By


class TestProduct:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def test_add_to_basket_form(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        trash = browser.find_element(By.ID, "add_to_basket_form")
        assert trash.is_enabled(), "Кнопка добавить в корзину отсутствует"
