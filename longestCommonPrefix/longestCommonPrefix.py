class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        letters = []
        result = []
        i = 0

        if len(strs) > 1 and "" not in strs:
            range = len((min((word for word in strs if word), key=len)))

            while i < range:
                index = 0
                while index < len(strs):
                    letters.append(strs[index][i])
                    index += 1
                if len(set(letters)) == 1:
                    result.append(letters[-1])
                    letters = []
                else:
                    break

                i += 1

            if len(result) > 0:
                result = "".join(result)
                return result

            else:
                return ""

        elif len(strs) == 1:
            return strs[0]

        else:
            return ""