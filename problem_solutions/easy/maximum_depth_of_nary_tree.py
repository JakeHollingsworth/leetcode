'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''
class Solution:    
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        nodes = [[root, 1]]
        max_depth = 0
        for node, depth in nodes:
            max_depth = max(max_depth, depth)
            for child in node.children:
                nodes.append([child, depth + 1])
        return max_depth
