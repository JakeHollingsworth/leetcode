'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
'''
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            left_sum = self.rangeSumBST(root.left, low, high)
            right_sum = self.rangeSumBST(root.right, low, high)          
            return left_sum + right_sum + (root.val if root.val >= low and root.val <= high else 0)
        else:
            return 0
