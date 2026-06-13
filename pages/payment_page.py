from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    """Page Object Model for Payment Page"""

    URL = "https://demo.fintech-app.com/payment"

    AMOUNT_FIELD       = (By.ID, "amount")
    ACCOUNT_NO_FIELD   = (By.ID, "accountNumber")
    IFSC_FIELD         = (By.ID, "ifscCode")
    SUBMIT_BUTTON      = (By.XPATH, "//button[contains(text(),'Submit Payment')]")
    SUCCESS_MESSAGE    = (By.CLASS_NAME, "success-msg")
    ERROR_MESSAGE      = (By.CLASS_NAME, "error-msg")
    TRANSACTION_ID     = (By.ID, "transactionId")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def enter_amount(self, amount):
        field = self.wait.until(EC.visibility_of_element_located(self.AMOUNT_FIELD))
        field.clear()
        field.send_keys(str(amount))

    def enter_account_number(self, account_no):
        field = self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_NO_FIELD))
        field.clear()
        field.send_keys(account_no)

    def enter_ifsc(self, ifsc):
        field = self.wait.until(EC.visibility_of_element_located(self.IFSC_FIELD))
        field.clear()
        field.send_keys(ifsc)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

    def get_transaction_id(self):
        return self.wait.until(EC.visibility_of_element_located(self.TRANSACTION_ID)).text
