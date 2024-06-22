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

| property   | meaning                                                                                   | type     | Values                                                                                                                                                                                                                                                                |
| ---------- | ----------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| solved     | whether you've solved the problem                                                         | Checkbox | true, false                                                                                                                                                                                                                                                           |
| difficulty | culty assigned by Leetco                                                                  | Text     | easy, medium, hard                                                                                                                                                                                                                                                    |
| category   | it's basically based on the category assigned by [Neetcode](https://neetcode.io/practice) | Text     | Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees, Heap / Priority Queue, Backtracking, Tries, Graphs, Advanced Graphs, 1-D Dynamic Programming, 2-D Dynamic Programming, Greedy, Intervals, Math & Geometry, Bit Manipulation |
| topics     |                                                                                           |          |                                                                                                                                                                                                                                                                       |

## Resources

- Time and space complexity calculator: [Big O Calc](https://www.bigocalc.com/)