# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        pre_index = 0

        def build(start, end):
            nonlocal pre_index
            if start > end:
                return None
            
            root_val = preorder[pre_index]
            pre_index += 1

            root = TreeNode(root_val)

            i = inorder_map[root_val]

            root.left = build(start, i-1)
            root.right = build(i+1, end)

            return root
        
        return build(0, len(inorder)-1)