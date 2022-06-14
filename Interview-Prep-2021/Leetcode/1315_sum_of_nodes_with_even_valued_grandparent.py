class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def sumEvenGrandparent(self, root):
    return self.auxiliary(0, root, None, None)
    
  def auxiliary(self, s, cur, gp, p):
    tmp_sum = s
        
    if cur == None:
      return tmp_sum
        
    if gp != None and gp.val % 2 == 0:
      tmp_sum += cur.val
        
    if cur.left:
      tmp_sum = self.auxiliary(tmp_sum, cur.left, p, cur)
    if cur.right:
      tmp_sum = self.auxiliary(tmp_sum, cur.right, p, cur)
        
    return tmp_sum


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