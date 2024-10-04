import requests
from bs4 import BeautifulSoup


class OpenEventFetcher:
    def __init__(self, url):
        self.url = url
        self.soup = self._fetch_page_content()

    def _fetch_page_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml")
        else:
            raise Exception(
                f"Failed to fetch the page at {self.url}, status code: {response.status_code}"
            )

    def get_open_event_urls(self):
        open_events = self.soup.find_all("div", class_="event-list-item--open")
        event_urls = []
        for event in open_events:
            a_tag = event.find("a")
            if a_tag and "href" in a_tag.attrs:
                event_urls.append(a_tag["href"])
        return event_urls
