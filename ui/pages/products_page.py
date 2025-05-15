from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
        self.add_to_cart_button = (By.CSS_SELECTOR, '[class*="btn btn_primary btn_small btn_inventory"]')
        self.cart_badge = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')        

    def get_inventory_items(self, timeout=2):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.inventory_items))
        return self.driver.find_elements(*self.inventory_items)

    def add_first_item_to_cart(self, timeout=5):
        items = self.get_inventory_items()
        first_item = items[0]
        add_to_cart_button = first_item.find_element(*self.add_to_cart_button)
        # Using JavaScript click to ensure reliability — Selenium click sometimes fails due to layout shifts or overlays
        self.driver.execute_script("arguments[0].click();", add_to_cart_button) 

    def get_cart_badge_count(self, timeout=2):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.cart_badge))
        return int(self.driver.find_element(*self.cart_badge).text)
