from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def press_add_basket(self):
        button_add_basket = self.browser.find_element(*BasketPageLocators.BUTTON_ADD_IN_BASKET)
        button_add_basket.click()

    def should_be_name_product_before_equal_after_add_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_NAME_BEFORE_ADD_BASKET) == self.is_element_present(
            *BasketPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET), "Product names added to the basket are not equal"

    def should_be_price_product_before_equal_after_add_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRICE_PRODUCT_BEFORE_ADD_BASKET) == self.is_element_present(
            *BasketPageLocators.PRICE_PRODUCT_AFTER_ADD_BASKET), "Product price added to the basket are not equal"
