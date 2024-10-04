from navet_tracker.core import DataSucker
from navet_tracker.notifications import Notification


def main():
    m = DataSucker()  # Zakaria suggested this name and I think it's hilarious
    url = m.next_event()
    p = m.get_participants(url)
    b = m.get_event_name(url)

    if int(p) == 0:
        print("No open positions")
        return

    n = Notification()
    n.notify(b, p)


if __name__ == "__main__":
    main()
