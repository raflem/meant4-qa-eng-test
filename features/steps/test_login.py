import pytest
from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when

from meant4_qa_eng_test.ap_pom import ALERT_CSS
from meant4_qa_eng_test.ap_pom import EMAIL_LOGIN_NAME
from meant4_qa_eng_test.ap_pom import LOGIN_PAGE
from meant4_qa_eng_test.ap_pom import PSWD_LOGIN_NAME
from meant4_qa_eng_test.ap_pom import SUBMIT_LOGIN_NAME


@scenario('login.feature', 'Logging in')
def test_login(browser):
    assert browser.is_text_present("Welcome to your account", wait_time=10)


@pytest.fixture(scope="session")
def login_info():
    return {}


@given("Browser is open on the Sign In page")
def open_browser_and_page(browser):
    browser.visit(LOGIN_PAGE)


@given("I have an account")
def check_account(login_info):
    login_info["email"] = "spoofed@account.com"  # ideally this is pulled from env vars or project secrets
    login_info["pswd"] = "pswd1234"
    return login_info


@when("I enter account name")
def enter_account_name(browser, login_info):
    browser.fill(EMAIL_LOGIN_NAME, login_info["email"])


@when("I enter password")
def enter_password(browser, login_info):
    browser.fill(PSWD_LOGIN_NAME, login_info["pswd"])


@when("I press the 'log in' button")
def press_login(browser):
    button = browser.find_by_name(SUBMIT_LOGIN_NAME)
    button.click()


@then("I should be logged in")
def login_check(browser):
    browser.is_text_present("Welcome to your account", wait_time=10)


@then("I shouldn't see an error message")
def check_no_error(browser):
    error = browser.find_by_css(ALERT_CSS)
    assert not error
