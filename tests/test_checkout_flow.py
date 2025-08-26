from playwright.sync_api import Page, Expect
from pages.login import LoginPage


def test_checkout_flow(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    # go to saucedemo
    login_page.load()

    # log into the website
    login_page.login("standard_user", "secret_sauce")

    # Add any product to the cart

    # Proceed to checkout
    # fill in first name, last name and postal code (can use dummy values)
    # complete the purchase
    # verify that the order has been successfully placed (check confirmation message (expect))