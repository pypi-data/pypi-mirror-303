import threading


class ThreadSafeCounter:
    """
    A thread-safe counter class that allows incrementing, decrementing,
    getting the current value, and resetting the counter.
    """

    def __init__(self, value=0):
        self.counter = value
        self.lock = threading.Lock()

    def increment(self, value=1):
        """
        Increments the counter by 1.
        """
        with self.lock:
            self.counter += value

    def decrement(self, value=1):
        """
        Decrements the counter by 1.
        """
        with self.lock:
            self.counter -= value

    def get_value(self):
        """
        Returns the current value of the counter.
        """
        with self.lock:
            return self.counter

    def reset(self):
        """
        Resets the counter to 0.
        """
        with self.lock:
            self.counter = 0
