from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_to_basket(self):
        selector_type, selector_str = MainPageLocators.BASKET_LINK
        selector_str = selector_str.format(self.get_current_language())
        self.browser.find_element(selector_type, selector_str).click()