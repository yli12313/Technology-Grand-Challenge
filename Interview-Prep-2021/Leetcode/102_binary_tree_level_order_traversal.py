# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # TC: O(N)
    # SC: O(N/2) -> O(N)

    def levelOrder(self, root):
        res = []

        # TRICK: Have to check the 'not root' case.
        if not root:
            return res

        queue = []
        queue.append(root)

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:  
                        queue.append(node.right)
            
            res.append(level)
    
        return res
