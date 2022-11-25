'''
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
'''
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = [root]
        avgs = [root.val]
        while nodes:
            level = []
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                avg = sum([x.val for x in level if x]) / len(level)
                avgs.append(avg)
            nodes = level
        return avgs
