def assert_equal(actual, expected, message):

    assert actual == expected, f"{message} | Actual: {actual} | Expected: {expected}"
    
def assert_url(actual_url, expected_url):

    assert expected_url in actual_url, f"URL incorrecta | Actual: {actual_url}"