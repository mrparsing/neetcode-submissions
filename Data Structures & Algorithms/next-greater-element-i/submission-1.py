class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1] * len(nums1)
        hashmap = {}

        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
        
        for i in range(len(nums1)):
            index = hashmap[nums1[i]]
            current = nums2[index]
            index += 1
            while index < len(nums2):

                if nums2[index] > current:
                    output[i] = nums2[index]
                    break
                index += 1
        return output