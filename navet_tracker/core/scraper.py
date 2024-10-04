import requests
import html2text
import json
from lxml import html


class DataSucker:
    def __init__(self) -> None:
        pass

    def next_event(self) -> str:
        url = "https://ifinavet.no"
        res = requests.get(url)
        data = res.text
        event = data.split(':events="')[1]
        event = event.split("}")[0] + "}" + "]"
        event = html2text.html2text(event)
        event = event.replace("\n", "")
        event = json.loads(event)
        return "https://ifinavet.no" + event[0]["Url"]

    def get_participants(self, url: str) -> int:
        res = requests.get(url)
        data = res.text
        tree = html.fromstring(data)
        participants = tree.xpath(
            '//*[@id="app"]/div/div/div[1]/div/div[2]/div[2]/span[3]/text()'
        )
        participants = participants[0].split(" ")[0]
        return participants[0]

    def get_event_name(self, url: str) -> str:
        url = "https://ifinavet.no"
        res = requests.get(url)
        data = res.text
        event = data.split(':events="')[1]
        event = event.split("}")[0] + "}" + "]"
        event = html2text.html2text(event)
        event = event.replace("\n", "")
        event = json.loads(event)
        return event[0]["Name"]
