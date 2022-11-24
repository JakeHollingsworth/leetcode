'''
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.
'''
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        if points[1][0] == points[0][0] or points[2][0] == points[0][0]:
            return not (points[1][0] == points[0][0] and points[2][0] == points[0][0])
        m1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        m2 = (points[2][1] - points[0][1]) / (points[2][0] - points[0][0])
        b1 = - m1 * points[1][0] + points[1][1]
        b2 = - m2 * points[1][0] + points[1][1]
        return m1 != m2 or b1 != b2
