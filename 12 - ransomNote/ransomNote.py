class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        for letter, count in ransom_counts.items():
            if count > magazine_counts[letter]:
                return False
        return True
