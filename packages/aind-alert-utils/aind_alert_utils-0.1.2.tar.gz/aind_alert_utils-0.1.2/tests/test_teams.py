"""Tests teams module."""

import unittest

from aind_alert_utils.teams import create_body_contents


class TestCreateBodyContents(unittest.TestCase):
    """Tests create_body_contents cases."""

    def test_message_no_extra(self):
        """Tests the create_body_contents with a message."""

        actual_output = create_body_contents("Hello World")
        expected_output = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "size": "Medium",
                                "weight": "Bolder",
                                "text": "Hello World",
                            }
                        ],
                        "$schema": (
                            "http://adaptivecards.io/schemas/"
                            "adaptive-card.json"
                        ),
                        "version": "1.0",
                    },
                }
            ],
        }

        self.assertEqual(expected_output, actual_output)

    def test_message_with_extra(self):
        """Tests the create_body_contents with a message and extra text."""

        actual_output = create_body_contents(
            message="Hello World", extra_text="Goodbye"
        )
        expected_output = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "size": "Medium",
                                "weight": "Bolder",
                                "text": "Hello World",
                            },
                            {"type": "TextBlock", "text": "Goodbye"},
                        ],
                        "$schema": (
                            "http://adaptivecards.io/schemas/"
                            "adaptive-card.json"
                        ),
                        "version": "1.0",
                    },
                }
            ],
        }
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
