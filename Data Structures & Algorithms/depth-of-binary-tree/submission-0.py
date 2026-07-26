# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # set max_depth to 0 initially
        max_depth = 0
        
        # base case: empty tree
        if root is None:
            return max_depth
        
        # step case: non-empty tree
        else:
            d1 = self.maxDepth(root.left)
            d2 = self.maxDepth(root.right)
            max_depth = 1 + max(d1, d2)
        
        return max_depth