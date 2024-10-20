# tests/test_client.py

import os
import unittest
from unittest.mock import patch
from sporosdk import SporoClient

class TestSporoClient(unittest.TestCase):

    def setUp(self):
        self.api_key = "test_api_key"
        self.client = SporoClient(api_key=self.api_key, base_url="http://testurl.com/api/v1")

    @patch('sporosdk.client.requests.Session.post')
    def test_generate_summary_success(self, mock_post):
        # Mock response
        mock_response = unittest.mock.Mock()
        expected_summary = "This is a summary."
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "summary": expected_summary
            }
        }
        mock_post.return_value = mock_response

        # Call the method
        transcript = "This is a transcript."
        summary = self.client.generate_summary(transcript)

        # Assertions
        self.assertEqual(summary, expected_summary)
        mock_post.assert_called_once()

        # Verify that 'files' were sent correctly with None as filenames
        called_args, called_kwargs = mock_post.call_args
        self.assertIn('files', called_kwargs)
        self.assertEqual(called_kwargs['files'], {
            'transcript': (None, transcript),
            'temperature': (None, '0.7'),
            'max_tokens': (None, '512'),
            'llm': (None, 'gpt4o-mini'),
        })

    @patch('sporosdk.client.requests.Session.post')
    def test_generate_summary_failure(self, mock_post):
        # Mock response with error
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        # Call the method and expect an HTTPError
        with self.assertRaises(Exception) as context:
            self.client.generate_summary("Bad transcript.")

        self.assertIn("API request failed with status code 400", str(context.exception))

if __name__ == '__main__':
    unittest.main()
