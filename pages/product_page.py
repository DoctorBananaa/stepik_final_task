from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET_BTN).click()

    def take_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def take_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def take_product_name_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text

    def take_product_price_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text

    def go_to_basket(self):
        selector_type, selector_str = ProductPageLocators.BASKET_LINK
        selector_str = selector_str.format(self.get_current_language())
        self.browser.find_element(selector_type, selector_str).click()