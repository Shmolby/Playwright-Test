from playwright.sync_api import Page


class LoginPage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = Page
        self.username_field = page.locator("xpath=//input[@data-test='username']")
        self.password_field = page.locator("xpath=//input[@data-test='password']")
        self.login_button = page.locator("xpath=//input[@data-test='login-button']")

    def load(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()