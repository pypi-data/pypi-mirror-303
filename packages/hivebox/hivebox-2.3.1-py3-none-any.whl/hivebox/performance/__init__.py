import contextlib
import csv
import time


class Timer:
    def __init__(self, output=None):
        self._results = []
        self._output = output

    @contextlib.contextmanager
    def measure(self, name):
        start = time.time()
        yield
        end = time.time()

        self._results.append((end, name, end - start))

    def dump(self):
        if self._output is None:
            print(self._results)
            return

        with open(self._output, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'name', 'elapsed'])
            for item in self._results:
                writer.writerow(item)
