from playwright.sync_api import expect, Page
from pages.login import LoginPage
from pages.products import ProductsPage
from pages.cart import CartPage
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import CheckoutStepTwo
from pages.checkout_complete import CheckoutComplete


def test_checkout_flow(login_page: LoginPage,
                       products_page: ProductsPage,
                       cart_page: CartPage,
                       checkout_step_one: CheckoutStepOne,
                       checkout_step_two: CheckoutStepTwo,
                       checkout_complete: CheckoutComplete):

    # go to SauceDemo
    login_page.load()

    # log into the website
    login_page.login("standard_user", "secret_sauce")
    expect(products_page.shopping_cart).to_be_visible()

    # Add any product to the cart
    products_page.add_product_to_cart("Sauce Labs Onesie")

    # Go to the cart and check whether the product is in the cart
    products_page.go_to_cart()
    expect(cart_page.product_in_cart("Sauce Labs Onesie")).to_be_visible()

    # proceed to the checkout
    cart_page.proceed_to_checkout()

    # fill in first name, last name and postal code (can use dummy values)
    checkout_step_one.enter_information("Test", "Person", "1000AA")
    checkout_step_one.proceed_to_purchase_overview()
    expect(checkout_step_two.summary_info).to_be_visible()

    # verify the item being purchased
    expect(checkout_step_two.product_in_cart("Sauce Labs Onesie")).to_be_visible()

    # complete the purchase
    checkout_step_two.finish_checkout()

    # verify that the order has been successfully placed (check confirmation message (expect))
    expect(checkout_complete.title_header).to_have_text("Checkout: Complete!")