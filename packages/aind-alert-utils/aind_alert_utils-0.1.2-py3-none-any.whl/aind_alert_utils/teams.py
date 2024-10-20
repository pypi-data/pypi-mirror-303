"""Module to send alerts to MS Teams"""

from typing import Any, Dict, Optional


def create_body_contents(
    message: str, extra_text: Optional[str] = None
) -> Dict[str, Any]:
    """
    Parse strings into appropriate format to send to an MS Teams channel.
    Check here for more information:
      https://learn.microsoft.com/en-us/microsoftteams/platform/
      task-modules-and-cards/cards/cards-reference#adaptive-card

    Parameters
    ----------
    message : str
      The main message content
    extra_text : Optional[str]
      Additional text to send in card body

    Returns
    -------
    Dict[str, Any]
      A dictionary that can be set in the post requests module.

    """
    body: list = [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": message,
        }
    ]
    if extra_text is not None:
        body.append({"type": "TextBlock", "text": extra_text})
    contents = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "type": "AdaptiveCard",
                    "body": body,
                    "$schema": (
                        "http://adaptivecards.io/schemas/" "adaptive-card.json"
                    ),
                    "version": "1.0",
                },
            }
        ],
    }
    return contents
