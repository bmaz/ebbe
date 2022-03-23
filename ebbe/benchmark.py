# =============================================================================
# Ebbe Benchmark Helpers
# =============================================================================
#
import sys
from timeit import default_timer as timer

from ebbe.format import prettyprint_time


class Timer(object):
    def __init__(self, name="Timer", file=sys.stderr, precision="nanoseconds"):
        self.name = name
        self.file = file
        self.precision = precision

    def __enter__(self):
        self.start = timer()

    def __exit__(self, *args):
        self.end = timer()
        self.duration = self.end - self.start
        print(
            "%s:" % self.name,
            prettyprint_time(self.duration, precision=self.precision, unit="seconds"),
            file=self.file,
        )
