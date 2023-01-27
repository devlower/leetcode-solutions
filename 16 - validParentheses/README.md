# Valid Parentheses

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type.

### Example 1:

```
Input: s = "()"
Output: true
```

### Example 2:

```
Input: s = "()[]{}"
Output: true
```

### Example 3:

```
Input: s = "(]"
Output: false
```

### Constraints:: 

- `1 <= s.length <= 10^4`
- s consists of parentheses only `'()[]{}'`.

## Solution explanation:

 The method `isValid` takes a string `s` as input and returns a boolean value indicating whether the string of brackets is valid or not.

The function uses a stack data structure to keep track of the brackets. The `valid` dictionary maps an opening bracket to its corresponding closing bracket.

The code iterates through each character `c` in the input string `s`.

If `c` is an opening bracket, it is pushed onto the stack.

If `c` is a closing bracket, the code checks whether the stack is empty or the last element on the stack is not the corresponding opening bracket. If either of these conditions is true, the function returns `False` as the string is not valid.

Finally, after all characters have been processed, if the stack is empty, it means that all opening brackets have been matched with closing brackets and the function returns `True` else `False`.

In short, this code checks the balance of opening and closing brackets in a given string. If all brackets are closed properly, the function returns true else false.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/valid-parentheses/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
