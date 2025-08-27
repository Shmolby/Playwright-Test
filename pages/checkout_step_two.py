from playwright.sync_api import Page


class CheckoutStepTwo:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/checkout-step-two.html"
        self.finish_button = page.locator("xpath=//button[@data-test='finish']")
        self.cart_item_name = page.locator("xpath=//div[@data-test='inventory-item-name']")
        self.summary_info = page.locator("xpath=//div[@class='summary_info']")

    def load(self):
        self.page.goto(self.url)

    def product_in_cart(self, product):
        return self.page.locator(f"xpath=//div[@data-test='inventory-item-name' and text() = '{product}']")

    def finish_checkout(self):
        self.finish_button.click()
