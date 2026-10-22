# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 3:
            return self.evaluateTree(root.right) and self.evaluateTree(root.left)
        elif root.val == 2:
            return self.evaluateTree(root.right) or self.evaluateTree(root.left)
        elif root.val == 0:
            return False
        else:
            return True