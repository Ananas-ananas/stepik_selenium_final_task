import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

promo_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)]

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
register_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
  
class TestGuestAddToBasketFromProductPage():  
    @pytest.mark.parametrize('link', promo_links) 
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()  
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.product_should_be_added()
        
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()  
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()  
        page.add_product_to_basket()
        page.should_not_be_success_message(wait=True)
        
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket_page()
    
class TestUserAddToBasketFromProductPage():
    @pytest.fixture
    def setup(self, browser):
        page = LoginPage(browser, register_link)
        page.open()
        email = "{}@fakemail.org".format(str(time.time()))
        password = '{}pass'.format(str(time.time()))
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()  
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()  
        page.add_product_to_basket()
        page.product_should_be_added()
        
    
    