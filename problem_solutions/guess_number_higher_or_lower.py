'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        med = 1
        while guess(med):
            med = start + (end - start) // 2
            if guess(med) == -1:
                end = med - 1
            else:
                start = med + 1
        return med
            