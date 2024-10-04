from navet_tracker.core import DataSucker
from navet_tracker.notifications import Notification
from navet_tracker.scheduler import Scheduler


def run():
    m = DataSucker()  # Zakaria suggested this name and I think it's hilarious
    url = m.next_event()
    p = m.get_participants(url)
    b = m.get_event_name(url)

    if int(p) == 0:
        print("No open positions")
        return

    print(f"Open positions at {b}: {p}")
    n = Notification()
    n.notify(b, p)


def main():
    per_day = 4
    s = Scheduler(run, (24 / per_day) * 60 * 60)  # 6 hours / 4 times a day
    s.start()


if __name__ == "__main__":
    main()
