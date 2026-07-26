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
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        # we do not need to consider subRoot because subRoot is what we are given
        # the only thing stopping our search is we have searched all the way
        # and there is no part of the tree left to search
        # because each node becomes the root in our recursive function
        if root is None:
            return False
        
        # step case
        # we use isSameTree to see if we find subtree within our tree
        if self.isSameTree(root, subRoot):
            return True
        # otherwise we look at the next nodes on either side of the root node
        else:
            # and see from there if they contain the subtree
            # we do not do subRoot.right&left because at each new node
            # of our original tree we are checking if the entire subtree is present
            return (
                self.isSubtree(root.left, subRoot) 
                or 
                self.isSubtree(root.right, subRoot)
            )





