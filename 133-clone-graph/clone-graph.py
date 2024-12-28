"""
Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node):
        adj = {}
        if not node:
            return    
        def dfs(node):
            if not node:
                return 
            if node in adj:
                return adj[node]
            copied = Node(node.val)
            adj[node] = copied
            for node_iter in node.neighbors:
                copied.neighbors.append(dfs(node_iter))
            return copied
        return dfs(node)

        