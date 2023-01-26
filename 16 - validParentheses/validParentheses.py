class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in valid.keys():
                stack.append(c)
            elif len(stack) == 0 or c != valid[stack.pop()]:
                return False

        return len(stack) == 0