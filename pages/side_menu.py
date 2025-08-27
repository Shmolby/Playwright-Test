from playwright.sync_api import Page


class SideMenu:

    def __init__(self, page: Page):
        self.page = page
        self.open_menu_button = page.locator("xpath=//div[@class='bm-burger-button']/button[text() = 'Open Menu']")
        self.close_menu_button = page.locator("xpath=//div[@class='bm-cross-button']/button[text() = 'Close Menu']")
        self.logout_link = page.locator("xpath=//a[@data-test='logout-sidebar-link']")

    def open_menu(self):
        self.open_menu_button.click()

    def close_menu(self):
        self.close_menu_button.click()

    def logout(self):
        self.logout_link.click()