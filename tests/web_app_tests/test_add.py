""" Integration tests for the web add functionality app """
from web_app.app import APP


def test_add_with_empty_session():
    """ Adding with an empty session should result in the number added
        being the new total presented in the UI
    """
    with APP.test_client() as client:
        response = client.post("/add", data={"number_to_add": 5}, follow_redirects=True)

        assert b"Current Total: 5" in response.data


def test_add_with_session():
    """ Adding with an non empty session should result in the number added
        plus the existing total being the new presented in the UI
    """
    with APP.test_client() as client:
        client.post("/add", data={"number_to_add": 5}, follow_redirects=True)
        response = client.post(
            "/add", data={"number_to_add": 51}, follow_redirects=True
        )

        assert b"Current Total: 56" in response.data


def test_add_without_passing_a_number():
    """ Adding without passing a number should simply add 0 """
    with APP.test_client() as client:
        client.post("/add", data={"number_to_add": 5}, follow_redirects=True)
        response = client.post("/add", data={}, follow_redirects=True)

        assert b"Current Total: 5" in response.data
