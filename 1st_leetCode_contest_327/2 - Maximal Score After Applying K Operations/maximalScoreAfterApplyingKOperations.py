import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        score = 0

        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            tmp = heapq.heappop(heap)
            score += - tmp
            heapq.heappush(heap, -math.ceil(-tmp / 3))

        return score