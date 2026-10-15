class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square > num:
                r = mid - 1
            elif square < num:
                l = mid + 1
            else:
                return True
        return False