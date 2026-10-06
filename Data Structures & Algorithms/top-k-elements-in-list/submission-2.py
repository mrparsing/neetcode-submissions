class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequence = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for num, cnt in count.items():
            frequence[cnt].append(num)
        
        output = []
        for i in range(len(frequence) - 1, -1, -1):
            for num in frequence[i]:
                output.append(num)
                if len(output) == k:
                    return output