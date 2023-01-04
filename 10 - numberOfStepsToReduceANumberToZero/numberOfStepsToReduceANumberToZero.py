class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num != 0:
            count += 1
            num = (num >> 1) if (num & 1 == 0) else (num - 1)

        return count