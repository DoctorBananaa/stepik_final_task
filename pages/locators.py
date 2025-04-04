from selenium.webdriver.common.by import By


class BasePageLocators:
    LANGUAGE_SELECT = By.CSS_SELECTOR, 'select[name="language"]'
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"
    LOGIN_LINK_INVALID = By.CSS_SELECTOR, "#login_link_inc"

class MainPageLocators(BasePageLocators):
    BASKET_LINK = By.CSS_SELECTOR, '[href="/{}/basket/"]'

class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = By.ID, 'login_form'
    REGISTER_FORM = By.ID, 'register_form'

class ProductPageLocators(BasePageLocators):
    ADD_BASKET_BTN = By.CLASS_NAME, 'btn-add-to-basket'
    PRODUCT_NAME = By.CSS_SELECTOR, '.product_main > h1'
    PRODUCT_PRICE = By.CSS_SELECTOR, '.product_main > p'
    PRODUCT_NAME_BASKET = By.CSS_SELECTOR, '#messages .alert-noicon:nth-child(1) strong'
    PRODUCT_PRICE_BASKET = By.CSS_SELECTOR, '#messages .alert-noicon:nth-child(3) strong'
    BASKET_LINK = By.CSS_SELECTOR, '[href="/{}/basket/"]'

class BasketPageLocators(BasePageLocators):
    PRODUCT_LIST = By.ID, 'basket_formset'
    BASKET_EMPTY = By.CSS_SELECTOR, '#content_inner p'