""" Integration tests for the web clear functionality app """
from web_app.app import APP


def test_clear_with_empty_session():
    """ clearing an empty session should set the total to 0 """
    with APP.test_client() as client:
        response = client.post("/clear", follow_redirects=True)

        assert b"Current Total: 0" in response.data


def test_clear_with_session():
    """ clearing an with an existing session should set the total to 0 """
    with APP.test_client() as client:
        response = client.post("/clear", follow_redirects=True)
        client.post("/add", data={"number_to_add": 5}, follow_redirects=True)

        assert b"Current Total: 0" in response.data
