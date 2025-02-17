from random import randint

import pytest
from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when
from random_word import RandomWords

from meant4_qa_eng_test.ap_pom import ALERT_DANGER_CSS
from meant4_qa_eng_test.ap_pom import CREATE_FNAME_NAME
from meant4_qa_eng_test.ap_pom import CREATE_LNAME_NAME
from meant4_qa_eng_test.ap_pom import EMAIL_CREATE_NAME
from meant4_qa_eng_test.ap_pom import LOGIN_PAGE_HREF
from meant4_qa_eng_test.ap_pom import PSWD_LOGIN_NAME
from meant4_qa_eng_test.ap_pom import REGISTER_ACCOUNT_NAME
from meant4_qa_eng_test.ap_pom import SUBMIT_CREATE_NAME


@scenario('register.feature', 'Registering new account')
def test_register(browser):
    assert browser.is_text_present("Your account has been created.", wait_time=10)


@pytest.fixture(scope="session")
def register_info() -> dict:
    return {}  # ideally this session-scoped fixture is re-used in test_login


@given("Browser is open on the Sign In page")
def open_browser_and_page(browser):
    browser.visit(LOGIN_PAGE_HREF)


@given("I don't have an account registered")
def create_register_info(register_info):
    r = RandomWords()
    name = r.get_random_word()
    domain = r.get_random_word()
    register_info["name"] = name
    register_info["surname"] = domain
    register_info["email"] = f"{name}@{domain}.com"
    register_info["pswd"] = f"{r.get_random_word()}{randint(1000, 9999)}"
    return register_info


@when("I enter an unregistered email address")
def enter_account_name(browser, register_info):
    browser.fill(EMAIL_CREATE_NAME, register_info["email"])


@when("Click the Create Account button")
def click_create(browser):
    submit_create_btn = browser.find_by_name(SUBMIT_CREATE_NAME)
    submit_create_btn.click()


@when("Provide required information")
def provide_info(browser, register_info):
    browser.fill(CREATE_FNAME_NAME, register_info["name"])
    browser.fill(CREATE_LNAME_NAME, register_info["surname"])
    browser.fill(PSWD_LOGIN_NAME, register_info["pswd"])


@when("Confirm form submission")
def confirm_register(browser):
    register_btn = browser.find_by_name(REGISTER_ACCOUNT_NAME)
    register_btn.click()


@then("An account is created")
def check_account_created(browser):
    browser.find_by_css(".alert.alert-success")


@then("I shouldn't see an error message")
def check_no_error(browser):
    error = browser.find_by_css(ALERT_DANGER_CSS)
    assert not error
