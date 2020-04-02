from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click() 

    def product_should_be_added(self):
        self.should_be_success_message()
        self.should_be_product_name_in_message(self.get_product_name())
        self.should_be_price_message()
        self.should_be_correct_total_price_in_message(self.get_product_price())

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text        
        
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), "Basket price message is not presented"
        
    def should_be_product_name_in_message(self, product_name):
        assert product_name in self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, \
            f"Product name '{product_name}' not in the success message"
    
    def should_be_correct_total_price_in_message(self, product_price):
        assert product_price in self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text, \
            f"Product price '{product_price}' not in the basket price message"
        
    
