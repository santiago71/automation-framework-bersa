import pytest
from utils.data_reader import read_csv


<<<<<<< HEAD
@pytest.mark.parametrize(
    "username,password,expected,error_message", read_csv("data/login.csv")
)
def test_login(login_p, username, password, expected, error_message):

    login_p.login(username, password)
    
    if login_p.is_captcha_present():

        pytest.skip("Captcha detectado")
=======
@pytest.mark.parametrize("user", read_csv("data/login.csv"))
def test_login(login_p, user):

    login_p.login(user["username"], user["password"])
>>>>>>> 0f9283e4534d9b48374b38c66ecf84388efd46ef

    is_valid = user["valid"].lower() == "true"

    if is_valid:

        login_p.take_screenshot("login exitoso")

        assert "/desktop" in login_p.driver.current_url

    else:
<<<<<<< HEAD
        
        actual_error = login_p.get_error_message()

        assert error_message in actual_error
=======

        login_p.take_screenshot("login fallido")

        actual_error = login_p.get_error_message()

        assert (user["error_message"] in actual_error)
>>>>>>> 0f9283e4534d9b48374b38c66ecf84388efd46ef
