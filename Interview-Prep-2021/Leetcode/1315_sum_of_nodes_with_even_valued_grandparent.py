# Link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def sumEvenGrandparent(self, root):

    # Pass the root into an auxiliary function. The genius to this solution is that the sum/answer
    # is passed into the function itself and tabulated via recursion!
    return self.auxiliary(0, root, None, None)
    
  def auxiliary(self, s, cur, gp, p):
    # Set a temporary sum as the sum/answer.
    tmp_sum = s
        
    # If the current node is None, then return the sum/answer.
    if cur == None:
      return tmp_sum
        
    # If the grandparent is None and it's an even node, increase the temporary sum by the current node.
    if gp != None and gp.val % 2 == 0:
      tmp_sum += cur.val
        
    # If the left side of the current node is present, recurse on the left node and set the temporary sum as the return value.
    if cur.left:
      tmp_sum = self.auxiliary(tmp_sum, cur.left, p, cur)

    # If the right side of the current node is present, recurse on the right node and set the temporary sum as the return value.
    if cur.right:
      tmp_sum = self.auxiliary(tmp_sum, cur.right, p, cur)
    
    # Return the sum/answer.
    return tmp_sum

# Creating the tree for testing if the algorithm worked correctly.
root_node = TreeNode(6)
root_node.left = TreeNode(7)
root_node.right = TreeNode(8)

root_node.left.left = TreeNode(2)
root_node.left.right = TreeNode(7)

root_node.right.left = TreeNode(1)
root_node.right.right = TreeNode(3)

root_node.left.left.left = TreeNode(9)
root_node.left.right.left = TreeNode(1)
root_node.left.right.right = TreeNode(4)

root_node.right.right.right = TreeNode(5)

foo = Solution();
print(foo.sumEvenGrandparent(root_node));