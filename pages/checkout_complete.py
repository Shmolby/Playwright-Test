from playwright.sync_api import Page


class CheckoutComplete:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/checkout-complete.html"
        self.home_button = page.locator("xpath=//button[@data-test='back-to-products']")
        self.title_header = page.locator("xpath=//div[@data-test='secondary-header']/span[@data-test='title']")

    def load(self):
        self.page.goto(self.url)

    def return_to_homepage(self):
        self.home_button.click()
