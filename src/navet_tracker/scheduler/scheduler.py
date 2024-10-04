import time
import threading
from datetime import datetime, timedelta


class Scheduler:
    def __init__(self, func, schedule_times) -> None:
        """
        Initializes the scheduler with the function and the list of schedule times.

        :param func: The function to be scheduled.
        :param schedule_times: List of times in 'HH:MM' format for running the function.
        """
        self.func = func
        self.schedule_times = [self._parse_time(t) for t in schedule_times]
        self._stop_event = threading.Event()

    def _parse_time(self, time_str):
        """Parses a time string in 'HH:MM' format and returns a datetime object for today."""
        now = datetime.now()
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        return datetime.combine(now.date(), time_obj)

    def _get_next_time(self):
        now = datetime.now()
        future_times = [t for t in self.schedule_times if t > now]

        if not future_times:
            # If no future times today, schedule the first time for tomorrow
            next_time = self.schedule_times[0] + timedelta(days=1)
        else:
            next_time = min(future_times)

        return next_time

    def _run(self) -> None:
        while not self._stop_event.is_set():
            next_time = self._get_next_time()
            sleep_duration = (next_time - datetime.now()).total_seconds()

            if sleep_duration > 0:
                time.sleep(sleep_duration)
                self.func()

    def start(self) -> None:
        self._stop_event.clear()
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def stop(self) -> None:
        self._stop_event.set()
        self.thread.join()
