import os
from dotenv import load_dotenv
from navet_tracker.notifications.discord import send_discord_message


class Notification:
    def __init__(self):
        load_dotenv()
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    def notify(self, message: str) -> None:
        if not self.webhook_url:
            raise ValueError("Discord webhook URL is not set in the .env file.")
        send_discord_message(self.webhook_url, message)
