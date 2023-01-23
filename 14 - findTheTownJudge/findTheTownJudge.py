class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_count = [0] * (n + 1)

        for x, y in trust:
            trust_count[x] -= 1
            trust_count[y] += 1

        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i

        return -1