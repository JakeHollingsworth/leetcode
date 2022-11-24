'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
'''
class Solution:
    def inorder_traversal(self, root):
        ret_list = []
        if root.left:
            ret_list += self.inorder_traversal(root.left)
        ret_list += [root.val]
        if root.right:
            ret_list += self.inorder_traversal(root.right)
        return ret_list
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        traversal = self.inorder_traversal(root)
        return min([x-y for x,y in zip(traversal[1:], traversal[:-1])])
