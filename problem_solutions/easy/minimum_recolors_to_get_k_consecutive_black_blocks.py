'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
'''
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks = [c for c in blocks]
        mini = len(blocks) if len(blocks) > k else blocks.count('W')
        for i in range(0, len(blocks) - k +1):
            mini = min(mini, blocks[i:i+k].count('W'))
        return mini
