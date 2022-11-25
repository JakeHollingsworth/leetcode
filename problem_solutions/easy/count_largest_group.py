'''
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.
'''
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(m):
            total = 0
            while m > 0:
                total += m % 10
                m //= 10
            return total
        groups = {}
        for i in range(1, n+1):
            g = digit_sum(i)
            groups[g] = groups[g] + 1 if g in groups else 1
        max_size = max(groups.values())
        return sum([v == max_size for v in groups.values()])
