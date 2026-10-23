class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for s in spells:
            target = math.ceil(success / s)
            value = self.binarySearch(target, potions)
            if value != -1:
                res.append(len(potions)-value)
        return res

    def binarySearch(self, target, potions):
        l, r = 0, len(potions)-1

        while l <= r:
            mid = (l + r) // 2

            if potions[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l