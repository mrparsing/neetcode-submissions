# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# n = 100 pick = 73
# lower = 0, upper = 100
# myPick = (lower + upper) // 2 = 50

# lower = 50, upper = 100
# myPick = (100 + 50) // 2 = 75

# lower = 50, upper = pick
# myPick = (lower + upper) // 2 = 62
# lower = 50, upper = 75

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 0, n
        pick = (lower + upper) // 2 + 1

        while True:
            guessRes = guess(pick)
            if guessRes == 0:
                return pick
            elif guessRes == -1:
                upper = pick - 1
            else:
                lower = pick + 1
            pick = (lower + upper) // 2