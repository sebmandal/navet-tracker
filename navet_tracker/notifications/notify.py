import requests
import json


class Notification:
    def __init__(self) -> None:
        pass

    def notify(self, event: str, participants: int) -> None:
        # TODO: move to .env
        REPO_OWNER = ""
        REPO_NAME = ""
        TOKEN = ""

        title = "Open positions at %s! There are %s open positions" % (
            event,
            participants,
        )
        body = (
            "There are %s open positions at %s. Please check the event page for more information"
            % (participants, event)
        )
        assignee = "sebmandal"
        labels = ["event"]

        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

        # Headers
        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }

        # Create our issue
        data = {
            "title": title,
            "body": body,
            "assignees": [assignee],
            "labels": labels,
        }

        payload = json.dumps(data)

        # Add the issue to our repository
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 201:
            print(f'Successfully created Issue "{title}"')
        else:
            print(f'Could not create Issue "{title}"')
            print("Response:", response.content)
