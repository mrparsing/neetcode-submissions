class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101

        for h in heights:
            count[h] += 1
        
        mismatch = 0
        current_expected_height = 1

        for h in heights:
            while count[current_expected_height] == 0:
                current_expected_height += 1

            if current_expected_height != h:
                mismatch += 1
            count[current_expected_height] -= 1
        return mismatch