'''
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
'''
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        left_flag = False
        right_flag = False
        cumulative = [arr[0]]
        for n in arr[1:]:
            cumulative.append(cumulative[-1] + n)
        for curr in cumulative[:-1]:
            if curr == (2 * total / 3) and left_flag:
                right_flag = True
            if curr == total / 3:
                left_flag = True
        return left_flag and right_flag
