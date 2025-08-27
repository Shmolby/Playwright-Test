from playwright.sync_api import Page


class CheckoutStepOne:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/checkout-step-one.html"
        self.first_name_field = self.page.locator("xpath=//input[@data-test='firstName']")
        self.last_name_field = self.page.locator("xpath=//input[@data-test='lastName']")
        self.postal_code_field = self.page.locator("xpath=//input[@data-test='postalCode']")
        self.continue_button = self.page.locator("xpath=//input[@data-test='continue']")

    def load(self):
        self.page.goto(self.url)

    def enter_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def proceed_to_purchase_overview(self):
        self.continue_button.click()