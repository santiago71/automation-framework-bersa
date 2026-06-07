import pytest
from utils.data_reader import read_csv


@pytest.mark.parametrize(
    "username,password,expected,error_message", read_csv("data/login.csv")
)
def test_login(login_p, username, password, expected, error_message):

    login_p.login(username, password)
    
    if login_p.is_captcha_present():

        pytest.skip("Captcha detectado")

    if expected:

        assert "/desktop" in login_p.driver.current_url

    else:
        
        actual_error = login_p.get_error_message()

        assert error_message in actual_error
