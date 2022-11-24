'''
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
'''
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        new_intervals = []
        # Simplify intervals by constructing largest continuous intervals
        for start, end in ranges:
            overlapping = False
            for i, (l, r) in enumerate(new_intervals):
                if start >= l and start <= r+1:
                    new_intervals[i][1] = max(new_intervals[i][1], end)
                    overlapping = True
                elif end <= r and end >= l-1:
                    new_intervals[i][0] = min(new_intervals[i][0], start)
                    overlapping = True
            if not overlapping:
                new_intervals.append([start, end])
        # Make sure that start and end lie within 1 of these intervals.
        for start, end in new_intervals:
            if left >= start and right <= end:
                return True
        return False
