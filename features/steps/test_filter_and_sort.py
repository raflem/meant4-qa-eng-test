import time

import pytest
from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when


@pytest.fixture(scope="function")
def default_state() -> dict:
    return {}


@pytest.fixture(scope="function")
def filtered_state() -> dict:
    return {}


@pytest.fixture(scope="function")
def sorted_state() -> dict:
    return {}


def save_state(browser, state):
    """Helper function"""
    visible_products = tuple(browser.find_by_css(".product-container"))
    visible_prices = tuple(browser.find_by_css(".price.product-price"))
    state["all_products"] = visible_products
    state["names"] = tuple(_.text.split("\n")[0] for _ in visible_products)
    state["prices"] = tuple(_.text for _ in visible_prices if _.text)


@scenario("filter_and_sort.feature", "Filter and sort")
def test_filter_and_sort(default_state, filtered_state, sorted_state):
    max_price = int(sorted_state["prices"][0].split("$")[-1])
    min_price = int(sorted_state["prices"][-1].split("$")[-1])
    filtered_summer_dresses = tuple("Summer" in _ or "Chiffon" in _ for _ in filtered_state["names"])
    assert max_price > min_price
    assert all(filtered_summer_dresses)



@given("The shop site is open")
def open_shop_site(browser):
    browser.visit("http://www.automationpractice.pl/index.php?id_category=8&controller=category")


@given("Default filters and sorting are enabled")
def save_default_state(browser, default_state):
    visible_products = tuple(browser.find_by_css(".product-container"))
    visible_prices = tuple(browser.find_by_css(".price.product-price"))
    default_state["all_products"] = visible_products
    default_state["names"] = tuple(_.text.split("\n")[0] for _ in visible_products)
    default_state["prices"] = tuple(_.text for _ in visible_prices if _.text)


@when("I enable a dress type filter")
def enable_filters(browser, filtered_state):
    browser.find_by_id("layered_category_11").click()
    time.sleep(1.5)  # force wait to avoid staleness
    visible_products = tuple(browser.find_by_css(".product-container"))
    visible_prices = tuple(browser.find_by_css(".price.product-price"))
    filtered_state["all_products"] = visible_products
    filtered_state["names"] = tuple(_.text.split("\n")[0] for _ in visible_products)
    filtered_state["prices"] = tuple(_.text for _ in visible_prices if _.text)


@when("Change sorting to price descending")
def change_sorting(browser, sorted_state):
    browser.find_by_id("selectProductSort").select("price:desc")
    time.sleep(1.5)  # force wait to avoid staleness
    visible_products = tuple(browser.find_by_css(".product-container"))
    visible_prices = tuple(browser.find_by_css(".price.product-price"))
    sorted_state["all_products"] = visible_products
    sorted_state["names"] = tuple(_.text.split("\n")[0] for _ in visible_products)
    sorted_state["prices"] = tuple(_.text for _ in visible_prices if _.text)


@then("One dress type is shown")
def items_filtered(default_state, filtered_state):
    assert len(filtered_state["all_products"]) < len(default_state["all_products"])


@then("Prices are sorted high to low")
def items_sorted(default_state, sorted_state):
    assert sorted_state != default_state
