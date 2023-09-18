# LINK: https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        # Constraints
        # - The number of nodes in the tree is in the range [1, 200].
        # - Node.val is either 0 or 1.

        # Topic: Recursion
        # This is a Tree, Depth-First Search (DFS) or Binary Tree problem.

        # Approach 1:
        # - If the root is None, return None (This is also the base case for the recursion).
        # - Do DFS and do it in postorder manner.
        # - If you find a node whose value == 0, with no left or right nodes, then prune the node.
        # - Return the root as the answer.

        # TC: O(N)
        # SC: O(H), where H is the height of the tree. 
        #   - The SC can be as bad as O(N), where you have a linked list.
        #   - The SC can be as good as O(log(N)), where to have a balanced binary tree.

        if root is None:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left == None and root.right == None:
            return None
        
        return root
