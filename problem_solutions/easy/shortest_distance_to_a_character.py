'''
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_inds = []
        for i, ch in enumerate(s):
            if ch == c:
                c_inds.append(i)
        ans = []
        c_inds = [-float('inf')] + c_inds + [float('inf')]
        for i, ch in enumerate(s):
            ans.append(min(i-c_inds[0], c_inds[1]-i))
            if ch == c:
                c_inds.pop(0)
        return ans
