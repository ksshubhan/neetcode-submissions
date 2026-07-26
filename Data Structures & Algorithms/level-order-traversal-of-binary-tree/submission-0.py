# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        tree = []
        
        # base case
        if root is None:
            return []
        
        # step case
        while queue:
            level_size = len(queue)
            level = []
            for i in range(0, level_size):
                root = queue.pop(0)
                level.append(root.val)
            
                if root.left:
                    queue.append(root.left)
            
                if root.right:
                    queue.append(root.right)
            
            tree.append(level)

        return tree