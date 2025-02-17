from random import randint

import pytest
from random_word import RandomWords


@pytest.fixture(scope="session")
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
