def test_login_exitoso(login_p):
        
        login_p.login("standard_user","secret_sauce")
        
        assert "inventory.html" in login_p.driver.current_url
        
def test_invalid_login(login_p):

        login_p.login("standar", "123455")

        error_message = login_p.get_error_message()

        assert error_message == "Epic sadface: Username and password do not match any user in this service"