class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        res = set()
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        while i < len(nums1) and i < len(nums2):
            if len(nums1) < len(nums2):
                if nums1[i] in nums2Set:
                    res.add(nums1[i])
            else:
                if nums2[i] in nums1Set:
                    res.add(nums2[i])
            i += 1
        return list(res)