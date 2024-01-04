from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.press_add_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_product_before_equal_after_add_basket()
    page.should_be_price_product_before_equal_after_add_basket()
