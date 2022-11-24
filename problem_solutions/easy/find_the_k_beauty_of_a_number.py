'''
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.
'''
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        res = 0
        for i in range(0, len(num_str)-k+1):
            k_sub = num_str[i:i+k]
            if int(k_sub) and num % int(k_sub) == 0:
                res += 1
        return res
