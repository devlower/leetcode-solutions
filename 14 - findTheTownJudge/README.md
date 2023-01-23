# Find the Town Judge

In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties **1** and **2**.

You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`.

Return *the label of the town judge if the town judge exists and can be identified, or return `-1` otherwise*.

### Example 1:

```
Input: n = 2, trust = [[1,2]]
Output: 2
```

### Example 2:

```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```

### Example 3:

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

### Constraints:: 

- `1 <= n <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- All the pairs of `trust` are **unique**.
- `ai != bi`
- `1 <= ai, bi <= n`

## Solution explanation:
The method `findJudge` takes two arguments: an integer called `n` and a list of lists of integers called `trust`.

The method first initializes an array `trust_count` of size `n + 1` and sets all elements to 0. This array will keep track of the number of people that trust each person.

It then iterates through the pairs of trust relationships in the input `trust` list, and for each pair, it decrements the trust_count of the person who trusts (x) and increments the trust_count of the person being trusted (y).

After that, it iterates through the trust_count array, starting from the first element (index 1), and checks if the trust_count of any person is equal to n-1, if so it returns that person's index (i) as the judge. Else it returns -1.

So the solution works by counting the number of people that trust each person, and returning the person who is trusted by n-1 people as the town judge.

### Overall solution details:

<p align="center">
  <img src="src/solutionDetails.png" alt="Solution Details" width="650">
</p>

Try yourself to so solve this [Problem](https://leetcode.com/problems/find-the-town-judge/)!
<br>
Exercise your coding skills at [LeetCode](https://leetcode.com)!

<p align="center">
  <img src="src/bat.png" alt="devlower logo" width="150">
</p>
