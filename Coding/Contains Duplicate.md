---
difficulty: easy
topics:
  - Array
  - Hash Table
  - Sorting
solved: true
category: Arrays & Hashing
tags:
  - blind75
companies:
  - Microsoft
link: https://leetcode.com/problems/contains-duplicate/description/
solutionLink: https://www.youtube.com/watch?v=3OamzN90kPg
codeLink: https://github.com/neetcode-gh/leetcode/blob/main/python/0217-contains-duplicate.py
---
## Similar Questions

- [[219. Contains Duplicate II]]
- [[220. Contains Duplicate III]]
- [[2357. Make Array Zero by Subtracting Equal Amounts]]
## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

**Input:** nums = [1,2,3,1]
**Output:** true

**Example 2:**

**Input:** nums = [1,2,3,4]
**Output:** false

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]
**Output:** true

**Constraints:**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
## Solution

- [oneLiner:: store unique numbers in a set and check incoming ones]
- [time:: O(n)]
- [space:: O(n)]

### Explanation

<iframe width="560" height="315" src="https://www.youtube.com/embed/3OamzN90kPg?si=EJn90cCRUKa_-TG2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Code

[Code](obsidian://open?vault=grinding&file=coding%2F217_contains_duplicate.py)