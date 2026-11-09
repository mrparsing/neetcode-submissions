class Solution:
    def isHappy(self, n: int) -> bool:
        unique = set()

        while True:
            total = 0
            while n > 0:
                cifra = n % 10
                total += cifra**2
                n //= 10
            if total == 1:
                return True
            elif total in unique:
                return False
            unique.add(total)
            n = total