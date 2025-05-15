from ui.pages.login_page import LoginPage
from ui.pages.products_page import ProductPage
from ui.utils import config, constants

def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login(config.USERNAME, config.PASSWORD, config.BASE_URL)

    product_page = ProductPage(driver)
    product_page.add_first_item_to_cart()

    assert product_page.get_cart_badge_count() == constants.EXPECTED_CART_BADGE_COUNT, \
        "Expected cart count to be 1"
