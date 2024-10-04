import requests


def send_discord_message(webhook_url, message):
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}

    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code {response.status_code}")
