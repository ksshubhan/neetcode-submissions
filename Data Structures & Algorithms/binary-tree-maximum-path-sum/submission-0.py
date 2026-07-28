# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def dfs(root):
            nonlocal max_sum
            # base case
            if root is None:
                return 0

            # step case
            left_contribution = dfs(root.left)
            right_contribution = dfs(root.right)
            
            left_contribution = max(left_contribution, 0)
            right_contribution = max(right_contribution, 0)
            
            complete_path = left_contribution + root.val + right_contribution
            max_sum = max(max_sum, complete_path)

            if left_contribution > right_contribution:
                return root.val + left_contribution
            else:
                return root.val + right_contribution

        dfs(root)
        return max_sum
        
        