from navet_tracker.web import OpenEventFetcher, EventScraper
from navet_tracker.notifications import Notification
from navet_tracker.scheduler import Scheduler


def run():
    notifier = Notification()
    fetcher = OpenEventFetcher(url="https://ifinavet.no/arrangementer/2024/host")

    open_event_urls = fetcher.get_open_event_urls()
    open_events_summary = []

    for event_url in open_event_urls:
        full_url = f"https://ifinavet.no{event_url}"
        scraper = EventScraper(full_url)
        event_title = scraper.get_event_title()
        open_spots = scraper.get_open_spots()
        if open_spots != "0":
            open_events_summary.append(
                {"title": event_title, "open_spots": open_spots, "url": full_url}
            )

    if not open_events_summary:
        print("No open events found.")
        notifier.notify("No open events found.")
        return

    message = "-" * 40 + "\n"
    for event in open_events_summary:
        if event["open_spots"] == "0":
            continue
        message += f"Event: [{event['title']}](<{event['url']}>)\n"
        message += f"Open Spots: {event['open_spots']}\n"
        message += "-" * 40 + "\n"

    notifier.notify(message)


def main():
    per_day = 1
    scheduler_interval = (24 / per_day) * 60 * 60
    s = Scheduler(run, scheduler_interval)
    s.start()


if __name__ == "__main__":
    main()
