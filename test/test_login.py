import pytest
from utils.data_reader import read_csv


@pytest.mark.parametrize("user", read_csv("data/login.csv"))
def test_login(login_p, user):

    login_p.login(user["username"], user["password"])

    is_valid = user["expected"].lower() == "true"

    if is_valid:

        login_p.take_screenshot("login exitoso")

        assert login_p.is_login_succesfull()

    else:

        login_p.take_screenshot("login fallido")

        actual_error = login_p.get_error_message()

        assert (user["error_message"] in actual_error)
