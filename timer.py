
from datetime import date, datetime


class Timer:
    def __init__(self, duration):
        self.reset()
        self.duration = duration

    def reset(self):
        self.start = datetime.now()

    def __bool__(self):
        now = datetime.now()
        time_passed = (now - self.start).total_seconds()
        return time_passed < self.duration

    __nonzero__ = __bool__