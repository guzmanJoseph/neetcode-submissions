class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = {}

        for i in range(n):
            graph[i] = []

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if dfs(neighbor, node) == False:
                    return False
            return True

        if dfs(0, -1) == False:
            return False

        return len(visited) == len(graph)

        