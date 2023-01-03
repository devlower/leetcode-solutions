# Root Equals Sum of Children

#### You are given the `root` of a binary tree that consists of exactly `3`nodes: the root, its left child, and its right child.

#### Return `true` *if the value of the root is equal to the sum of the values of its two children, or* `false` *otherwise.*

### Example 1:

<p align="left">
  <img src="src/ex1.png" alt="Example 1" width="250">
</p>

```
Input: root = [10,4,6]
Output: true
Explanation: The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.
```

### Example 2:

<p align="left">
  <img src="src/ex2.png" alt="Example 2" width="250">
</p>

```
Input: root = [5,3,1]
Output: false
Explanation: The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.
```

### Constraints:: 

- The tree consists only of the root, its left child, and its right child.
- `-100 <= Node.val <= 100`

### Solution explanation:
The `checkTree` function defined in the `Solution` class checks whether a given binary tree satisfies the following condition: for each non-leaf node in the tree, the sum of the values of its left and right child nodes is equal to the value of that node. If this condition is satisfied for all non-leaf nodes in the tree, the function returns `True`, otherwise it returns `False`.

The function first checks whether the root node is `None`. If it is, it returns `True`. This handles the case where the tree is empty.

Next, it checks whether the root node is a leaf node (i.e., it has no children). If it is, the function returns `True`.

If the root node is not `None` and is not a leaf node, the function checks whether it has both a left and a right child. If it does, it checks whether the sum of the values of the left and right child nodes is equal to the value of the root node. If this is the case, it calls the `checkTree` function recursively on the left and right child nodes and returns the logical AND of the results.

If none of the above conditions are met (i.e., the root node is not `None`, is not a leaf node, and does not have both a left and a right child), the function returns `False`.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/root-equals-sum-of-children/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
