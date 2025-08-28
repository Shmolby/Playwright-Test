from playwright.sync_api import expect


def test_checkout_flow(login_page,
                       products_page,
                       cart_page,
                       checkout_step_one,
                       checkout_step_two,
                       checkout_complete,
                       side_menu):

    # go to SauceDemo
    login_page.load()

    # log into the website
    login_page.login("standard_user", "secret_sauce")
    expect(side_menu.open_menu_button).to_be_visible()

    # Add any product to the cart
    products_page.add_product_to_cart("Sauce Labs Onesie")

    # Go to the cart and check whether the product is in the cart
    products_page.go_to_cart()
    expect(cart_page.product_in_cart("Sauce Labs Onesie")).to_be_visible()

    # proceed to the checkout
    cart_page.proceed_to_checkout()

    # fill in first name, last name and postal code
    checkout_step_one.enter_information("Test", "Person", "1000AA")
    checkout_step_one.proceed_to_purchase_overview()

    # verify the item being purchased
    expect(checkout_step_two.product_in_cart("Sauce Labs Onesie")).to_be_visible()

    # complete the purchase
    checkout_step_two.finish_checkout()

    # verify that the order has been successfully placed
    expect(checkout_complete.title_header).to_have_text("Checkout: Complete!")
    expect(checkout_complete.complete_text).to_have_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")
