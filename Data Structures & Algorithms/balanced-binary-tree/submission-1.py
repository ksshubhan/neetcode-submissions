# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0 

        if root is None:
            return max_depth
        else:
            d1 = self.maxDepth(root.left)
            d2 = self.maxDepth(root.right)

            return 1 + max(d1, d2)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base case
        if root is None:
            return True
        
        # step case
        else:
            curr_balanced = self.maxDepth(root.left) - self.maxDepth(root.right) in [0, 1, -1]
            
            return curr_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)