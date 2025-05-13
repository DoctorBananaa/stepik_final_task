from ..pages.product_page import ProductPage
from ..pages.basket_page import BasketPage
from ..pages.login_page import LoginPage
from ..pages.locators import ProductPageLocators
from ..pages.links import ProductPageLinks
import pytest, time


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, ProductPageLinks.PRODUCT_LINK)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", str(time.time()))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
        page.open()
        page.product_dont_add_to_backet()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
        page.open()
        page.add_to_basket()
        page.is_product_add_correct()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
    page.open()
    page.product_dont_add_to_backet()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
    page.open()
    page.add_to_basket()
    page.is_product_add_correct()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
    page.open()
    page.add_to_basket()
    page.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE_BASKET)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
    page.open()
    page.add_to_basket()
    page.is_disappeared(*ProductPageLocators.PRODUCT_PRICE_BASKET)

def test_guest_should_see_login_link_on_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, ProductPageLinks.PRODUCT_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_empty()