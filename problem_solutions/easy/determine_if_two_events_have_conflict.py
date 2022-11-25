'''
You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.
'''
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def min_from_day_start(time_str):
            return 60 * int(time_str[:2]) + int(time_str[3:])
        s1, e1, s2, e2 = [min_from_day_start(t) for t in event1 + event2]
        return (s2 <= e1 and s2 >= s1) or (s1 <= e2 and s1 >= s2)
