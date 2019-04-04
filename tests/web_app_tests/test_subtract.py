# """ Integration tests for the web subtract functionality app """
# from web_app.app import APP
#
#
# def test_subtract_with_empty_session():
#     """ Subtracting with an empty session should result in the number subtracted
#         being the new (negative) total presented in the UI
#     """
#     with APP.test_client() as client:
#         response = client.post(
#             "/subtract", data={"input_number": 5}, follow_redirects=True
#         )
#
#         assert b"-5" in response.data
#
#
# def test_subtract_with_session():
#     """ Subtract with an non empty session should result in the existing total
#         minus the number to subtract being the new total presented in the UI
#     """
#     with APP.test_client() as client:
#         client.post("/subtract", data={"input_number": 5}, follow_redirects=True)
#         response = client.post(
#             "/subtract", data={"input_number": 51}, follow_redirects=True
#         )
#
#         assert b"-56" in response.data
#
#
# def test_subtract_without_passing_a_number():
#     """ Subtracting without passing a number should simply subtract 0 """
#     with APP.test_client() as client:
#         client.post("/subtract", data={"input_number": 5}, follow_redirects=True)
#         response = client.post("/subtract", data={}, follow_redirects=True)
#
#         assert b"-5" in response.data
