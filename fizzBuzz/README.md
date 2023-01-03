# Fizz Buzz

#### Given an integer `n`, return *a string array* `answer` *(1-indexed) where*:
- `answer[i] == "FizzBuzz"` if `i` is divisible by `3` and `5`.
- `answer[i] == "Fizz"` if `i` is divisible by `3`.
- `answer[i] == "Buzz"` if `i` is divisible by `5`.
- `answer[i] == i` (as a string) if none of the above conditions are true.

### Example 1:

```
Input: n = 3
Output: ["1","2","Fizz"]
```

### Example 2:

```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
```

### Example 3:

```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

### Constraints:: 

- `1 <= n <= 10^4`

## Solution explanation:
The `fizzBuzz` method takes an input `n`, which is an integer, and returns a list of strings as output.

The method first initializes an empty list called `result`. It then iterates through the range of integers from 1 to `n + 1` using a `for` loop. For each integer `num` in the range, the code checks if `num` is divisible by both 3 and 5. If it is, the string 'FizzBuzz' is appended to `result`. If `num` is only divisible by 3, the string 'Fizz' is appended to `result`. If `num` is only divisible by 5, the string 'Buzz' is appended to `result`. If num is not divisible by 3 or 5, the string `f'{num}'` is appended to `result`. This is the string representation of `num`, with `f` indicating that this is an "f-string", which is a string that can contain formatted expressions (in this case, `num`).

Finally, the method returns the list `result`.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/fizz-buzz/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
