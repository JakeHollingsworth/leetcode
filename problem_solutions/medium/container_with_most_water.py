'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        volume = lambda i,j: (j-i) * min(height[i], height[j])
        max_vol = volume(left, right)
        while right > left:
            max_vol = max(max_vol, volume(left, right))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_vol
