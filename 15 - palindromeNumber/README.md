# Palindrome Number

Given an integer `x`, return `true` _if `x` is a **<span title="Palindrome: An integer is a palindrome when it reads the same forward and backword. For example, 121 is a palindrome whhile 123 is not.">palindrome</span>**, and `false` otherwise._

### Example 1:

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

### Example 2:

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3:

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### Constraints:: 

- `-2^31 <= x <= 2^31 - 1`

### Challenge:

Could you solve it without convertig the integer to a string?

## Solution explanation:
The method `isPalindrome` takes one argument: an integer called `x` and returns a Boolean value indicating whether `x` is a palindrome number or not.

The method first checks if `x` is a negative number. If it is, the method immediately returns `False`, as negative numbers cannot be palindromes.

It then checks if `x` is less than 10. If `x` is less than 10, the method returns `True`, as any single-digit number is a palindrome.

It then checks if `x` is divisible by 10. If it is, the method returns `False`, as numbers ending in 0 cannot be palindromes.

The method then initializes a variable `rev` to 0 and enters a while loop. The loop continues until `x` is less than or equal to `rev`. In each iteration, the value of `rev` is updated by multiplying it by 10 and adding the last digit of `x`. The value of `x` is also updated by removing the last digit.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/palindrome-number/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
