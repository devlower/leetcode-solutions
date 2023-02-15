class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = k
        result = []

        while i >= 0 or carry:
            if i >= 0:
                carry += num[i]
                i -= 1
            result.append(carry % 10)
            carry //= 10

        return result[::-1]