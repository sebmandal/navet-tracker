import os
from dotenv import load_dotenv
from navet_tracker.notifications.discord import send_discord_message


class Notification:
    def __init__(self):
        load_dotenv()
        self.webhook_urls = os.getenv("DISCORD_WEBHOOK_URLS").split(",")

    def notify(self, message: str) -> None:
        if not self.webhook_urls:
            raise ValueError("Discord webhook URLs are not set in the .env file.")
        for url in self.webhook_urls:
            send_discord_message(url.strip(), message)
