import heapq
import math

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        res = 0
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(k):
            t = heapq.heappop(heap)
            res += -t
            heapq.heappush(heap, -math.ceil(-t / 3))
        return res

a = Solution()

a.maxKelements([1,10,3,3,3], 3)