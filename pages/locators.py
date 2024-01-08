from selenium.webdriver.common.by import By

"""(Tuple have: By selector, locator, timeout wait)"""


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # link for negative test
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs .btn.btn-default")


class MainPageLocators:
    pass

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BUTTON_ADD_IN_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_BEFORE_ADD_BASKET = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_PRODUCT_BEFORE_ADD_BASKET = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME_AFTER_ADD_BASKET = (By.CSS_SELECTOR, ".alert-success > .alertinner strong")
    PRICE_PRODUCT_AFTER_ADD_BASKET = (By.CSS_SELECTOR, ".alert-info > .alertinner strong")
    SUCCESS_MESSAGE_ADDING_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".row h2")
