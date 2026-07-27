# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # initialise intervals
        lower = float('-inf')
        upper = float('inf')
        
        def dfs(root, lower, upper):
            if root is None:
                return True
            else:
                if root.val <= lower or root.val >= upper:
                    return False
                else:
                    return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)

        return dfs(root, lower, upper)