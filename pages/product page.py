from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    
    def get_product_count(self):
        return len(self.find_elements(self.PRODUCT_NAMES))
    
    def get_product_names(self):
        return [product.text for product in self.find_elements(self.PRODUCT_NAMES)]
    
    def get_product_prices(self):
        return [price.text for price in self.find_elements(self.PRODUCT_PRICES)]
    
    def add_product_to_cart(self, product_index=0):
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        buttons[product_index].click()
    
    def add_multiple_products(self, count=3):
        for i in range(min(count, 6)):
            self.add_product_to_cart(i)
    
    def get_cart_count(self):
        if self.is_displayed(self.SHOPPING_CART_BADGE):
            return int(self.get_text(self.SHOPPING_CART_BADGE))
        return 0
    
    def go_to_cart(self):
        self.click(self.SHOPPING_CART_LINK)
    
    def sort_products(self, sort_by="az"):
        from selenium.webdriver.support.ui import Select
        dropdown = Select(self.find_element(self.SORT_DROPDOWN))
        dropdown.select_by_value(sort_by)
    
    def get_sort_options(self):
        from selenium.webdriver.support.ui import Select
        dropdown = Select(self.find_element(self.SORT_DROPDOWN))
        return [option.text for option in dropdown.options]