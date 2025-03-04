from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when

from meant4_qa_eng_test.ap_pom import ALERT_DANGER_CSS
from meant4_qa_eng_test.ap_pom import CREATE_FNAME_NAME
from meant4_qa_eng_test.ap_pom import CREATE_LNAME_NAME
from meant4_qa_eng_test.ap_pom import EMAIL_CREATE_NAME
from meant4_qa_eng_test.ap_pom import LOGIN_PAGE_HREF
from meant4_qa_eng_test.ap_pom import PSWD_LOGIN_NAME
from meant4_qa_eng_test.ap_pom import REGISTER_ACCOUNT_NAME
from meant4_qa_eng_test.ap_pom import SUBMIT_CREATE_NAME


@scenario("register.feature", "Registering new account")
def test_register(function_browser):
    assert function_browser.is_text_present("Your account has been created.", wait_time=10)


@given("Browser is open on the Sign In page")
def open_browser_and_page(function_browser):
    function_browser.visit(LOGIN_PAGE_HREF)


@given("I don't have an account registered")
def check_registered():
    pass


@when("I enter an unregistered email address")
def enter_account_name(function_browser, user_info):
    function_browser.fill(EMAIL_CREATE_NAME, user_info["email"])


@when("Click the Create Account button")
def click_create(function_browser):
    submit_create_btn = function_browser.find_by_name(SUBMIT_CREATE_NAME)
    submit_create_btn.click()


@when("Provide required information")
def provide_info(function_browser, user_info):
    function_browser.fill(CREATE_FNAME_NAME, user_info["name"])
    function_browser.fill(CREATE_LNAME_NAME, user_info["surname"])
    function_browser.fill(PSWD_LOGIN_NAME, user_info["pswd"])


@when("Confirm form submission")
def confirm_register(function_browser):
    register_btn = function_browser.find_by_name(REGISTER_ACCOUNT_NAME)
    register_btn.click()


@then("An account is created")
def check_account_created(function_browser):
    function_browser.find_by_css(".alert.alert-success")


@then("I shouldn't see an error message")
def check_no_error(function_browser):
    error = function_browser.find_by_css(ALERT_DANGER_CSS)
    assert not error
