# Add Binary

Given two binary strings `a` and `b`, return _their sum as a binary string_.

### Example 1:

```
Input: a = "11", b = "1"
Output: "100"
```

### Example 2:

```
Input: a = "1010", b = "1011"
Output: "10101"
```

### Constraints:: 

- `1 <= a.length, b.length <= 104`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## Solution explanation:

The method `addBinary` takes two string arguments `a` and `b`, which represent two binary numbers, and returns the sum of the two binary numbers as a binary string. 

To add the two binary strings, the method converts them to integers using the `int()` function with a base of 2. This works because the base-2 representation of a binary string is equivalent to the decimal representation of the same number.

Once the binary strings are converted to integers, the method adds them together using the `+` operator. This produces the sum of the two binary numbers as a decimal integer.

To convert the decimal integer back to a binary string, the method uses the `bin()` function. This function takes a decimal integer as input and returns a string that represents the same number in binary. The resulting string has the prefix "0b", which indicates that it represents a binary number.

To remove the "0b" prefix from the binary string, the method uses string slicing. The `[2:]` notation specifies that the method should return the string starting from the third character (i.e., the character at index 2) and continuing to the end. This removes the prefix and returns only the binary digits.

Finally, the method returns the binary string that represents the sum of the two binary numbers.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/add-binary/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
