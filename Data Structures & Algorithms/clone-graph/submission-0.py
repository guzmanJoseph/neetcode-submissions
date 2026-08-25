
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = set()
        hash_map = {}

        def dfs(current):
            if current in hash_map:
                return hash_map[current]

            copy = Node(current.val)
            hash_map[current] = copy

            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
        
            return copy
        return dfs(node)