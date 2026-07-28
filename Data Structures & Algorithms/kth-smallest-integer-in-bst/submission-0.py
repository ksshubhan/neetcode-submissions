# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while stack or curr is not None:
            
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop(-1)  
            
            k -= 1
            
            if k == 0:
                return curr.val
            else:
                curr = curr.right
