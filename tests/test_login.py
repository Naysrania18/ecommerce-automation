import pytest

class TestLogin:
    def test_valid_login(self, driver):
        driver.get("https://example.com")
        assert "Example" in driver.title