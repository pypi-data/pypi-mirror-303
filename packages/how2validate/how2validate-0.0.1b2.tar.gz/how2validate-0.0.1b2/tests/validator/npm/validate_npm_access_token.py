import unittest
from unittest.mock import patch, Mock
import requests
import json

from how2validate.utility.config_utility import get_active_secret_status, get_inactive_secret_status
from how2validate.validators.npm.npm_access_token import validate_npm_access_token



# Import the function you want to test

class TestValidateNpmAccessToken(unittest.TestCase):

    @patch('how2validate.validators.npm.npm_access_token.requests.get')
    def test_valid_token_success(self, mock_get):
        """
        Test the case where the NPM access token is valid and the API returns 200 with a valid JSON response.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"user": "valid_user"}
        mock_get.return_value = mock_response
        
        result = validate_npm_access_token("npm", "valid_token", True, False)
        
        self.assertIn("active and operational", result.lower())
        self.assertIn('"user": "valid_user"', result)

    @patch('how2validate.validators.npm.npm_access_token.requests.get')
    def test_inactive_token(self, mock_get):
        """
        Test the case where the NPM access token is invalid, and the API returns a 401 status code.
        """
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_get.return_value = mock_response
        
        result = validate_npm_access_token("npm", "invalid_token", True, False)

        self.assertIn("inactive and not operational", result)
        self.assertIn("Unauthorized", result)

    # @patch('how2validate.validators.npm.npm_access_token.requests.get')
    # @patch('how2validate.utility.log_utility.get_active_secret_status')
    # def test_json_decode_error(self, mock_get_status, mock_get):
    #     """
    #     Test the case where the NPM API returns a 200 response but the body is not valid JSON.
    #     """
    #     mock_response = Mock()
    #     mock_response.status_code = 200
    #     mock_response.json.side_effect = ValueError("Invalid JSON")  # Simulate JSON decode error
    #     mock_get.return_value = mock_response
        
    #     # Mock the active secret status return value
    #     mock_get_status.return_value = "Active"

    #     result = validate_npm_access_token("npm", "valid_token", True, False)

    #     self.assertIn("Response is not a valid JSON.", result)


    # @patch('how2validate.validators.npm.npm_access_token.requests.get')
    # def test_connection_error(self, mock_get):
    #     """
    #     Test the case where a connection error occurs during the request.
    #     """
    #     mock_get.side_effect = requests.ConnectionError("Failed to establish a connection")
        
    #     result = validate_npm_access_token("npm", "invalid_token", True, False)

    #     self.assertIn("currently inactive and not operational", result)
    #     self.assertIn("No response.", result)

    # @patch('how2validate.validators.npm.npm_access_token.requests.get')
    # def test_timeout_error(self, mock_get):
    #     """
    #     Test the case where a timeout occurs during the request.
    #     """
    #     mock_get.side_effect = requests.Timeout("Request timed out")
        
    #     result = validate_npm_access_token("npm", "invalid_token", True, False)

    #     self.assertIn("currently inactive and not operational", result)
    #     self.assertIn("Request timed out", result)

    # @patch('how2validate.validators.npm.npm_access_token.requests.get')
    # def test_empty_response(self, mock_get):
    #     """
    #     Test the case where the API returns a 200 response with an empty body.
    #     """
    #     mock_response = MagicMock()
    #     mock_response.status_code = 200
    #     mock_response.json.return_value = {}  # Return an empty JSON object
    #     mock_get.return_value = mock_response

    #     service = "npm"
    #     secret = "dummy_secret"
    #     response = True
    #     report = False

    #     result = validate_npm_access_token(service, secret, response, report)

    #     # Check for "active" status message and ensure it's structured correctly
    #     self.assertIn("currently active and operational", result)
    #     self.assertIn("Here is the additional response data :", result)
    #     self.assertIn("{}", result)

if __name__ == '__main__':
    unittest.main()
