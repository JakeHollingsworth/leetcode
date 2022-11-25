'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num_flowers = 0
        if len(flowerbed) == 1 and not flowerbed[0]:
            num_flowers += 1
        if len(flowerbed) > 1 and not flowerbed[0] and not flowerbed[1]:
            flowerbed[0] = 1
            num_flowers += 1
        if len(flowerbed) > 2 and not flowerbed[-1] and not flowerbed[-2]:
            flowerbed[-1] = 1
            num_flowers += 1
        i = 1
        while i < len(flowerbed)-1:
            if not (flowerbed[i] or flowerbed[i+1] or flowerbed[i-1]):
                flowerbed[i] = 1
                num_flowers += 1
            i += 1
        return num_flowers >= n
