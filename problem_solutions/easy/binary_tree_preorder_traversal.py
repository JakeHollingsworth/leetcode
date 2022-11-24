'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return_li = [root.val]
        if root.left:
            left_traversal = self.preorderTraversal(root.left)
        if root.right:
            right_traversal = self.preorderTraversal(root.right)
        if root.left and root.right:
            return return_li + left_traversal + right_traversal
        elif root.left:
            return return_li + left_traversal
        elif root.right:
            return return_li + right_traversal
        else:
            return return_li
