import pytest
from pages.login_page import LoginPage

@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url
        print("✅ Login successful")
    
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("invalid_user", "wrong_password")
        error_message = login_page.get_error_message()
        assert error_message is not None
        assert "Epic sadface" in error_message
        print(f"✅ Error message shown: {error_message}")
    
    def test_locked_user(self, driver):
        login_page = LoginPage(driver)
        login_page.login("locked_out_user", "secret_sauce")
        error_message = login_page.get_error_message()
        assert "locked out" in error_message.lower()
        print(f"✅ Locked user error: {error_message}")

    def test_empty_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("", "")
        error_message = login_page.get_error_message()
        assert error_message is not None
        print(f"✅ Empty login error: {error_message}")
