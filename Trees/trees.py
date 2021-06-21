Class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = None
    self.right = None
    

Class Tree:
  def __init__(self):
    root = TreeNode(None)
    
  def inorder_traversal(self, root):
    if root:
      return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
    else:
      return []
