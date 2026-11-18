import pytest
from playwright.sync_api import expect
from tests.conftest import VALID_USER, VALID_PASSWORD


@pytest.mark.smoke
def test_valid_login_shows_products(login_page, inventory_page):
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)
    inventory_page.expect_loaded()
    assert inventory_page.items.count() == 6


@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.parametrize(
    "user, pwd, message",
    [
        ("locked_out_user", VALID_PASSWORD, "this user has been locked out"),
        (VALID_USER, "wrong_password", "do not match any user"),
        ("", VALID_PASSWORD, "Username is required"),
        (VALID_USER, "", "Password is required"),
        ("", "", "Username is required"),
    ],
    ids=["locked-out", "wrong-password", "no-username", "no-password", "both-empty"],
)
def test_invalid_login_shows_error(login_page, user, pwd, message):
    login_page.open()
    login_page.login(user, pwd)
    login_page.expect_error(message)


@pytest.mark.regression
def test_logout_returns_to_login(logged_in, inventory_page, login_page):
    inventory_page.logout()
    expect(login_page.login_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.negative
def test_inventory_blocked_without_login(page, login_page):
    page.goto("/inventory.html")
    login_page.expect_error("You can only access '/inventory.html' when you are logged in")
