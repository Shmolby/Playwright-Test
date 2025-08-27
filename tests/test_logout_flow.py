from playwright.sync_api import expect


def test_logout_flow(login_page,
                     products_page,
                     side_menu):

    # go to SauceDemo
    login_page.load()

    # log into the website
    login_page.login("standard_user", "secret_sauce")
    expect(products_page.shopping_cart).to_be_visible()

    # open the menu and log out
    side_menu.open_menu()
    side_menu.logout()

    # verify that you are redirected to the login page
    expect(login_page.login_button).to_be_visible()