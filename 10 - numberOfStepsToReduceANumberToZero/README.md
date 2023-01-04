# Number of Steps to Reduce a Number to Zero

#### Given an integer `num`, return *the number of steps to reduce it to zero.*

#### In one step, if the current number is even, you have to divide it by `2`, otherwise, you have to subtract `1` from it.

### Example 1:

```
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
```

### Example 2:

```
Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
```

### Example 3:

```
Input: num = 123
Output: 12
```

### Constraints:: 

- `0 <= num <= 10^6`

## Solution explanation:
The `numberOfSteps` method takes an integer `num` as input and returns an integer as output.

The method uses a loop to iterate until `num` is equal to 0. At each iteration of the loop, it increments the `count` variable by 1 and then updates the value of `num` using the following logic:

- If `num` is even (that is, if `num & 1` is equal to 0), then `num` is set to `num >> 1`, which is equivalent to num divided by 2.
- If `num` is odd (that is, if `num & 1` is equal to 1), then `num` is set to `num - 1`.

The loop continues to iterate as long as `num` is not equal to 0. When the loop finishes, `count` holds the total number of steps that were taken, so the method returns `count` as the result.

### Further explanation:

In this approah, I use the bitwise operator, which has better performance than the common operators `%` for modulos and `/` for division. 

- The `&` operator is used to check whether a number is odd or even. If `num & 1` is equal to 0, then `num` is even, because the least significant bit (the rightmost bit) is 0. If `num & 1` is equal to 1, then `num` is odd, because the least significant bit is 1.

- The `>>` operator is used to divide `num` by 2 when `num` is even. This is done by shifting the bits of `num` one place to the right, which is equivalent to dividing `num` by 2.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
