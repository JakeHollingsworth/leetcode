'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
'''
class Solution:
    def getCombos(self, n):
        l = [[]]
        if not n: return [[]]
        if len(n) > 1:
            other_combos = self.getCombos(n[1:])
        else:
            other_combos = [[]]
        l = [[n[0]] + li for li in other_combos]
        l += other_combos
        return l

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        nums = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        inds = list(range(len(nums)))
        all_combos = self.getCombos(inds)
        all_strings = []
        for combo in all_combos:
            if len(combo) != turnedOn:
                continue
            hrs = sum([n for i,n in enumerate(nums) if i < 4 and i in combo])
            minutes = sum([n for i,n in enumerate(nums) if i >= 4 and i in combo])
            if hrs < 12 and minutes < 60:
                hr_string = str(hrs)
                minute_string = str(minutes) if minutes > 9 else "0" + str(minutes)
                all_strings.append(f'{hr_string}:{minute_string}')
        return all_strings
