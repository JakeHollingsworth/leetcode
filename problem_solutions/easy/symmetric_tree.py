'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class Solution:
    def symmetric_halves(self, left_half, right_half):
        if not left_half and not right_half: return True
        if (not left_half and right_half) or (left_half and not right_half): return False
        if left_half.val == right_half.val:
            return self.symmetric_halves(left_half.left, right_half.right) and \
                   self.symmetric_halves(left_half.right, right_half.left)
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric_halves(root, root)
