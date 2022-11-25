'''
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.
'''
class Solution:
    def maximumTime(self, time: str) -> str:
        def max_valid(i, time):
            if i == 0:
                if time[1] == '?' or int(time[1]) <= 3:
                    return '2'
                else:
                    return '1'
            elif i == 1:
                if time[0] == '?' or time[0] == '2':
                    return '3'
                else:
                    return '9'
            elif i == 3:
                return '5'
            else:
                return '9'
            
        max_time = [c if c != '?' else max_valid(i, time) for i, c in enumerate(time)]
        if max_time[0] == '2' and time[1] == '?':
            max_time[1] = '3'
        return ''.join(max_time)
