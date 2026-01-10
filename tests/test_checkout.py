import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.checkout
class TestCheckout:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        yield
    
    def test_complete_checkout_flow(self):
        # Add product and go to cart
        self.products_page.add_product_to_cart(0)
        self.products_page.go_to_cart()
        self.cart_page.proceed_to_checkout()
        
        # Enter shipping info
        self.checkout_page.enter_shipping_info("John", "Doe", "12345")
        
        # Complete purchase
        self.checkout_page.complete_purchase()
        
        # Verify success
        assert self.checkout_page.is_order_successful()
        success_msg = self.checkout_page.get_success_message()
        assert "Thank you for your order" in success_msg
        print(f"✅ Order successful: {success_msg}")
    
    def test_checkout_without_info(self):
        self.products_page.add_product_to_cart(0)
        self.products_page.go_to_cart()
        self.cart_page.proceed_to_checkout()
        
        # Try to continue without info
        self.checkout_page.click(self.checkout_page.CONTINUE_BTN)
        
        # Should show error
        assert self.checkout_page.is_displayed(self.checkout_page.ERROR_MESSAGE)
        print("✅ Error shown for missing info")
    
    def test_order_summary(self):
        # Add expensive product
        self.products_page.add_product_to_cart(0)
        self.products_page.go_to_cart()
        self.cart_page.proceed_to_checkout()
        
        # Enter info and check summary
        self.checkout_page.enter_shipping_info("John", "Doe", "12345")
        
        subtotal = self.checkout_page.get_subtotal()
        total = self.checkout_page.get_total()
        
        assert "Item total" in subtotal
        assert "Total" in total
        print(f"✅ Order summary: {subtotal}, {total}")