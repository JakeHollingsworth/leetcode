'''
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.
'''
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        hrs_curr, min_curr = int(current[:2]), int(current[3:])
        hrs_goal, min_goal = int(correct[:2]), int(correct[3:])
        num_ops = hrs_goal - hrs_curr
        min_diff = min_goal - min_curr if min_curr <= min_goal else 60 - (min_curr - min_goal)
        while min_diff:
            if min_diff >= 15:
                num_ops += min_diff // 15
                min_diff %= 15 
            elif min_diff >= 5:
                num_ops += min_diff // 5
                min_diff %= 5 
            else:
                num_ops += min_diff
                min_diff = 0
        return num_ops - (1 if min_curr>min_goal else 0)
