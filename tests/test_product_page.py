from ..pages.product_page import ProductPage
from ..pages.basket_page import BasketPage
from ..pages.login_page import LoginPage
from ..pages.locators import ProductPageLocators
import pytest, time

LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'

@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", str(time.time()))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE_BASKET), \
            'Сообщения про новую стоимость корзины не появилось'

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.add_to_basket()
        #time.sleep(30)
        #page.solve_quiz_and_get_code()
        #print(page.take_product_name())
        #print(page.take_product_name_in_basket())
        assert page.take_product_name() == page.take_product_name_in_basket(), 'Имя не совпадает'
        assert page.take_product_price() == page.take_product_price_in_basket(), 'Стоимость не совпадает'

def test_guest_cant_see_success_message(self, browser):
    page = ProductPage(browser, LINK)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE_BASKET), \
        'Сообщения про новую стоимость корзины не появилось'

def test_guest_can_add_product_to_basket(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    assert page.take_product_name() == page.take_product_name_in_basket(), 'Имя не совпадает'
    assert page.take_product_price() == page.take_product_price_in_basket(), 'Стоимость не совпадает'

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.PRODUCT_PRICE_BASKET),\
        'Сообщения про новую стоимость корзины не появилось'

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.PRODUCT_PRICE_BASKET),\
        'Сообщение об успехе не пропало'

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.is_empty(), 'Корзина не пустая'