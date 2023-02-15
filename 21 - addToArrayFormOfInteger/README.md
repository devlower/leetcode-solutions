# Add to Array-Form of Integer

The **array-form** of an integer `num` is an array representing its digits in left to right order.

- For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return _the **array-form** of the integer `num + k`_.

### Example 1:

```
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```

### Example 2:

```
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```

### Example 3:

```
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```

### Constraints:: 

- `1 <= num.length <= 10^4`
- `0 <= num[i] <= 9`
- `num` does not contain any leading zeros except for the zero itself.
- `1 <= k <= 10^4`

## Solution explanation:

The method `addToArrayForm` takes two arguments: a list of integers `num` and an integer `k`. The goal is to add k to the number represented by num and return the result as a list of integers.

The method initializes a few variables: `i` is the index of the current digit in `num`, `carry` is the value that needs to be carried over to the next digit, and `result` is the list that will store the digits of the sum.

The main loop of the function processes the digits of the sum one by one, starting from the least significant digit. The loop continues as long as there are more digits to process (`i >= 0`) or there is still a carry to propagate (`carry != 0`).

At each iteration, the loop checks if there are more digits to process (`i >= 0`). If so, it adds the current digit of `num` to `carry` and decrements `i` to move to the next digit. This step is necessary to ensure that we process all the digits of `num`, even if `k` has more digits.

The loop then computes the current digit of the sum as the remainder of `carry` divided by 10 (`carry % 10`). This digit is added to the result list using the `append` method.

The loop then updates the value of `carry` by integer division (`carry //= 10`), which effectively removes the current digit from `carry` and propagates any carry to the next iteration.

Once the loop finishes, the result list is reversed using the slicing operator `[::-1]` and returned.

Overall, this code implements a simple and efficient algorithm for adding two numbers represented as lists of digits. The key idea is to process the digits one by one and propagate the carry as needed. This approach avoids the need to convert the numbers to strings or perform any other complex operations.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/add-to-array-form-of-integer/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
