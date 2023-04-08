'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def find_nodes_list(node, visits):
            lst = [node]
            new = []
            visits.add(node.val)
            for adj_node in node.neighbors:
                if adj_node.val not in visits:
                    visits.add(adj_node.val)
                    new += find_nodes_list(adj_node, visits)
            return lst + new

        def create_copy_of_nodes(nodes):
            visits = set([])
            nodes = find_nodes_list(node, visits)
            return {n.val: Node(n.val) for n in nodes}

        def create_copy_of_graph(node, duped_nodes):
            nodes_bfs = [node]
            next_level = []
            visits = {node}
            while nodes_bfs:
                for n in nodes_bfs:
                    if n.val not in visits:
                        visits.add(n.val)
                        duped_nodes[n.val].neighbors = [duped_nodes[n_adj.val] for n_adj in n.neighbors]
                        next_level += n.neighbors
                nodes_bfs = next_level
                next_level = []
            return duped_nodes

        if not node:
            return None
        elif not node.neighbors:
            return Node(1)
        visits = set([])
        nodes = find_nodes_list(node, visits)
        duped_nodes = create_copy_of_nodes(nodes)
        copied_graph = create_copy_of_graph(node, duped_nodes)
        return copied_graph[1]
