class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        tmp_sum = 0

        for num in nums:
            tmp_sum += num
            result.append(tmp_sum)

        return result

