# grinding

Obsidian vault to help you keep track of the [Leetcode]([LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/)) problems you've solved, and are willing to solve.

I've organized this vault in such a way that the friction for you to just grab a new problem, analyze it, solve it, and document it, it's the smoothest one possible (given that you've used [Obsidian]() before. Otherwise, would take you some time to get it through the learning curve)

## What you could find

```shel
├── All.md
├── Blind 75.md
├── NeetCode 150.md
├── Pipfile
├── Pipfile.lock
├── Templates
│   ├── Coding template.md
│   └── View.md
├── _assets
└── coding
	├── __init__.py
    ├── Problem.md
    ├── problem.py
    └── test_script.py
```

### Root

Here you could find some predefined table views, built with [Dataview](https://blacksmithgu.github.io/obsidian-dataview/api/intro/) (an Obsidian community plugin), where you could visualize all the problems (Markdown files) within your `/coding` folder

You could show there any property defined in your problem Markdown file. Here is the list of currently supported properties + [Dataviews' Implicit fields](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-pages/#implicit-fields):

| property   | meaning                                                                                                                                                                                                                                                                 | type     | Values                                                                                                                                                                                                                                                                |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| solved     | whether you've solved the problem                                                                                                                                                                                                                                       | Checkbox | true, false                                                                                                                                                                                                                                                           |
| difficulty | difficulty assigned by Leetcode                                                                                                                                                                                                                                         | Text     | easy, medium, hard                                                                                                                                                                                                                                                    |
| category   | it's basically based on the category assigned by [Neetcode](https://neetcode.io/practice)                                                                                                                                                                               | Text     | Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees, Heap / Priority Queue, Backtracking, Tries, Graphs, Advanced Graphs, 1-D Dynamic Programming, 2-D Dynamic Programming, Greedy, Intervals, Math & Geometry, Bit Manipulation |
| topics     | could be seen as a free list where you type the topics you used to solved it (Hash Maps, Arrays, Linked Lists, etc.). Although, I'm filling the property with the topics assigned by Leetcode:<br><br>![[Pasted image 20240621225158.png]]                              | List     | Free                                                                                                                                                                                                                                                                  |
| tags       | tags that would help you classify these problems. Could be: "blind75", neetcode150, or whatever tag you want to put on. However, take into account that the views [[Blind 75]] and [[NeetCode 150]], are based on these tags.<br><br>All the problems would have the "" |          |                                                                                                                                                                                                                                                                       |

## Resources

- Time and space complexity calculator: [Big O Calc](https://www.bigocalc.com/)