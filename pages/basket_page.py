from .base_page import BasePage
from .locators import BasketPageLocators

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        """Ожидаем, что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)

    def should_be_title_basket_empty(self):
        """Ожидаем, что есть текст о том что корзина пуста"""
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")  # Вернет язык en, ru, и.т.д.
        text_basket_empty = languages.get(str(language))
        assert text_basket_empty in self.get_element(*BasketPageLocators.EMPTY_BASKET).text, "Корзина должна быть пустой"
