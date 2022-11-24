'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
'''
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        locs = {(x,y)}
        for step in path:
            if step == 'N':
                y += 1
            elif step == 'S':
                y -= 1
            elif step == 'E':
                x += 1
            elif step == 'W':
                x -= 1
            if (x,y) in locs:
                return True
            else:
                locs.add((x,y))
        return False
        
