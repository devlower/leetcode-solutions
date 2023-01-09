# Maximal Score After Applying K Operations

You are given a **0-indexed** integer array `nums` and an integer `k`. You have a starting score of `0`.

In one **operation**:

choose an index `i` such that `0 <= i < nums.length`, increase your **score** by `nums[i]`, and replace `nums[i]` with `ceil(nums[i] / 3)`.

Return *the maximum possible **score** you can attain after applying **exactly** `k` operations.* 

The ceiling function `ceil(val)` is the least integer greater than or equal to `val`.

### Example 1:

```
Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
```

### Example 2:

```
Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
```

### Constraints:: 

- `1 <= nums.length, k <= 10^5`
- `<= nums[i] <= 10^9`

## Solution explanation:
The method `maxKelements` takes in two arguments:

- a list of integers `nums`
- an integer `k`

The method returns an integer, which is the sum of the k largest elements in the input list `nums`, after dividing each element by 3 and rounding up to the nearest integer.

The method first initializes an empty list `heap` and a variable `score` to 0. It then iterates through the elements `num` in the input list `nums`, and pushes each element onto the heap as a negative value using the `heappush` function from the `heapq` module. This is because the `heapq` module implements a heap as a list, and by default it is a min-heap where the smallest element is at the top. By pushing the negative of each element, I am effectively creating a max-heap where the largest element is at the top.

Next, the method enters a loop that will run `k` times. On each iteration of the loop, it pops the top element (which is the largest element in the heap) from the heap using the `heappop` function, and adds its absolute value to the `score`. It then pushes the result of dividing the absolute value of the popped element by 3 and rounding up to the nearest integer onto the heap.

Finally, the method returns the value of `score`, which is the sum of the `k` largest elements in the input list `nums`, after dividing each element by 3 and rounding up to the nearest integer.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/contest/weekly-contest-327/problems/maximal-score-after-applying-k-operations)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
