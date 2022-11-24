'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        visited = n * [False]
        visited[source] = True
        connected_edges = {i: [] for i in range(n)}

        for u,v in edges:
            connected_edges[u].append(v)
            connected_edges[v].append(u)

        def depth_first_search(curr, dest, visited):
            for next_step in connected_edges[curr]:
                if next_step == dest:
                    return True
                elif not visited[next_step]:
                    visited[next_step] = True
                    if depth_first_search(next_step, dest, visited):
                        return True
            return False

        return depth_first_search(source, destination, visited)
