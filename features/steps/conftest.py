from random import randint

import pytest
from random_word import RandomWords
from splinter import Browser


@pytest.fixture(scope="function")
def function_browser(splinter_webdriver):
    """
    Function-scoped browser fixture to ensure fresh env per test.

    :param splinter_webdriver: webdriver to use, configured in pyproject toml or in command line
    :yields: splinter.Browser instance configured with `splinter_webdriver` setting
    """
    browser = Browser(splinter_webdriver)
    yield browser
    browser.quit()



@pytest.fixture(scope="function")
def user_info() -> dict:
    user_info = dict()
    r = RandomWords()
    name = r.get_random_word().capitalize()
    domain = r.get_random_word().capitalize()
    user_info["name"] = name
    user_info["surname"] = domain
    user_info["email"] = f"{name}@{domain}.com"
    user_info["pswd"] = f"{r.get_random_word()}{randint(1000, 9999)}"
    user_info["address"] = f"{r.get_random_word().capitalize()} Street"
    user_info["city"] = f"{r.get_random_word().capitalize()} Town"
    user_info["state"] = f"{randint(1, 50)}"
    user_info["zip"] = "".join(f"{randint(1, 9)}" for _ in range(5))
    user_info["phone"] = "".join(f"{randint(1, 9)}" for _ in range(9))
    return user_info
