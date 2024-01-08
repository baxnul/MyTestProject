import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    """Пользователь может добавлять товары в корзину и наименование и цена товара на странице
    и в сообщение успешного добавления в корзину одинаковые"""
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.press_add_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_product_before_add_basket_equal_after_add_basket()
    page.should_be_price_product_before_add_basket_equal_after_add_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Пользователь НЕ должен увидеть после добавления товара в корзину сообщение,
     об успешном добавлении товара"""
    page = ProductPage(browser, links[0])
    page.open()
    page.press_add_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """Пользователь НЕ должен увидеть сообщение об успешном добавлении товара в корзину"""
    page = ProductPage(browser, links[0])
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Сообщение добавления в корзину должно исчезнуть после добавления товара в корзину"""
    page = ProductPage(browser, links[0])
    page.open()
    page.press_add_basket()
    page.solve_quiz_and_get_code()
    page.should_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """Пользователь должен видеть кнопку со ссылкой для перехода к авторизации"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """Пользователь может перейти на страницу авторизации"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Не должно быть товаров в корзине и должна быть надпись о том что корзина пустая"""
    page = BasketPage(browser, links[0])
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()  # Не должно быть товаров в корзине
    page.should_be_title_basket_empty()  # Должна быть надпись о том что корзина пустая
