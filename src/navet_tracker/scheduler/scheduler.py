import time
import threading


class Scheduler:
    def __init__(self, func, frequency_seconds) -> None:
        """
        Initializes the scheduler with the function and the frequency (in seconds).

        :param func: The function to be scheduled.
        :param frequency_seconds: The frequency (in seconds) for running the function.
        """
        self.func = func
        self.frequency_seconds = frequency_seconds
        self._stop_event = threading.Event()

    def _run(self) -> None:
        while not self._stop_event.is_set():
            self.func()
            time.sleep(self.frequency_seconds)

    def start(self) -> None:
        self._stop_event.clear()
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def stop(self) -> None:
        self._stop_event.set()
        self.thread.join()
