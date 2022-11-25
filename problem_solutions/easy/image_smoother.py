'''
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
'''
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_mat =  [[0 for sublist in img[0]] for sublist in img]
        for i in range(len(img)):
            for j in range(len(img[0])):
                a, b = [-1, 0, 1], [-1, 0, 1]
                if i == 0:
                    a = [0, 1]
                if i == len(img) - 1:
                    a = [-1,0]
                if j == 0:
                    b = [0, 1]
                if j == len(img[0])-1:
                    b = [-1, 0]
                new_mat[i][j] = int(sum([sum([img[i+x][j+y] for y in b]) for x in a]) / (len(a) * len(b)))
        return new_mat
