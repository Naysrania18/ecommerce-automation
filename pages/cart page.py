from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")
    
    def get_item_count(self):
        return len(self.find_elements(self.CART_ITEMS))
    
    def get_item_names(self):
        return [item.text for item in self.find_elements(self.ITEM_NAMES)]
    
    def get_item_prices(self):
        return [price.text for price in self.find_elements(self.ITEM_PRICES)]
    
    def remove_item(self, item_index=0):
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if buttons:
            buttons[item_index].click()
    
    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)
    
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)