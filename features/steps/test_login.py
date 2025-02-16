import pytest
from pytest_bdd import scenario
from pytest_bdd import given
from pytest_bdd import when
from pytest_bdd import then

from meant4_qa_eng_test.ap_pom import LOGIN_PAGE
from meant4_qa_eng_test.ap_pom import LOGIN_BUTTON


@scenario('login.feature', 'Logging in')
def test_publish():
    pass


@pytest.fixture(scope="session")
def login_info():
    return {}


@given("Browser is open on the login page")
def open_browser_and_page(browser):
    browser.visit(LOGIN_PAGE)


@given("I have an account")
def check_account(login_info):
    # having an account is a given for this test
    login_info["email"] = "spoofed@account.com"
    login_info["pswd"] = "pswd1234"
    return login_info


@when("I enter account name")
def enter_account_name(browser, login_info):
    browser.fill("email", login_info["email"])


@when("I enter password")
def enter_password(browser, login_info):
    browser.fill("passwd", login_info["pswd"])


@when("I press the 'log in' button")
def press_login(browser):
    button = browser.find_by_xpath(LOGIN_BUTTON)
    browser.click(button)


@then("I should be logged in")
def login_check():
    pass


@then("I shouldn't see an error message")
def check_no_error():
    pass
