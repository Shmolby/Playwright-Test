from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/cart.html"
        self.cart_item_name = page.locator("xpath=//div[@data-test='inventory-item-name']")
        self.checkout_button = page.locator("xpath=//button[@data-test='checkout']")

    def load(self):
        self.page.goto(self.url)

    def product_in_cart(self, product: str):
        cart_products = [item.text_content() for item in self.cart_item_name.all()]
        return product in cart_products

    def proceed_to_checkout(self):
        self.checkout_button.click()
