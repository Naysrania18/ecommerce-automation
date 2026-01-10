from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    # Locators
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CANCEL_BTN = (By.ID, "cancel")
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def enter_shipping_info(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BTN)
    
    def complete_purchase(self):
        self.click(self.FINISH_BTN)
    
    def get_subtotal(self):
        return self.get_text(self.SUBTOTAL_LABEL)
    
    def get_total(self):
        return self.get_text(self.TOTAL_LABEL)
    
    def is_order_successful(self):
        return self.is_displayed(self.SUCCESS_MESSAGE)
    
    def get_success_message(self):
        if self.is_displayed(self.SUCCESS_MESSAGE):
            return self.get_text(self.SUCCESS_MESSAGE)
        return None