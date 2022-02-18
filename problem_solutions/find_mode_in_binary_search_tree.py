'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
'''
class Solution:
    def modeSearch(self,root,memo):
        memo[root.val] = memo[root.val] + 1 if root.val in memo else 1
        if root.left:
            self.modeSearch(root.left, memo)
        if root.right:
            self.modeSearch(root.right, memo)

        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        memo = {}
        self.modeSearch(root, memo)
        max_c = 0
        ans = []
        for m, c in memo.items():
            if c == max_c:
                ans.append(m)
            elif c > max_c:
                ans = [m]
                max_c = c
        return ans
