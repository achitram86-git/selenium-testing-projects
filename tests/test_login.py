import pytest
from pages.login_page import LoginPage

class TestLogin:
    """Test cases for Login functionality - Fintech Application"""

    def test_valid_login(self, driver):
        """TC_LOGIN_001: Verify successful login with valid credentials"""
        page = LoginPage(driver)
        page.open()
        page.enter_username("admin@finsurge.com")
        page.enter_password("Admin@123")
        page.click_login()
        assert page.is_dashboard_visible(), "Dashboard should be visible after valid login"

    def test_invalid_username(self, driver):
        """TC_LOGIN_002: Verify error message with invalid username"""
        page = LoginPage(driver)
        page.open()
        page.enter_username("wronguser@finsurge.com")
        page.enter_password("Admin@123")
        page.click_login()
        error = page.get_error_message()
        assert "Invalid credentials" in error

    def test_invalid_password(self, driver):
        """TC_LOGIN_003: Verify error message with invalid password"""
        page = LoginPage(driver)
        page.open()
        page.enter_username("admin@finsurge.com")
        page.enter_password("wrongpassword")
        page.click_login()
        error = page.get_error_message()
        assert "Invalid credentials" in error

    def test_empty_username(self, driver):
        """TC_LOGIN_004: Verify validation when username is empty"""
        page = LoginPage(driver)
        page.open()
        page.enter_username("")
        page.enter_password("Admin@123")
        page.click_login()
        error = page.get_error_message()
        assert "required" in error.lower()

    def test_empty_password(self, driver):
        """TC_LOGIN_005: Verify validation when password is empty"""
        page = LoginPage(driver)
        page.open()
        page.enter_username("admin@finsurge.com")
        page.enter_password("")
        page.click_login()
        error = page.get_error_message()
        assert "required" in error.lower()

    def test_empty_credentials(self, driver):
        """TC_LOGIN_006: Verify validation when both fields are empty"""
        page = LoginPage(driver)
        page.open()
        page.enter_username("")
        page.enter_password("")
        page.click_login()
        error = page.get_error_message()
        assert error is not None
