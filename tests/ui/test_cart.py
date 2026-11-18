import pytest
from playwright.sync_api import expect
from tests.conftest import BACKPACK, BIKE_LIGHT


@pytest.mark.smoke
def test_add_item_updates_cart_badge(logged_in, inventory_page):
    inventory_page.add_to_cart(BACKPACK)
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_add_two_items_then_remove_one(logged_in, inventory_page):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.add_to_cart(BIKE_LIGHT)
    expect(inventory_page.cart_badge).to_have_text("2")
    inventory_page.remove_from_cart(BACKPACK)
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_cart_page_lists_added_item(logged_in, inventory_page, cart_page):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()
    assert cart_page.items.count() == 1
    expect(cart_page.item_names).to_have_text("Sauce Labs Backpack")


@pytest.mark.regression
def test_sort_price_low_to_high(logged_in, inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.price_values()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_sort_name_z_to_a(logged_in, inventory_page):
    inventory_page.sort_by("za")
    names = inventory_page.names.all_inner_texts()
    assert names == sorted(names, reverse=True)
