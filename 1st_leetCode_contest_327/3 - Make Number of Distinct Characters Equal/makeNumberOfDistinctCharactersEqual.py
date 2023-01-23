from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        w1c = Counter(word1)
        w2c = Counter(word2)

        print(len(w1c))
        print(len(w2c))
        print(len(word1))
        print(len(word2))


        if len(w1c) == len(word1) and len(w2c) == len(word2) and len(w1c) == len(w2c):
            return True

        if (len(word1) == 1 and len(word2) > len(word1)) or (len(word2) == 1 and len(word1) > len(word2)):
            return False

        for letter1, count1 in w1c.items():
            if count1 > 1:
                tmp1 = word1[:word1.index(letter1)]
                word1 = tmp1 + word1[word1.index(letter1) + 1:]
                for letter2, count2 in w2c.items():
                    if count2 > 1:
                        tmp2 = word2[:word2.index(letter2)]
                        word2 = tmp2 + word2[word2.index(letter2) + 1:]
                        word2 += letter1
                        word1 += letter2
                        if len(Counter(word1)) == len(Counter(word2)):
                            return True
                        else:
                            return False

        return False

        # for letter, count in w1c.items():
        #     if count > 1:




a = Solution()
b = a.isItPossible('aab', 'bccd')
print(b)