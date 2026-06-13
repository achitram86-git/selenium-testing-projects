import pytest
from pages.payment_page import PaymentPage

class TestPayment:
    """Test cases for Payment functionality - Fintech Application"""

    def test_valid_payment(self, driver):
        """TC_PAY_001: Verify successful payment with valid details"""
        page = PaymentPage(driver)
        page.open()
        page.enter_amount(1000)
        page.enter_account_number("1234567890")
        page.enter_ifsc("HDFC0001234")
        page.click_submit()
        assert "Payment Successful" in page.get_success_message()

    def test_payment_transaction_id_generated(self, driver):
        """TC_PAY_002: Verify transaction ID is generated after payment"""
        page = PaymentPage(driver)
        page.open()
        page.enter_amount(500)
        page.enter_account_number("9876543210")
        page.enter_ifsc("ICIC0005678")
        page.click_submit()
        assert page.get_transaction_id() != ""

    def test_zero_amount_payment(self, driver):
        """TC_PAY_003: Verify error when payment amount is zero"""
        page = PaymentPage(driver)
        page.open()
        page.enter_amount(0)
        page.enter_account_number("1234567890")
        page.enter_ifsc("HDFC0001234")
        page.click_submit()
        error = page.get_error_message()
        assert "Invalid amount" in error or "greater than zero" in error.lower()

    def test_negative_amount_payment(self, driver):
        """TC_PAY_004: Verify error when payment amount is negative"""
        page = PaymentPage(driver)
        page.open()
        page.enter_amount(-100)
        page.enter_account_number("1234567890")
        page.enter_ifsc("HDFC0001234")
        page.click_submit()
        assert page.get_error_message() is not None

    def test_invalid_account_number(self, driver):
        """TC_PAY_005: Verify error with invalid account number"""
        page = PaymentPage(driver)
        page.open()
        page.enter_amount(1000)
        page.enter_account_number("ABC123")
        page.enter_ifsc("HDFC0001234")
        page.click_submit()
        error = page.get_error_message()
        assert "Invalid account" in error or "numeric" in error.lower()

    def test_invalid_ifsc_code(self, driver):
        """TC_PAY_006: Verify error with invalid IFSC code"""
        page = PaymentPage(driver)
        page.open()
        page.enter_amount(1000)
        page.enter_account_number("1234567890")
        page.enter_ifsc("INVALID")
        page.click_submit()
        error = page.get_error_message()
        assert "Invalid IFSC" in error or "invalid" in error.lower()

    def test_empty_payment_fields(self, driver):
        """TC_PAY_007: Verify validation when all payment fields are empty"""
        page = PaymentPage(driver)
        page.open()
        page.click_submit()
        assert page.get_error_message() is not None
