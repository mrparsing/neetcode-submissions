class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}

        for p, s in zip(position, speed):
            hashmap[p] = s
        
        hashmap = dict(sorted(hashmap.items(), reverse=True))
        
        stack = []

        for pos, sp in hashmap.items():
            res = (target - pos) / sp
            
            if not stack or res > stack[-1]:
                stack.append(res)
        
        return len(stack)