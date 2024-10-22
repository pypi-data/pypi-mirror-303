import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackClient:
    def __init__(self, bot_token_env_var: str):
        self.client = WebClient(token=os.getenv(bot_token_env_var))

    def send_text_message(self, channel_id: str, text: str):
        try:
            return self.client.chat_postMessage(channel=channel_id, text=text)
        except SlackApiError:
            raise
