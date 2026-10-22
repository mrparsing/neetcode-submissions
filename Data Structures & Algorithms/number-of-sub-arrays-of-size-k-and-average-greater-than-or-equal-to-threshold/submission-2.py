class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # average >= threshold -> sum >= threshold * k
        currSum = sum(arr[:k])
        target = threshold * k
        res = 0
        if currSum >= target:
            res += 1
        for r in range(k, len(arr)):
            currSum += (arr[r] - arr[r - k])
            if currSum >= target:
                res += 1
        return res