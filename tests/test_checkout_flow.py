from playwright.sync_api import expect, Page
from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage


def test_checkout_flow(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    # go to SauceDemo
    login_page.load()

    # log into the website
    login_page.login("standard_user", "secret_sauce")
    expect(products_page.shopping_cart).to_be_visible()

    # Add any product to the cart
    products_page.add_product_to_cart("Sauce Labs Onesie")

    # Proceed to checkout
    products_page.go_to_checkout()
    expect()

    # fill in first name, last name and postal code (can use dummy values)
    # complete the purchase
    # verify that the order has been successfully placed (check confirmation message (expect))