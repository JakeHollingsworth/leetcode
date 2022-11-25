'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        right_traversal, left_traversal = [], []
        if root.right:
            right_traversal = self.postorderTraversal(root.right)
        if root.left:
            left_traversal = self.postorderTraversal(root.left)
        return left_traversal + right_traversal + [root.val]
