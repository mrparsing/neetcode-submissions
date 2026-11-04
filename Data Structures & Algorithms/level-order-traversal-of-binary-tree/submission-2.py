# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        level_curr = [root]
        level_succ = []

        while level_curr:
            res.append([node.val for node in level_curr])
            for node in level_curr:
                if node.left:
                    level_succ.append(node.left)
                if node.right:
                    level_succ.append(node.right)
            level_curr = level_succ
            level_succ = []
        return res