from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, '[data-test="username"]')
        self.password_input = (By.CSS_SELECTOR, '[data-test="password"]')
        self.login_button = (By.CSS_SELECTOR, '[data-test="login-button"]')

    def login(self, username, password, url, timeout=2):
        self.driver.get(url)
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.login_button)).click()