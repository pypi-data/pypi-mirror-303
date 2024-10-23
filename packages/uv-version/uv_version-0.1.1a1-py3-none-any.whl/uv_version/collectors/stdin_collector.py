import os
import sys

from uv_version.collectors.base import BaseCollector


class StdinCollector(BaseCollector):
    def collect(self):
        if os.isatty(sys.stdin.fileno()):
            return None

        return sys.stdin.read()
