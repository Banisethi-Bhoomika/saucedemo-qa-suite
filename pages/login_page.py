from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the SauceDemo login screen."""

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto("/")

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()

    def expect_error(self, text: str):
        expect(self.error).to_be_visible()
        expect(self.error).to_contain_text(text)
