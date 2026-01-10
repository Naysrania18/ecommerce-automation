import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.mark.products
class TestProducts:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        self.products_page = ProductsPage(driver)
        yield
    
    def test_product_count(self):
        count = self.products_page.get_product_count()
        assert count == 6
        print(f"✅ Found {count} products")
    
    def test_add_product_to_cart(self):
        initial_count = self.products_page.get_cart_count()
        self.products_page.add_product_to_cart(0)
        new_count = self.products_page.get_cart_count()
        assert new_count == initial_count + 1
        print(f"✅ Cart count: {initial_count} → {new_count}")
    
    def test_add_multiple_products(self):
        self.products_page.add_multiple_products(3)
        cart_count = self.products_page.get_cart_count()
        assert cart_count == 3
        print(f"✅ Added 3 products to cart")
    
    def test_sort_products(self):
        # Test A to Z sort
        self.products_page.sort_products("az")
        names = self.products_page.get_product_names()
        assert names == sorted(names)
        print(f"✅ Products sorted A-Z: {names}")
        
        # Test Z to A sort
        self.products_page.sort_products("za")
        names = self.products_page.get_product_names()
        assert names == sorted(names, reverse=True)
        print(f"✅ Products sorted Z-A: {names}")