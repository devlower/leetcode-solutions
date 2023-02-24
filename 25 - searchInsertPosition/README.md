# Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1:

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

### Example 2:

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

### Constraints:

- `1 <= nums.length <= 10^4`.
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10^4 <= target <= 10^4`

## Solution explanation:

The method `searchInsert` takes a list of integers `nums` and an integer `target` as parameters and returns the `index` of the `target` if it is found in `nums`, or the `index` where `target` should be inserted in `nums` to maintain the order.

The search is performed using the [binary search algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm), which works by repeatedly dividing the search interval in half. In this case, the initial search interval is the entire length of `nums`. The `left` and `right` boundaries of the interval are initialized to `0` and `len(nums)-1`, respectively.

The algorithm then enters a `while` loop that continues as long as the `left` boundary is less than or equal to the `right` boundary. Within each iteration of the loop, the midpoint of the current search interval is calculated as `(left+right)//2` using integer division. If the value of `nums[mid]` is equal to the `target`, then the method `returns` the `index` `mid` where the `target` was found.

If the value of `nums[mid]` is less than the `target`, then the search interval is restricted to the right half of the current interval by setting `left = mid + 1`. If the value of `nums[mid]` is greater than the `target`, then the search interval is restricted to the left half of the current interval by setting `right = mid - 1`.

The loop continues until either the `target` is found or the `left` boundary becomes greater than the `right` boundary. If the `target` is not found, the method **returns the value of the left boundary** as the `index` where `target` _should_ be inserted in `nums` to **maintain the order**.

### Overall solution details:

 <p align="center">
    <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/search-insert-position/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
