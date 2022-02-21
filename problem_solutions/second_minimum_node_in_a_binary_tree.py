'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
'''
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        possibilities = []
        copy = root
        while root and root.left and root.right:
            maxi = max(root.left.val, root.right.val)
            if maxi != copy.val:
                possibilities.append(maxi)
            if root.left.val == root.right.val:
                second_sol = self.findSecondMinimumValue(root.right)
                if second_sol > 0:
                    possibilities.append(second_sol)
            root = root.left if root.left.val <= root.right.val else root.right
        print(possibilities)
        return min(possibilities) if possibilities else -1

