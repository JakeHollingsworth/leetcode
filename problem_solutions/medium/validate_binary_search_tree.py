'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(subroot, mini=-float('inf'), maxi=float('inf')):
            if not subroot:
                return True
            if subroot.left:
                if not subroot.left.val < subroot.val or not subroot.left.val > mini or not helper(subroot.left, mini = mini, maxi=subroot.val):
                    return False
            if subroot.right:
                if not subroot.right.val > subroot.val or not subroot.right.val < maxi or not helper(subroot.right, mini=subroot.val, maxi=maxi):
                    return False
            return True
        return helper(root, mini=-float('inf'), maxi=float('inf'))
