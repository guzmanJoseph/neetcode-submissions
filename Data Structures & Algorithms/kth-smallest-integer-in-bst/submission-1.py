# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        value = 0
        
        def dfs(root, k):
            nonlocal count, value
            if not root:
                return 0
            
            dfs(root.left, k)

            count += 1

            if count == k:
                value = root.val
                return
            dfs(root.right, k)

            return value
        dfs(root, k)
        return value

        


        