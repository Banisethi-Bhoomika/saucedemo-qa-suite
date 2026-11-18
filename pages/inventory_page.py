from playwright.sync_api import Page, expect


class InventoryPage:
    """Page Object for the product listing page."""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")
        self.prices = page.locator(".inventory_item_price")
        self.names = page.locator(".inventory_item_name")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def expect_loaded(self):
        expect(self.title).to_have_text("Products")

    def add_to_cart(self, slug: str):
        self.page.locator(f"[data-test='add-to-cart-{slug}']").click()

    def remove_from_cart(self, slug: str):
        self.page.locator(f"[data-test='remove-{slug}']").click()

    def sort_by(self, value: str):
        """value: az, za, lohi, hilo"""
        self.sort_dropdown.select_option(value)

    def price_values(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
