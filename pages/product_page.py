from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def press_add_basket(self):
        button_add_basket = self.browser.find_element(*BasketPageLocators.BUTTON_ADD_IN_BASKET)
        button_add_basket.click()

    def should_be_name_product_before_equal_after_add_basket(self):
        product_name1 = self.get_element(*BasketPageLocators.PRODUCT_NAME_BEFORE_ADD_BASKET).text
        product_name2 = self.get_element(*BasketPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET).text
        print(product_name1, "==", product_name2, "?")
        assert product_name1 == product_name2, "Product names added to the basket are not equal"

    def should_be_price_product_before_equal_after_add_basket(self):
        price1 = self.get_element(*BasketPageLocators.PRICE_PRODUCT_BEFORE_ADD_BASKET).text
        price2 = self.get_element(*BasketPageLocators.PRICE_PRODUCT_AFTER_ADD_BASKET).text
        print(price1, "==", price2, "?")
        assert price1 == price2, "Product price added to the basket are not equal"
