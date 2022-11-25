'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
class Solution:
    def get_depth(self, root):
        if not root: 
            return 0
        else: 
            return max(self.get_depth(root.left), self.get_depth(root.right)) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.get_depth(root.left)
        right_height = self.get_depth(root.right)
        if abs(left_height - right_height) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
