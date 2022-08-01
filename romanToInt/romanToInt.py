class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
        final_sum = 0
        tmp = 0
        i = 0

        while i < len(s):
            tmp = roman_dict[s[i]]
            if (i +1) < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                tmp = roman_dict[s[i + 1]] - roman_dict[s[i]]
                i += 1
            i += 1
            final_sum += tmp

        return final_sum