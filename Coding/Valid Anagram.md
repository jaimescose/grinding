---
solved: true
difficulty: easy
category: Arrays & Hashing
topics:
  - Hash Table
  - String
  - Sorting
tags:
  - blind75
companies:
  - Uber
link: https://leetcode.com/problems/valid-anagram/description/
solutionLink: 
codeLink: https://github.com/neetcode-gh/leetcode/blob/main/python/0242-valid-anagram.py
premium: false
code: obsidian://open?vault=grinding&file=coding%2F242_valid_anagram.py
---
## Similar Questions

- [[Group Anagrams]]
- [[Palindrome Permutation]]
- [[Find All Anagrams in a String]]
- [[Find Resulting Array After Removing Anagrams]]
## Problem

Given two strings `s` and `t`, return `true` _if_ `t` _is an anagram of_ `s`_, and_ `false` _otherwise_.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** s = "anagram", t = "nagaram"
**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"
**Output:** false

**Constraints:**

- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain [[Unicode characters]]? How would you adapt your solution to such a case?
## Solution

- [oneLiner:: count characters occurrences, store them in a Hash Map, compare then]
- [time:: O(n)]
- [space:: O(n)]

### Explanation

<iframe width="560" height="315" src="https://www.youtube.com/embed/9UtInBqnCgA?si=2aQars0febQ3-TOG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Code

a="race"
b="care"
anagram -> True

a="anagram"
b="nagaram"
anagram -> True

a="rat"
b="car"
anagram -> False

#### Brute Force

- check first if they are equally long
	- no? they are not anagrams
- take character by character from "b" and search it in "a" as it were an array
	- not found? they are not anagrams
- remove it from "a" and "b"
- repeat the process until both are empty

**time:** `O(n^2)`

**space:** `O(1)`

#### Optimized #1

- Sorting both strings
	- optimized [[Sorting Algorithms]] might be:
		- **time:** `O(nLog(n))`
		- **space:** [[Heapsort]] = `O(1)` or [[Merge Sort]] = `O(n)` depending on the algorithm
	- Python uses [[Timsort]]
- Compare them

#### Optimized #2

- loop through both strings while counting the character occurrences
- store them in a dictionary (Hash Map)
- compare these counters

[Code](obsidian://open?vault=grinding&file=coding%2F242_valid_anagram.py)