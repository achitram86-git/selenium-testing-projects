from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object Model for Login Page"""

    URL = "https://demo.fintech-app.com/login"

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON   = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE  = (By.CLASS_NAME, "error-message")
    DASHBOARD_HEADER = (By.XPATH, "//h1[contains(text(),'Dashboard')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

    def is_dashboard_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER))
            return True
        except:
            return False
