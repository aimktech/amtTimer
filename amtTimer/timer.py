# -*- coding: utf-8 -*-
#
# A simple class to measure code performances.
# 
# Copyright 2020 AI Mechanics & Tech
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#----- Imports
from __future__ import annotations
from typing import List, Dict, Union, Iterator, ClassVar

import time
from threading import Lock

from amtStats import Statistics

#----- Classes
class Timer:
    """A simple class to measure code performances"""

    class TimerObject:
        def __init__(self, parent: Timer, name: str) -> None:
            """Constructor"""
            self._parent = parent
            self._name = name

        def __enter__(self):
            """Support for context managers #1"""
            self.start()
            return self
        
        def __exit__(self, *args):
            """Support for context managers #2"""
            self.stop()

        def start(self) -> None:
            """Start the timer or reset it if already started"""
            self._start: int = time.perf_counter_ns()
            self._stop: int = self._start

        def stop(self) -> None:
            """Stop the timer and update the parent array"""
            self._stop = time.perf_counter_ns()
            self._parent._update(self)

    def __init__(self) -> None:
        """Constructor"""
        self._timers: Dict[str, Statistics] = {}
        self._lock = Lock()

    def __call__(self, name: str) -> Timer.TimerObject:
        """Create a new timer"""
        return Timer.TimerObject(self, name)

    def _update(self, timer: Timer.TimerObject) -> None:
        """Update the statistics with this timer"""
        with self._lock:
            if timer._name not in self._timers:
                self._timers[timer._name] = Statistics()
            
            self._timers[timer._name].update(timer._stop - timer._start)
        
    def timers(self) -> Iterator[str]:
        """Return the names of all defined timers"""
        for name in self._timers:
            yield name
    
    def stats(self, name: str) -> Dict[str, Union[int, float]]:
        """Return the statistics for a defined timer"""
        with self._lock:
            if name not in self._timers:
                raise NameError(f'Timer {name} is not defined.')
            return self._timers[name].compute()


class TimerSingleton:
    """Performance Timer class implemented as a Singleton"""
    __instance: ClassVar[Timer] = Timer()

    @staticmethod
    def instance() -> Timer:
        return TimerSingleton.__instance
