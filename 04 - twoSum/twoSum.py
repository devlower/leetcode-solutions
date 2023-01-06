class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_index = {}

        for i, num in enumerate(nums):
            nums_index[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_index and i != nums_index[target - num]:
                return [i, nums_index[target - num]]
