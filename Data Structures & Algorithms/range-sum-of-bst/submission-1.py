# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.s = 0
        def search(node):
            if not node:
                return
            if low <= node.val <= high:
                self.s += node.val
                search(node.left)
                search(node.right)
            elif node.val > high:
                search(node.left)
            elif node.val < low:
                search(node.right)
        search(root)
        return self.s