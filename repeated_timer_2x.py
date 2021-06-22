# Copyright (c) 2021-2025 Tackhyun Jung and Jongsung Yoon.
# This Library is completely free of charge.
__version__ = '0.0.1'

import time
from time import sleep
from threading import Timer
<<<<<<< HEAD


class Repeated_Timer_2x(object):
    def __init__(self, interval, duration, function, *args, **kwargs):
=======
from typing import Callable


class Repeated_Timer_2x(object):
    def __init__(self: object, interval: int, duration: int, function: Callable, *args: tuple, **kwargs: dict) -> object:
>>>>>>> 064bf87f467b06f80139c6ae46cd502236edfaef
        self._timer = None
        self.interval = interval
        self.duration = duration
        self.timer_tick = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()

<<<<<<< HEAD
    def _run(self):
=======
    def _run(self) -> None:
>>>>>>> 064bf87f467b06f80139c6ae46cd502236edfaef
        self.is_running = False
        self.start()
        self.timer_tick(self.duration, *self.args, **self.kwargs)

<<<<<<< HEAD
    def start(self):
=======
    def start(self) -> None:
>>>>>>> 064bf87f467b06f80139c6ae46cd502236edfaef
        if not self.is_running:
            if self._timer is not None:
                self.duration -= self.interval
                if self.duration <= 0:
                    return

            self.next_call += self.interval
            self._timer = Timer(self.next_call - time.time(), self._run)
            self._timer.start()
            self.is_running = True

<<<<<<< HEAD
    def stop(self):
        self._timer.cancel()
        self.is_running = False
=======
    def stop(self) -> None:
        self._timer.cancel()
        self.is_running = False

>>>>>>> 064bf87f467b06f80139c6ae46cd502236edfaef
