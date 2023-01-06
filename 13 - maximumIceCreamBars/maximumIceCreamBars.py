class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        counter = 0

        for price in costs:
            if price <= coins:
                coins -= price
                counter += 1
            else:
                break

        return counter
