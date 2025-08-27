from playwright.sync_api import expect, Page
from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage
from pages.checkout_step_one import CheckoutStepOne


def test_checkout_flow(page: Page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_step_one = CheckoutStepOne(page)

    # go to SauceDemo
    login_page.load()

    # log into the website
    login_page.login("standard_user", "secret_sauce")
    expect(products_page.shopping_cart).to_be_visible()

    # Add any product to the cart
    products_page.add_product_to_cart("Sauce Labs Onesie")

    # Proceed to checkout
    products_page.go_to_cart()
    assert cart_page.product_in_cart("Sauce Labs Onesie")

    cart_page.proceed_to_checkout()

    # fill in first name, last name and postal code (can use dummy values)
    checkout_step_one.enter_information("Test", "Person", "1000AA")
    checkout_step_one.proceed_to_purchase_overview()

    # complete the purchase
    # verify that the order has been successfully placed (check confirmation message (expect))