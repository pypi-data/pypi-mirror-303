# pymsteams

Python Wrapper Library to send requests to Microsoft Teams via Microsoft Power Automate workflows.

I have created this library because the Microsoft Teams Webhook is being retired. [Retirement of Office 365 connectors within Microsoft Teams](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/)

## Overview

This library allows sending messages with rich formatting to Microsoft Teams by utilizing Power Automate workflows. Messages can include simple text, titles, link buttons, and more. You can also use asynchronous operations to send messages in parallel.

## Installation

Install with pip:

```bash
pip install pymsteams-workflow
```

## Usage

### Creating ConnectorCard Messages

Below is a basic example demonstrating how to send a message using a Power Automate workflow URL:

```python
from pymsteams import connectorcard

# You must create the connectorcard object with the Power Automate URL
myTeamsMessage = connectorcard("<Power Automate URL>")

# Add text to the message
myTeamsMessage.text("This is my text")

# Send the message
myTeamsMessage.send()
```

### Asynchronous ConnectorCard Messages

You can send messages asynchronously using `async_connectorcard`. This is useful when sending multiple messages or performing other asynchronous tasks.

```python
import asyncio
from pymsteams import async_connectorcard

loop = asyncio.get_event_loop()

# The async_connectorcard object is used for asynchronous operations
myTeamsMessage = async_connectorcard("<Power Automate URL>")

# Add text to the message
myTeamsMessage.text("This is my async message")

# Send the message asynchronously
loop.run_until_complete(myTeamsMessage.send())
```

### Optional Formatting Methods

#### Add a Title

You can add a title to the message, which will be displayed prominently:

```python
myTeamsMessage.title("This is my message title")
```

#### Add a Link Button

Add a link button to your message to redirect users to a specific URL:

```python
myTeamsMessage.addLinkButton("This is the button Text", "https://example.com")
```

### Example: Sending a Message with a Title and Link Button

Here's a complete example of sending a message with both a title and a link button:

```python
from your_module import connectorcard  # Replace 'your_module' with your module name

webhook_url = "<Power Automate URL>"

# Create the connector card
card = connectorcard(webhook_url)
card.title("Important Notification")
card.text("Please review the latest updates.")
card.addLinkButton("Review Updates", "https://example.com/updates")

# Send the message
card.send()
```

### Exception Handling

If the call to the Power Automate service fails, a `TeamsWebhookException` will be thrown. Ensure you handle this exception in your code:

```python
try:
    card.send()
except TeamsWebhookException as e:
    print(f"Failed to send message: {e}")
```

## Testing

In order to test in your environment with `pytest`, set the environment variable `MS_TEAMS_WORKFLOW` to the Power Automate workflow URL you would like to use.

Then, from the root of the repo, install the requirements and run pytest.

```bash
pip install -r dev-requirements.txt
MS_TEAMS_WORKFLOW=<PowerAutomateURL>
export MS_TEAMS_WORKFLOW
pytest --cov=./your_module --cov-report=term-missing --cov-branch  # Replace 'your_module' with your module name
```

## Docs

- [Send a message in Teams using Power Automate](https://learn.microsoft.com/en-us/power-automate/teams/send-a-message-in-teams)
- [apprise Notify_workflows](https://github.com/caronc/apprise/wiki/Notify_workflows)
- [Retirement of Office 365 connectors within Microsoft Teams](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/)

