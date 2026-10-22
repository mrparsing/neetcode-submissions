class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k
        res = 0

        while r <= len(arr):
            subArrayAverage = sum(arr[l:r]) // len(arr[l:r])
            if subArrayAverage >= threshold:
                res += 1
            l += 1
            r += 1
        return res