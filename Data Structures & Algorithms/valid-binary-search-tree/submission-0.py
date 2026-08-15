# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        interval = [float("-inf"), float("inf")]
        low = interval[0]
        high = interval[1]

        def valid(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            left = valid(node.left, low, node.val)
            right = valid(node.right, node.val, high)

            return left and right

        return valid(root, low, high)

        