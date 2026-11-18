import pytest
from playwright.sync_api import expect
from tests.conftest import BACKPACK


def go_to_checkout_form(inventory_page, cart_page):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()
    cart_page.start_checkout()


@pytest.mark.smoke
def test_complete_purchase_happy_path(logged_in, inventory_page, cart_page, checkout_page):
    go_to_checkout_form(inventory_page, cart_page)
    checkout_page.fill_details("Asha", "Rao", "110001")
    checkout_page.finish()
    checkout_page.expect_order_complete()


@pytest.mark.regression
def test_order_summary_shows_item_total(logged_in, inventory_page, cart_page, checkout_page):
    go_to_checkout_form(inventory_page, cart_page)
    checkout_page.fill_details("Asha", "Rao", "110001")
    expect(checkout_page.subtotal).to_contain_text("$29.99")


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize(
    "first, last, postal, message",
    [
        ("", "Rao", "110001", "First Name is required"),
        ("Asha", "", "110001", "Last Name is required"),
        ("Asha", "Rao", "", "Postal Code is required"),
    ],
    ids=["no-first-name", "no-last-name", "no-postal-code"],
)
def test_checkout_form_validation(
    logged_in, inventory_page, cart_page, checkout_page, first, last, postal, message
):
    go_to_checkout_form(inventory_page, cart_page)
    checkout_page.fill_details(first, last, postal)
    expect(checkout_page.error).to_contain_text(message)
