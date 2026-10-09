class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)

        for a in arr:
            if counts[a] == 1:
                k-= 1
                if k == 0:
                    return a
        return ""