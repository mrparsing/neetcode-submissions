class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = buildTree(left, mid-1)
            root.right = buildTree(mid+1, right)

            return root
        root = buildTree(0, len(nums)-1)
        return root