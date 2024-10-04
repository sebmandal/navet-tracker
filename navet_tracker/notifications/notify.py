import requests
import json
from navet_tracker.notifications.discord import send_discord_message


class Notification:
    def notify(self, event: str, participants: int) -> None:
        # TODO: move to .env
        webhook_url = "https://discord.com/api/webhooks/..."
        message = f"Open positions at {event}: {participants}"
        send_discord_message(webhook_url, message)
