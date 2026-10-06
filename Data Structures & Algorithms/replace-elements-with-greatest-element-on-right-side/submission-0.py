class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_elem = -1
        ans = [0] * len(arr)
        for i in range(len(arr)-1, -1 , -1):
            ans[i] = max_elem
            max_elem = max(max_elem, arr[i])
        return ans