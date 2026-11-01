"""A tiny thread-safe counter, used to know when every robot has stopped."""
import threading


class SharedCounter:

    def __init__(self, starting_value):
        self._value = starting_value
        self._lock = threading.Lock()

    def decrement(self):
        with self._lock:
            self._value -= 1

    def is_zero(self):
        with self._lock:
            return self._value <= 0
