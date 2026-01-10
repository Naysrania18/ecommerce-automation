import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.cart
class TestCart:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(driver)
        self.cart_page = CartPage(driver)
        yield
    
    def test_add_items_and_verify_cart(self):
        # Add products
        self.products_page.add_multiple_products(2)
        
        # Go to cart
        self.products_page.go_to_cart()
        
        # Verify items in cart
        item_count = self.cart_page.get_item_count()
        item_names = self.cart_page.get_item_names()
        
        assert item_count == 2
        assert len(item_names) == 2
        print(f"✅ Cart has {item_count} items: {item_names}")
    
    def test_remove_item_from_cart(self):
        # Add products
        self.products_page.add_multiple_products(3)
        self.products_page.go_to_cart()
        
        # Remove one item
        initial_count = self.cart_page.get_item_count()
        self.cart_page.remove_item(0)
        
        # Verify removal
        new_count = self.cart_page.get_item_count()
        assert new_count == initial_count - 1
        print(f"✅ Item removed: {initial_count} → {new_count}")
    
    def test_continue_shopping(self):
        self.products_page.go_to_cart()
        self.cart_page.continue_shopping()
        assert "inventory" in self.driver.current_url
        print("✅ Continue shopping successful")
    
    def test_proceed_to_checkout(self):
        self.products_page.add_product_to_cart(0)
        self.products_page.go_to_cart()
        self.cart_page.proceed_to_checkout()
        assert "checkout" in self.driver.current_url
        print("✅ Proceed to checkout successful")