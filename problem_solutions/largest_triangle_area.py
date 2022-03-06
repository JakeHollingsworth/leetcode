'''
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
'''
class Solution:
    def getArea(self, vert1, vert2, vert3):
        vert2 = [vert2[0] - vert1[0], vert2[1]-vert1[1]]
        vert3 = [vert3[0] - vert1[0], vert3[1]-vert1[1]]
        return .5 * abs(vert2[0] * vert3[1] - vert2[1] * vert3[0]) # Cross product
    
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        for i, vert1 in enumerate(points[:-2]):
            for j, vert2 in enumerate(points[i+1:-1]):
                for k, vert3 in enumerate(points[i+j+1:]):
                    max_area = max(max_area, self.getArea(vert1, vert2, vert3))
        return max_area
