# grinding (WIP)

Obsidian vault to help you keep track of the [Leetcode](https://leetcode.com/) problems you've solved, and are willing to solve.

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

| property   | meaning                                                                                                                                                                                                                                                                                                                                                                                                                    | type                 | Values                                                                                                                                                                                                                                                                |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| solved     | whether you've solved the problem                                                                                                                                                                                                                                                                                                                                                                                          | Checkbox             | true, false                                                                                                                                                                                                                                                           |
| difficulty | difficulty assigned by Leetcode                                                                                                                                                                                                                                                                                                                                                                                            | Text                 | `easy`, `medium`, `hard`                                                                                                                                                                                                                                              |
| category   | it's basically based on the category assigned by [Neetcode](https://neetcode.io/practice)                                                                                                                                                                                                                                                                                                                                  | Text                 | Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees, Heap / Priority Queue, Backtracking, Tries, Graphs, Advanced Graphs, 1-D Dynamic Programming, 2-D Dynamic Programming, Greedy, Intervals, Math & Geometry, Bit Manipulation |
| topics     | could be seen as a free list where you type the topics you used to solved it (Hash Maps, Arrays, Linked Lists, etc.). Although, I'm filling the property with the topics assigned by Leetcode:<br><br>![Pasted image 20240621225158](_assets/Pasted%20image%2020240621225158.png)                                                                                                                                          | List                 | Free text                                                                                                                                                                                                                                                             |
| tags       | tags that would help you classify these problems. Could be: `blind75` `neetcode150`, or whatever tag you want to put on. However, take into account that the views [Blind 75](Blind%2075.md) and [NeetCode 150](NeetCode%20150.md), are based on these tags.<br><br>All the problems would have the `problem` tag to facilitate finding them within Obsidian (given by the **Coding template** within `/Templates` folder) | Obsidian native tags | `problem`, `blind75`, `neetcode150`                                                                                                                                                                                                                                   |
| companies  | list of companies that have used the problem during their interviews. Would be helpful if you desire to create a view for a specific company                                                                                                                                                                                                                                                                               | List                 | Free text                                                                                                                                                                                                                                                             |
| link       | Leetcode link                                                                                                                                                                                                                                                                                                                                                                                                              | Text                 | Valid URL                                                                                                                                                                                                                                                             |
| premium    | whether you need a Leetcode subscription to access the problem                                                                                                                                                                                                                                                                                                                                                             | Checkbox             | true, false                                                                                                                                                                                                                                                           |

## Resources

- Time and space complexity calculator: [Big O Calc](https://www.bigocalc.com/)