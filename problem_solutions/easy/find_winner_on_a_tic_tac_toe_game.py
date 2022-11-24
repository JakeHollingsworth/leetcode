'''
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check_win(player):
            rows = 3*[0]
            cols = 3*[0]
            diags = 2*[0]
            for x, y in player:
                rows[x] += 1
                cols[y] += 1
                diags[0] += 1 if (y == x) else 0
                diags[1] += 1 if y == 2-x else 0
            return any([r==3 for r in rows]) or any([c==3 for c in cols]) or any([d==3 for d in diags]) 
        alice = [moves[i] for i in range(0, len(moves), 2)]
        bob =  [moves[i] for i in range(1, len(moves), 2)]
        if check_win(alice):
            return 'A'
        elif check_win(bob):
            return 'B'
        else:
            return 'Draw' if len(moves) == 9 else 'Pending'
