'''
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.
'''
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def scan(board, start, increment):
            left, right = start
            dl, dr = increment
            while left >= 0 and left < 8 and right >= 0 and right < 8:
                if board[left][right] == 'p':
                    return 1
                elif board[left][right] == 'B':
                    return 0
                else:
                    left += dl
                    right += dr
            return 0
        for i, row in enumerate(board):
            for j, col in enumerate(board[i]):
                if board[i][j] == 'R':
                    start = [i, j]
        return scan(board, start, [1,0]) + scan(board, start, [-1,0]) + scan(board, start, [0,1]) + scan(board, start, [0,-1]) 
