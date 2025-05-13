import pytest
from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage
from ..pages.basket_page import BasketPage
from ..pages.locators import BasketPageLocators
from ..pages.links import MainPageLinks


class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MainPageLinks.PRODUCT_LINK)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MainPageLinks.MAIN_PAGE_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.is_empty(), 'Корзина не пустая'