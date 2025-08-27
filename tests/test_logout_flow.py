from playwright.sync_api import expect
from pages.login import LoginPage
from pages.side_menu import SideMenu
from pages.products import ProductsPage


def test_logout_flow(login_page: LoginPage,
                     products_page: ProductsPage,
                     side_menu: SideMenu):

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