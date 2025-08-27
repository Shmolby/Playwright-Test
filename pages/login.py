from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.saucedemo.com/'
        self.username_field = page.locator("xpath=//input[@data-test='username']")
        self.password_field = page.locator("xpath=//input[@data-test='password']")
        self.login_button = page.locator("xpath=//input[@data-test='login-button']")

    def load(self):
        self.page.goto(self.url)

    def username_fill(self, username: str):
        self.username_field.fill(username)

    def password_fill(self, password: str):
        self.password_field.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.username_fill(username)
        self.password_fill(password)
        self.click_login_button()
