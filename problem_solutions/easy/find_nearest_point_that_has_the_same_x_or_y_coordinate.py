'''
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
'''
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_pts = [(p, i) for i, p in enumerate(points) if p[0] == x or p[1] == y]
        
        man_dists = [abs(p[0] - x) + abs(p[1] - y) for  (p,_) in valid_pts]
        if not man_dists:
            return -1
        min_dist = min(man_dists)
        for (_, i), d in zip(valid_pts, man_dists):
            if d == min_dist:
                return i
