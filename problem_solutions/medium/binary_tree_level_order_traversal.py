'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        nodes = [root]
        while nodes:
            level = []
            new_nodes = []
            for node in nodes:
                level.append(node.val)
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            res.append(level)
            nodes = new_nodes
        return res
