'''
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.



Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.
'''
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        cols = 'abcdefgh'
        return (cols.index(coordinates[0]) + 1 + int(coordinates[1])) % 2
