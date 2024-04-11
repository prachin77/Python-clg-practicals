import time

class StopWatch:
    def __init__(self):
        self._start_time = time.time()
        self._end_time = None

    def start(self):
        self._start_time = time.time()

    def stop(self):
        self._end_time = time.time()

    def get_elapsed_time(self):
        if self._end_time is None:
            raise ValueError("StopWatch has not been stopped yet")
        return (self._end_time - self._start_time) * 1000  # Convert to milliseconds

# Test program
def main():
    stopwatch = StopWatch()

    # Start stopwatch
    stopwatch.start()

    # Perform operation
    total = 0
    for i in range(1, 1000001):
        total += i

    # Stop stopwatch
    stopwatch.stop()

    # Get elapsed time
    elapsed_time = stopwatch.get_elapsed_time()
    print("Elapsed time:", elapsed_time, "milliseconds")

if __name__ == "__main__":
    main()
