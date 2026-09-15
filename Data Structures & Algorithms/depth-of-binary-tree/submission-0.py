# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.maxDepthHelper(root, 0)

    def maxDepthHelper(self, root: Optional[TreeNode], currMax):
        
        if root is None:
            return currMax
        
        return 1 + max(self.maxDepthHelper(root.left, currMax), self.maxDepthHelper(root.right, currMax))
