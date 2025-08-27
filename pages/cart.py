from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/cart.html"
        self.checkout_button = page.locator("xpath=//button[@data-test='checkout']")

    def load(self):
        self.page.goto(self.url)

    def product_in_cart(self, product: str):
        return self.page.locator(f"xpath=//div[@data-test='inventory-item-name' and text() = '{product}']")

    def proceed_to_checkout(self):
        self.checkout_button.click()
