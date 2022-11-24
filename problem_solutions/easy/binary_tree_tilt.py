'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.
'''
class Solution:
    
    def dfs(self, node, tilt_sum):
        if node.left and node.right:
            left_sums, left_tilt = self.dfs(node.left, tilt_sum)
            right_sums, right_tilt = self.dfs(node.right, tilt_sum)
            total_sum = left_sums + right_sums + node.val
            tilt = abs(left_sums - right_sums)
        elif node.left:
            right_tilt = 0
            left_sums, left_tilt = self.dfs(node.left, tilt_sum)
            total_sum = left_sums + 0 + node.val
            tilt = abs(left_sums - 0)
        elif node.right:
            left_tilt = 0
            right_sums, right_tilt = self.dfs(node.right, tilt_sum)
            total_sum = right_sums + 0 + node.val
            tilt = abs(right_sums - 0)
        else:
            return node.val, 0
        return total_sum, left_tilt + right_tilt + tilt
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        _, tilt = self.dfs(root, 0)
        return tilt
