from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = 0
        queue = deque([(root, float('-inf'))])

        while queue:
            node, max_so_far = queue.popleft()

            if node.val >= max_so_far:
                result += 1

            maximum = max(node.val, max_so_far)

            if node.left:
                queue.append((node.left, maximum))

            if node.right:
                queue.append((node.right, maximum))
        return result
                
        