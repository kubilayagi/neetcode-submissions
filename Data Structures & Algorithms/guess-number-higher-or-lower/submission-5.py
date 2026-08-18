# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n+1
        while l < r:
            g = ((r - l) // 2) + l
            response = guess(g)
            if response == 0:
                return g
            elif response == 1:
                l = g + 1
            else:
                r = g
        return -1