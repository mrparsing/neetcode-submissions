class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        count1 = Counter(s1)
        count2 = Counter(s2[:n1])

        for r in range(n1, n2):
            if count1 == count2:
                return True
            
            left_char = s2[r - n1]
            count2[left_char] -= 1
            if count2[left_char] == 0:
                del count2[left_char]
            
            count2[s2[r]] += 1
        return count1 == count2