from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when

from meant4_qa_eng_test.ap_pom import ALERT_DANGER_CSS
from meant4_qa_eng_test.ap_pom import CREATE_FNAME_NAME
from meant4_qa_eng_test.ap_pom import CREATE_LNAME_NAME
from meant4_qa_eng_test.ap_pom import EMAIL_CREATE_NAME
from meant4_qa_eng_test.ap_pom import EMAIL_LOGIN_NAME
from meant4_qa_eng_test.ap_pom import LOGIN_PAGE_HREF
from meant4_qa_eng_test.ap_pom import PSWD_LOGIN_NAME
from meant4_qa_eng_test.ap_pom import REGISTER_ACCOUNT_NAME
from meant4_qa_eng_test.ap_pom import SUBMIT_CREATE_NAME
from meant4_qa_eng_test.ap_pom import SUBMIT_LOGIN_NAME


@scenario("login.feature", "Logging in")
def test_login(browser):
    assert browser.is_text_present("Welcome to your account", wait_time=10)


@given("Browser is open on the Sign In page")
def open_browser_and_page(browser):
    browser.visit(LOGIN_PAGE_HREF)


@given("I have an account")
def create_account_and_log_out(browser, user_info):
    browser.fill(EMAIL_CREATE_NAME, user_info["email"])
    submit_create_btn = browser.find_by_name(SUBMIT_CREATE_NAME)
    submit_create_btn.click()
    browser.fill(CREATE_FNAME_NAME, user_info["name"])
    browser.fill(CREATE_LNAME_NAME, user_info["surname"])
    browser.fill(PSWD_LOGIN_NAME, user_info["pswd"])
    register_btn = browser.find_by_name(REGISTER_ACCOUNT_NAME)
    register_btn.click()
    browser.find_by_css(".logout").click()


@when("I enter account name")
def enter_account_name(browser, user_info):
    browser.fill(EMAIL_LOGIN_NAME, user_info["email"])


@when("I enter password")
def enter_password(browser, user_info):
    browser.fill(PSWD_LOGIN_NAME, user_info["pswd"])


@when("I press the 'log in' button")
def press_login(browser):
    button = browser.find_by_name(SUBMIT_LOGIN_NAME)
    button.click()


@then("I should be logged in")
def login_check(browser):
    assert browser.is_text_present("Welcome to your account", wait_time=10)


@then("I shouldn't see an error message")
def check_no_error(browser):
    error = browser.find_by_css(ALERT_DANGER_CSS)
    assert not error
