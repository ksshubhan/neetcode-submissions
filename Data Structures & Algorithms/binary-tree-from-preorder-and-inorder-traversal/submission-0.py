# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        # if either list is empty then stop
        # because there is no subtree to build
        if not preorder or not inorder:
            return None
        
        # from preorder traversal the first element will always be the 
        # root node of the entire tree
        root = TreeNode(preorder[0])

        # now we find the position on our root node in the inorder
        # because inorder is left-root-right so every node on the left of 
        # our root belongs on the left and vice versa
        index = inorder.index(preorder[0])

        # so now we recursively call the funtion to find left and right nodes
        # by extract different parts of inorder and preorder each call
        # inorder is straightforward for root.left we extract all the nodes
        # left our of root node's position in the inorder
        # and for root.right we extract all the nodes right of our root node's
        # position in the inorder
        # for root.left in the preorder we skip the root and take exactly index nodes
        # for root.right after we have taken the root node and the left subtree nodes
        # everything left must be for the right so we take the nodes starting 
        # from the position after taking index nodes 
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        
        # we return root which will return reconstructed tree 
        return root

        
