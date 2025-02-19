from selenium.webdriver.common.by import By


class MainPageLocators:
    #LOGIN_LINK = By.CSS_SELECTOR, "#registration_link"
    pass

class LoginPageLocators:
    LOGIN_FORM = By.ID, 'login_form'
    REGISTER_FORM = By.ID, 'register_form'

class ProductPageLocators:
    ADD_BASKET_BTN = By.CLASS_NAME, 'btn-add-to-basket'
    PRODUCT_NAME = By.CSS_SELECTOR, '.product_main > h1'
    PRODUCT_PRICE = By.CSS_SELECTOR, '.product_main > p'
    PRODUCT_NAME_BASKET = By.CSS_SELECTOR, '#messages .alert-noicon:nth-child(1) strong'
    PRODUCT_PRICE_BASKET = By.CSS_SELECTOR, '#messages .alert-noicon:nth-child(3) strong'

class BasePageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, "#login_link"
    LOGIN_LINK_INVALID = By.CSS_SELECTOR, "#login_link_inc"