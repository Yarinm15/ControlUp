from ui.pages.login_page import LoginPage
from ui.pages.products_page import ProductPage
from ui.utils import config, constants

def test_inventory_items(driver):
    login_page = LoginPage(driver)
    login_page.login(config.USERNAME, config.PASSWORD, config.BASE_URL)

    product_page = ProductPage(driver)
    items = product_page.get_inventory_items()

    assert len(items) == constants.EXPECTED_INVENTORY_COUNT, \
        f"Expected {constants.EXPECTED_INVENTORY_COUNT} items, found {len(items)}"
