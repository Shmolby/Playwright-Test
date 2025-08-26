from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/cart.html"
        self.cart_items = page.locator("xpath=//div[@data-test='inventory-item']")
