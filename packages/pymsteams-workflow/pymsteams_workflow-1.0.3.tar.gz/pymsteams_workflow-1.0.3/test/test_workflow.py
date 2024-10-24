import os
import sys
import pytest
from unittest.mock import patch
import asyncio

os.environ["MS_TEAMS_WORKFLOW"] = "https://httpstat.us/200"

# add scripts to the path
sys.path.append(
    os.path.split(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )[0]
)

import pymsteams
from pymsteams import TeamsWebhookException

def test_env_webhook_url():
    """
        Test that we have the webhook set as an environment variable.
        This is testing our test environment, not the code.
    """
    webhook_url = os.getenv("MS_TEAMS_WORKFLOW", None)
    assert webhook_url
    assert webhook_url.find("https") == 0

def test_send_message():
    """
    Test sending a simple text message with a title and link button.
    """
    webhook_url = os.getenv("MS_TEAMS_WORKFLOW")

    # Create the connector card
    teams_message = pymsteams.connectorcard(webhook_url)
    teams_message.text("This is a simple text message.")
    teams_message.title("Simple Message Title")
    teams_message.addLinkButton("Go to the Repo", "https://github.com/mroussamamessabih-emirates/pymsteams")

    # Patch the requests.post method to simulate sending
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200  # Simulate success response
        teams_message.send()
        # Assert that requests.post was called once
        mock_post.assert_called_once()

def test_send_message_failure():
    """
    Test sending a message when the request fails (HTTP 500).
    """
    webhook_url = os.getenv("MS_TEAMS_WORKFLOW")
    
    # Create the connector card
    teams_message = pymsteams.connectorcard(webhook_url)
    teams_message.text("This is a test message that should fail.")
    teams_message.title("Failing Message")

    # Patch the requests.post method to simulate failure
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 500  # Simulate server error response
        with pytest.raises(TeamsWebhookException):
            teams_message.send()
        # Assert that requests.post was called once
        mock_post.assert_called_once()

def test_async_send_message():
    """
        This asynchronously send a simple text message with a title and link button.
    """

    loop = asyncio.get_event_loop()

    teams_message = pymsteams.async_connectorcard(os.getenv("MS_TEAMS_WORKFLOW"))
    teams_message.text("This is a simple text message.")
    teams_message.title("Simple Message Title")
    teams_message.addLinkButton("Go to the Repo", "https://github.com/mroussamamessabih-emirates/pymsteams")
    
    
    
def test_http_500():
    """
    Test handling of a 500 HTTP status response.
    """
    with pytest.raises(TeamsWebhookException):
        myTeamsMessage = pymsteams.connectorcard("https://httpstat.us/500")
        myTeamsMessage.text("This is a simple text message.")
        myTeamsMessage.title("Simple Message Title")
        
        # Patch the requests.post method to simulate failure
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 500  # Simulate server error response
            myTeamsMessage.send()
            # Assert that requests.post was called once
            mock_post.assert_called_once()

def test_http_403():
    """
    Test handling of a 403 HTTP status response.
    """
    with pytest.raises(TeamsWebhookException):
        myTeamsMessage = pymsteams.connectorcard("http://httpstat.us/403")
        myTeamsMessage.text("This is a simple text message.")
        myTeamsMessage.title("Simple Message Title")
        
        # Patch the requests.post method to simulate failure
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 403  # Simulate forbidden error response
            myTeamsMessage.send()
            # Assert that requests.post was called once
            mock_post.assert_called_once()

