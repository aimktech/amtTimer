# -*- coding: utf-8 -*-
# 
# Unit tests for the amtTimer module
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
import unittest
import time

from amtTimer import Timer, TimerSingleton


#----- Classes
class TestFactory(unittest.TestCase):

    def setUp(self):
        self.myTimer = Timer()

    def test_new_timer(self):
        timer = self.myTimer("timer")
        self.assertTrue(isinstance(timer, Timer.TimerObject))
    
    def test_time_measurement(self):
        timer = self.myTimer("timer")
        start = time.perf_counter_ns()
        timer.start()
        time.sleep(0.2)
        timer.stop()
        stop = time.perf_counter_ns()

        value = self.myTimer._timers['timer'].values[0]
        delta = stop - start

        self.assertLessEqual(value, delta)

    def test_context_manager(self):
        start = time.perf_counter_ns()
        with self.myTimer("timer"):
            time.sleep(0.2)
        stop = time.perf_counter_ns()

        value = self.myTimer._timers['timer'].values[0]
        delta = stop - start

        self.assertLessEqual(value, delta)

    def test_iterator(self):
        timer_names = ['one', 'two', 'three', 'four']
        for name in timer_names:
            with self.myTimer(name):
                time.sleep(0.2)

        timers = []
        for name in self.myTimer.timers():
            timers.append(name)

        self.assertEqual(timers, timer_names) 

    def test_stats_unknown_timer(self):
        with self.assertRaises(NameError):
            self.myTimer.stats("Unknown")

    def test_stats_timer(self):
        with self.myTimer("timer"):
            time.sleep(0.2)

        value = self.myTimer._timers['timer'].values[0]
        results = self.myTimer.stats("timer")

        self.assertTrue(isinstance(results, dict))
        self.assertEqual(results['min'], value)
        self.assertEqual(results['max'], value)


    #
    # Singleton testing
    #
    def test_singleton_instance(self):
        timer_one = TimerSingleton.instance()
        timer_two = TimerSingleton.instance()
        self.assertEqual(id(timer_one), id(timer_two))
