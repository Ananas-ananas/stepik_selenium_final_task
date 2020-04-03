from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_page(self):
        self.should_have_no_products()
        self.should_have_text_about_emptyness()
  
    def should_have_text_about_emptyness(self):
        assert self.is_element_present(*BasketPageLocators.EMTPYNESS_TEXT), "Text about emptyness is not presented"
        
    def should_have_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), "Some products are in the basket"
        