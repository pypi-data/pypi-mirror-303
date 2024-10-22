#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# **************************************************
__author__  = "Teddy Chantrait"
__email__   = "teddy.chantrait@gmail.com"
__status__  = "Development"
__date__    = "2024-07-03 17:28:00.999352"
__version__ = 1.0
# **************************************************

class IScheduler():
    def __init__(self, dt_seuil=1e-9):
        self._its_a_meeting_point = True
        self._dt_to_next_meeting_point = -1
        self._dt_seuil = dt_seuil
        # self.neibor_dt = 0
        # self._dtmax = 0
        # self._dtmin = 0
        self.next_meeting_point = 0
        # self.dt_guest = 0

    def _check_schedule(self):
        self._dt_to_next_meeting_point = abs(self.next_meeting_point-self.get_current_time())
        if self._dt_to_next_meeting_point < self._dt_seuil:
            self._is_a_meeting_point = True
        else:
            self._is_a_meeting_point = False

    def do_publish_action(self):
        self._check_schedule()
        return self._is_a_meeting_point

    def do_collect_action(self):
        # self._check_schedule()  # par securité le garder?
        return self._is_a_meeting_point

    def get_current_time(self):
        raise NotImplementedError('Must be override')

    def __repr__(self):
        to_ret = ""
        to_ret += "time to next meeting point: " + str(self._dt_to_next_meeting_point) + "\n"
        to_ret += "next meeting point: " + str(self.next_meeting_point) + "\n"
        return to_ret
