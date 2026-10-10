class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []

        for a in arr2:
            for i in range(1, count[a]+1):
                res.append(a)
                arr1.remove(a)
        arr1.sort()
        return res + arr1