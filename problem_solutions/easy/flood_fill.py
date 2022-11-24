'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
'''
class Solution:
    def dfs(self, image, sr, sc, newColor, starting_pixel):
        if image[sr][sc] == starting_pixel:
            image[sr][sc] = newColor
            if sr - 1 >= 0:
                image = self.dfs(image, sr-1, sc, newColor, starting_pixel)
            if sr + 1 < len(image):
                image = self.dfs(image, sr+1, sc, newColor, starting_pixel)
            if sc - 1 >= 0:
                image = self.dfs(image, sr, sc-1, newColor, starting_pixel)
            if sc + 1 < len(image[0]):
                image = self.dfs(image, sr, sc+1, newColor, starting_pixel)
        return image
                
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        if  starting_pixel != newColor:
            return self.dfs(image, sr, sc, newColor, starting_pixel)
        return image
