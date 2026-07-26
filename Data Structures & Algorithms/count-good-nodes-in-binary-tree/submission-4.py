# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # we define a good node as a node that is greater than or equal to 
    # all the other nodes in the path to that node
    def goodNodes(self, root: TreeNode) -> int:

        # perform a dfs and for each node check if it is greater than or
        # equal to the max_value; if it is then we have found a good node
        def dfs(root, max_value):
            # base case
            if root is None:
                return 0
            
            # step case 
            else:
                # if the current node is greater than max_value set good_nodes
                # to 1 else set it to 0
                good_nodes = 1 if root.val >= max_value else 0
                
                # update max_value
                max_value = max(max_value, root.val)

                # traverse left and right subtree add either 0 or 1 to the
                # total number of good nodes accordingly
                good_nodes += dfs(root.left, max_value)
                good_nodes += dfs(root.right, max_value)
                
                # return number of good nodes found so far
                return good_nodes
        
        # This starts the process 
        # at the end the final good_nodes returned will be the total number
        # of good nodes in the tree
        return dfs(root, root.val)