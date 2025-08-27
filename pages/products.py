from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory.html"
        self.inventory_item = page.locator("xpath=//div[@data-test='inventory-item-name']")
        self.shopping_cart = page.locator("xpath=//a[@data-test='shopping-cart-link']")

    def load(self):
        self.page.goto(self.url)

    def add_product_to_cart(self, product: str):
        self.page.locator(f"xpath=//div[@data-test='inventory-item-name' and text() = '{product}']//ancestor::div[@class = 'inventory_item_description']//button[text() = 'Add to cart']").click()

    def go_to_cart(self):
        self.shopping_cart.click()

