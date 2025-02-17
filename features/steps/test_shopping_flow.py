import pytest
from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when

from meant4_qa_eng_test.ap_pom import ALERT_DANGER_CSS
from meant4_qa_eng_test.ap_pom import ALERT_SUCCESS_CSS
from meant4_qa_eng_test.ap_pom import AVAILABLE_DIF_CSS
from meant4_qa_eng_test.ap_pom import CREATE_FNAME_NAME
from meant4_qa_eng_test.ap_pom import CREATE_LNAME_NAME
from meant4_qa_eng_test.ap_pom import DRESSES_XPATH
from meant4_qa_eng_test.ap_pom import EMAIL_CREATE_NAME
from meant4_qa_eng_test.ap_pom import EMPTY_CART_XPATH
from meant4_qa_eng_test.ap_pom import HOME_PAGE_HREF
from meant4_qa_eng_test.ap_pom import LOGIN_PAGE_HREF
from meant4_qa_eng_test.ap_pom import PSWD_LOGIN_NAME
from meant4_qa_eng_test.ap_pom import REGISTER_ACCOUNT_NAME
from meant4_qa_eng_test.ap_pom import SUBMIT_CREATE_NAME


@scenario("shopping_flow.feature", "Shopping flow")
def test_shopping_flow(browser):
    assert browser.find_by_text("Your order on My Shop is complete.")


@pytest.fixture(scope="function")
def register_and_sign_in(browser, user_info):
    """
    Factory fixture wrapping the registering process.

    :param browser: pytest-splinter's browser fixture
    :param user_info: registration info fixture
    :return: registration and sign in function
    """

    def _register_and_sign_in():
        browser.visit(LOGIN_PAGE_HREF)
        browser.fill(EMAIL_CREATE_NAME, user_info["email"])
        submit_create_btn = browser.find_by_name(SUBMIT_CREATE_NAME)
        submit_create_btn.click()
        browser.fill(CREATE_FNAME_NAME, user_info["name"])
        browser.fill(CREATE_LNAME_NAME, user_info["surname"])
        browser.fill(PSWD_LOGIN_NAME, user_info["pswd"])
        register_btn = browser.find_by_name(REGISTER_ACCOUNT_NAME)
        register_btn.click()
        browser.find_by_css(".alert.alert-success")

    return _register_and_sign_in


@given("I am registered and signed in")
def open_browser_and_register(browser, register_and_sign_in):
    browser.visit(LOGIN_PAGE_HREF)
    register_and_sign_in()
    browser.visit(HOME_PAGE_HREF)


@given("Browser is open on the shop page")
def open_shop_page(browser):
    dresses_btn = browser.find_by_xpath(DRESSES_XPATH)[-1]
    dresses_btn.click()


@given("Shopping cart is empty")
def check_empty_cart(browser):
    assert browser.find_by_xpath(EMPTY_CART_XPATH)


@given("Items are available")
def check_item_availability(browser):
    available_items = browser.find_by_css(AVAILABLE_DIF_CSS)
    assert available_items, "Found no items are available for sale!"


@when("I add an item to the cart")
def add_item_to_cart(browser):
    # browser.find_by_css(".product-container")[-1].click()  # BUG?: performs as hover not as click
    # browser.find_by_id("View").click()  # WARN: doesn't work despite elements being visible!
    browser.visit(
        "http://www.automationpractice.pl/index.php?id_product=7&controller=product#/16-color-yellow/2-size-m"
    )  # bruteforce to an available item
    browser.find_by_text("Add to cart").click()


@when("Proceed to checkout")
def go_to_checkout(browser):
    browser.find_by_css(".btn.btn-default.button.button-medium").click()
    browser.find_by_text("Proceed to checkout").click()


@when("Provide a delivery address")
def enter_delivery_info(browser, user_info):
    browser.fill("address1", user_info["address"])
    browser.fill("city", user_info["city"])
    browser.find_by_id("id_state").select(user_info["state"])
    browser.fill("postcode", user_info["zip"])
    browser.fill("phone", user_info["phone"])
    # browser.find_by_id("phone_mobile").click()  # click elsewhere to save the phone no.
    browser.find_by_id("submitAddress").click()


@when("Select a shipping option")
def select_shipping(browser):
    # default shipping is OK
    browser.find_by_text("Proceed to checkout").click()


@when("Accept the ToS")
def accept_tos(browser):
    browser.find_by_id("cgv").click()
    browser.find_by_css(
        ".button.btn.btn-default.standard-checkout.button-medium"
    ).click()


@when("Select a payment option")
def select_payment(browser):
    browser.find_by_css(".bankwire").click()


@when("Confirm the transaction")
def confirm_order(browser):
    browser.find_by_text("I confirm my order").click()


@then("An order is placed")
def check_order_placed(browser):
    assert browser.find_by_css(ALERT_SUCCESS_CSS)


@then("I shouldn't see an error message")
def check_no_error(browser):
    error = browser.find_by_css(ALERT_DANGER_CSS)
    assert not error
