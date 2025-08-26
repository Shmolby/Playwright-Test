from playwright.sync_api import Page


class ProductsPage:

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.inventory_item = page.locator("xpath=//div[@data-test='inventory-item-name']")

    def load(self):
        self.page.goto(self.URL)

    def products(self) -> list[str]:
        self.inventory_item.wait_for()
        return self.inventory_item.all_text_contents()

    def add_product_to_cart(self, product: str):
        all_products = self.products()
        product_name = [item for item in all_products if (product.lower() == item.lower())]
        self.page.locator(f"xpath=//div[@data-test='inventory-item-name' and text() = '{product_name}']//ancestor::div[@class = 'inventory_item_description']//button[text() = 'Add to cart']").click()

    def go_to_checkout(self):
        self.page.locator("xpath=//")

