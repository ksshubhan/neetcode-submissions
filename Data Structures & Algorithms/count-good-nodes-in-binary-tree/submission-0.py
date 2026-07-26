# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_value):
            if root is None:
                return 0
            else:
                good_nodes = 1 if root.val >= max_value else 0
                
                max_value = max(max_value, root.val)

                good_nodes += dfs(root.left, max_value)
                
                good_nodes += dfs(root.right, max_value)
                
                return good_nodes
            
        return dfs(root, root.val)