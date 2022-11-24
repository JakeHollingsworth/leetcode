'''
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for n in range(2 ** (len(nums))):
            xor_tot = 0
            i = 0
            while n > 0:
                if n % 2:
                    xor_tot ^= nums[i]
                i += 1
                n //= 2
            total += xor_tot
        return total
