# Ransom Note

#### Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote` *can be constructed by using the letters from* `magazine` *and* `false` *otherwise.*

#### Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1:

```
Input: ransomNote = "a", magazine = "b"
Output: false
```

### Example 2:

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

### Example 3:

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

### Constraints:: 

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Solution explanation:
This solution uses the `Counter` class from the `collections` module to count the frequency of each letter in the `ransomNote` and `magazine` strings.

- The `Counter` class is used to create two dictionaries: `ransom_counts` and `magazine_counts`. Each dictionary maps a letter to the number of times it appears in the corresponding string.
- A `for` loop iterates over the items in `ransom_counts`. The `items()` method returns a list of tuples, where each tuple consists of a letter and the number of times it appears in `ransomNote`.
- Inside the loop, an `if` statement checks if the count of the current letter in `ransom_counts` is greater than the count of the same letter in `magazine_counts`. If this is the case, the function returns `False`.
- If the loop finishes executing without returning `False`, the function returns `True`.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/ransom-note/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
