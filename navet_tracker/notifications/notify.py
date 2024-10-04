import requests
import json
from navet_tracker.notifications.discord import send_discord_message


class Notification:
    def notify(self, message: str) -> None:
        # TODO: move to .env
        webhook_url = "https://discord.com/api/webhooks/..."
        send_discord_message(webhook_url, message)
