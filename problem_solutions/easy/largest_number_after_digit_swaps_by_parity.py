'''
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.
'''
class Solution:
    def largestInteger(self, num: int) -> int:
        evens = []
        odds = []
        is_odd_digit = []
        num_copy = num
        while num_copy:
            if num_copy % 2:
                odds.append(num_copy % 10)
            else:
                evens.append(num_copy % 10)
            is_odd_digit.append(num_copy % 2)
            num_copy //= 10
        evens.sort()
        odds.sort()
        res = 0
        for parity in is_odd_digit[::-1]:
            res *= 10
            if parity:
                res += odds.pop(-1) if odds else evens.pop(-1)
            else:
                res += evens.pop(-1) if evens else odds.pop(-1)
        return res
