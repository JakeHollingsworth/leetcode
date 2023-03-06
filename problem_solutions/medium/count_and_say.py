'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        def next_n(s):
            lst = []
            for c in s:
                if not lst or c != lst[-1][1]:
                    lst.append([1, c])
                else:
                    lst[-1][0] += 1
            return ''.join([str(count) + val for count, val in lst])
        s = '1'
        for i in range(n-1):
            s = next_n(s)
        return s
