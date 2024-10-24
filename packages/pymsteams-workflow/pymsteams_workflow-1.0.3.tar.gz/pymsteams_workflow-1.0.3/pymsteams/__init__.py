#!/usr/bin/env python

import requests
import json
from urllib.parse import urlparse, parse_qs

class TeamsWebhookException(Exception):
    """Custom exception for failed webhook call."""
    pass

class connectorcard:
    def __init__(self, url):
        # Parse the URL to extract the base URL and query parameters
        parsed_url = urlparse(url)
        self.hookurl = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        query_params = parse_qs(parsed_url.query)

        # Extract or set default values for the required parameters
        self.params = {
            'api-version': query_params.get('api-version', ['2016-06-01'])[0],
            'sp': query_params.get('sp', ['/triggers/manual/run'])[0],
            'sv': query_params.get('sv', ['1.0'])[0],
            'sig': query_params.get('sig', ['_8Ig0bXgZb2XNvMBzqfi69WYujgKSxYxXWEr5YlctXM'])[0]
        }

        # Set up the payload structure
        self.payload = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "contentUrl": None,
                    "content": {
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.4",
                        "body": [
                            {
                                "type": "Image",
                                "url": "https://github.com/caronc/apprise/raw/master/apprise/assets/themes/default/apprise-info-32x32.png",
                                "height": "32px",
                                "altText": "info"
                            }
                        ],
                        "msteams": {
                            "width": "full"
                        }
                    }
                }
            ]
        }
        self.proxies = None
        self.http_timeout = 60
        self.verify = True
        self.last_http_response = None

    def text(self, mtext):
        # Add text block to the payload
        self.payload["attachments"][0]["content"]["body"].append({
            "type": "TextBlock",
            "text": mtext,
            "style": "default",
            "wrap": True,
            "id": "body"
        })
        return self

    def title(self, mtitle):
        # Insert title block into the payload
        self.payload["attachments"][0]["content"]["body"].insert(1, {
            "type": "TextBlock",
            "text": mtitle,
            "style": "heading",
            "weight": "Bolder",
            "size": "Large",
            "id": "title"
        })
        return self
    
    def addLinkButton(self, button_text, button_url):
        # Add a link button to the payload
        self.payload["attachments"][0]["content"]["actions"] = [
            {
                "type": "Action.OpenUrl",
                "title": button_text,
                "url": button_url
            }
        ]
        return self
    
    def send(self):
        headers = {
            'User-Agent': 'MSTeams',
            'Content-Type': 'application/json'
        }

        # Make the POST request to send the notification
        try:
            r = requests.post(
                self.hookurl,
                params=self.params,
                data=json.dumps(self.payload),
                headers=headers,
                proxies=self.proxies,
                timeout=self.http_timeout,
                verify=self.verify
            )
            self.last_http_response = r

            # Check the response
            if r.status_code in (requests.codes.ok, requests.codes.accepted):
                print("Message sent successfully!")
                return True
            else:
                print(f"Failed to send message. Status code: {r.status_code}, Response: {r.text}")
                raise TeamsWebhookException(r.text)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            raise TeamsWebhookException(str(e))

class async_connectorcard(connectorcard):

    async def send(self):
        try:
            import httpx
        except ImportError as e:
            print("For use the asynchronous connector card, "
                  "install the asynchronous version of the library via pip: pip install pymsteams[async]")
            raise e

        headers = {"Content-Type": "application/json"}

        async with httpx.AsyncClient(proxies=self.proxies, verify=self.verify) as client:
            resp = await client.post(
                self.hookurl,
                params=self.params,
                data=json.dumps(self.payload),
                headers=headers,
                timeout=self.http_timeout,
            )
            self.last_http_response = resp
            # Check the response
            if resp.status_code in (requests.codes.ok, requests.codes.accepted):
                return True
            else:
                raise TeamsWebhookException(resp.text)