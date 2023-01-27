# Contains Duplicate

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1:

```
Input: nums = [1,2,3,1]
Output: true
```

### Example 2:

```
Input: nums = [1,2,3,4]
Output: false
```

### Example 3:

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Constraints:: 

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Solution explanation:

The method `containsDuplicate` takes in one parameter `nums` which is a list of integers. The method returns a Boolean value (`True` or `False`).

The method first converts the input list of integers "`nums` into a set `set_nums`. A set is a collection of unique elements.

Then, the code checks if the `length` of the set is less than the `length` of the input list. If this is true, it means that there were duplicate elements in the input list because the set only contains unique elements. So the method returns `True` indicating that the input list contains duplicate elements. Otherwise, it returns `False` indicating that the input list does not contain duplicate elements.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/contains-duplicate/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
