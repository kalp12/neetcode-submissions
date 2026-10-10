"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, vis):
        if node in vis:
            return vis[node]
        cloned_node = Node(node.val)
        vis[node] = cloned_node
        for nei in node.neighbors:
            cloned_node.neighbors.append(self.dfs(nei, vis))
        return cloned_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return 
        return self.dfs(node, {})