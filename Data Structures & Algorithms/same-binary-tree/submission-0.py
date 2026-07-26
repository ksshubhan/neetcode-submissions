# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        
        # 1. both empty
        if p is None and q is None:
            return True 
        
        # 2. one is empty and the other is not
        
        # because if q is empty q.left and q.right would yield errors
        # so we have to take care of this beforehand
        if p is None or q is None:
            return False

        # step case
        else:
            # as usual after considering root need to consider left and right subtrees
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
