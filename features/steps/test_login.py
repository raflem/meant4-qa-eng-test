from pytest_bdd import scenario, given, when, then


@scenario('login.feature', 'Logging in')
def test_publish():
    pass


@given("Browser is open on the login page")
def open_browser_and_page():
    pass


@given("I have an account")
def check_account():
    pass  # ideally this is another prerequisite test or this function returns pre-made login info


@when("I enter account name")
def enter_account_name():
    pass


@when("I enter password")
def enter_password():
    pass


@when("I press the 'log in' button")
def press_login():
    pass


@then("I should be logged in")
def login_check():
    pass


@then("I shouldn't see an error message")
def check_no_error():
    pass
