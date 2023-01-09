# Maximum Ice Cream Bars

#### It is a sweltering summer day, and a boy wants to buy some ice cream bars.

#### At the store, there are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the price of the `ith` ice cream bar in `coins`. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

#### *Return the maximum number of ice cream bars the boy can buy with* `coins`.

*Note:* The boy can buy the ice cream bars in any order.

### Example 1:

```
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
```

### Example 2:

```
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.
```

### Example 3:

```
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
```

### Constraints:: 

- `costs.length == n`
- `1 <= n <= 10^5`
- `1 <= costs[i] <= 10^5`
- `1 <= coins <= 10^8`

## Solution explanation:
The method `maxIceCream` takes two arguments: a list of integers called `costs` and an integer called `coins`.

The method first sorts the `costs` list in ascending order. It then initializes a `counter` variable to 0.

Next, it begins a loop that iterates over each element, `price`, in the `costs` list. For each iteration, it checks if the value of `price` is less than or equal to `coins`. If this condition is true, it subtracts `price` from `coins` and increments the `counter` by 1. If the condition is false, the loop breaks.

Finally, the method returns the value of the `counter` variable, which will be the maximum number of ice creams that the boy can buy.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/maximum-ice-cream-bars/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
