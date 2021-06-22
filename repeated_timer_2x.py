# Copyright (c) 2021-2025 Tackhyun Jung and Jongsung Yoon.
# This Library is completely free of charge.
__version__ = '0.0.1'

import time
from time import sleep
from threading import Timer


class Repeated_Timer_2x(object):
    def __init__(self, interval, duration, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.duration = duration
        self.timer_tick = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()

    def _run(self):
        self.is_running = False
        self.start()
        self.timer_tick(self.duration, *self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            if self._timer is not None:
                self.duration -= self.interval
                if self.duration <= 0:
                    return

            self.next_call += self.interval
            self._timer = Timer(self.next_call - time.time(), self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
