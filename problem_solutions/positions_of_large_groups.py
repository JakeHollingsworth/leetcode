'''
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.
'''
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0
        end = 0
        groups = []
        while end < len(s):
            while end < len(s) and s[end] == s[start]:
                end += 1
            if end - start >= 3:
                groups.append([start, end-1])
            start = end
        return groups
