class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence = defaultdict(int)

        for n in nums:
            frequence[n] += 1
        
        frequence = {k: v for k, v in sorted(frequence.items(), key=lambda item: item[1], reverse=True)}

        output = []

        for v in frequence.keys():
            output.append(v)
            if len(output) == k:
                return output