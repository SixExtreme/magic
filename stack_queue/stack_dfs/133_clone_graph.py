# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        return self.DFS(node, dict())

    def DFS(self, node, visit):
        if node.label in visit:
            return visit[node.label]
        clone = UndirectedGraphNode(node.label)
        visit[clone.label] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.DFS(neighbor, visit))
        return clone
