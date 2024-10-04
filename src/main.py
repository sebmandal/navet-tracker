from navet_tracker.web import OpenEventFetcher, EventScraper
from navet_tracker.notifications import Notification
from navet_tracker.scheduler import Scheduler


def run():
    notifier = Notification()
    message = ""

    fetcher = OpenEventFetcher(url="https://ifinavet.no/arrangementer/2024/host")
    open_event_urls = fetcher.get_open_event_urls()
    open_events_summary = []

    for event_url in open_event_urls:
        full_url = f"https://ifinavet.no{event_url}"
        scraper = EventScraper(full_url)
        event_title = scraper.get_event_title()
        open_spots = scraper.get_open_spots()
        date_time = scraper.get_event_date_time()
        location = scraper.get_event_location()

        if open_spots != "0":
            open_events_summary.append(
                {
                    "title": event_title,
                    "open_spots": open_spots,
                    "url": full_url,
                    "date_time": date_time,
                    "location": location,
                }
            )

    if not open_events_summary:
        print("No open events found.")
        message += f"No open events right now. Check back later."
        # return  # Uncomment/comment this line to toggle sending a message when there are no open events.

    else:
        for event in open_events_summary:
            message += f"Tittel: [{event['title']}]({event['url']})\n"
            message += f"Ledige plasser: {event['open_spots']}\n"
            message += f"Dato og tidspunkt: {event['date_time']}\n"
            message += f"Lokasjon: {event['location']}\n\n"

    notifier.notify(message)


def main():
    schedule_times = ["12:05", "00:00"]
    s = Scheduler(run, schedule_times)
    s.start()


if __name__ == "__main__":
    main()
