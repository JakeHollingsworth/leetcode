'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if root.left and root.right:
            return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        elif root.left:
            return self.inorderTraversal(root.left) + [root.val]
        elif root.right:
            return [root.val] + self.inorderTraversal(root.right)
        else:
            return [root.val]
