class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        countNeg = 0
        countPos = 0

        for num in nums:
            if num < 0:
                countNeg += 1
            elif num > 0:
                countPos += 1

        if countNeg > countPos:
            return countNeg

        return countPos