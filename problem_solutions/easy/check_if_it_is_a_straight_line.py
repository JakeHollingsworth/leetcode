'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] == coordinates[0][0]:
            if len(coordinates) == 2:
                return True
            return all([p[0] == coordinates[0][0] for p in coordinates[2:]])
        m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for point in coordinates[2:]:
            if (point[1] - coordinates[0][1]) != m * (point[0] - coordinates[0][0]):
                return False
        return True
