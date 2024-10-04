import requests
from bs4 import BeautifulSoup


class EventScraper:
    def __init__(self, event_url):
        self.event_url = event_url
        self.soup = self._fetch_event_page()

    def _fetch_event_page(self):
        response = requests.get(self.event_url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml")
        else:
            raise Exception(
                f"Failed to fetch event page at {self.event_url}, status code: {response.status_code}"
            )

    def get_event_title(self):
        title = self.soup.find("h1", class_="primary center")
        return title.text

    def get_event_date_time(self):
        event_meta = self.soup.find_all("div", class_="event-meta")
        date_time = event_meta[0].find_all("span")[2]
        date_time = date_time.text.strip()
        date_time = date_time.replace("kl. ", " klokken ")
        return date_time

    def get_event_location(self):
        location = self.soup.find("span", class_="icon-location")
        return location.find_next_sibling("span").find_next_sibling("span").text

    def get_food(self):
        food = self.soup.find("span", class_="icon-spoon-knife")
        return food.find_next_sibling("span").text

    def get_open_spots(self):
        spots = self.soup.find("span", class_="icon-users")
        return (
            spots.find_next_sibling("span").find_next_sibling("span").text.split(" ")[0]
        )

    def get_event_description(self):
        description = self.soup.find("h2")
        return description.find_next("p").text.strip()

    def get_organizers(self):
        organizers = {}
        main_contact = self.soup.find("div", class_="contact-personalia")
        organizers["main"] = main_contact.find("p").text.strip()

        helpers = self.soup.find_all("div", class_="contact-card--small")
        organizers["helpers"] = [helper.find("p").text.strip() for helper in helpers]

        return organizers
