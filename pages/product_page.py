from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        """Сообщение об успешном добавлении товара в корзину не должна присутствовать"""
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE_ADDING_BASKET), "Success message added in basket is presented, " \
                                                                 "but should not be"

    def press_add_basket(self):
        """Нажать добавить товар в корзину"""
        button_add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_IN_BASKET)
        button_add_basket.click()

    def should_be_name_product_before_add_basket_equal_after_add_basket(self):
        """Имя товара на странице товара и в сообщении об успешном добавлении в корзину должны быть одинаковые"""
        product_name1 = self.get_element(*ProductPageLocators.PRODUCT_NAME_BEFORE_ADD_BASKET).text
        product_name2 = self.get_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADD_BASKET).text
        print(product_name1, "==", product_name2, "?")
        assert product_name1 == product_name2, "Product names added to the basket are not equal before added in basket"

    def should_be_price_product_before_add_basket_equal_after_add_basket(self):
        """Цена товара на странице товара и в сообщении об успешном добавлении в корзину должны быть одинаковые"""
        price1 = self.get_element(*ProductPageLocators.PRICE_PRODUCT_BEFORE_ADD_BASKET).text
        price2 = self.get_element(*ProductPageLocators.PRICE_PRODUCT_AFTER_ADD_BASKET).text
        print(price1, "==", price2, "?")
        assert price1 == price2, "Product price added to the basket are not equal before added in basket"

    def should_is_disappeared(self):
        """Сообщение добавления в корзину должно исчезнуть"""
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE_ADDING_BASKET), "The success message does not disappear, but should"
