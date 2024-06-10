```dataviewjs
let pages = dv.pages('"Coding" and #blind75');
for (let group of pages.groupBy(p => p.category)) {
   dv.header(3, group.key);
   dv.table(
	   ["Name", "Difficulty", "Solved", "Updated at", "Pattern", "Similar Questions"],
	   group.rows.sort(k => k.file.mtime, 'desc')
	    .map(k => [
		    k.file.link,
		    k.difficulty === 'hard' ? '🔴' : 
			    k.difficulty == 'medium' ? '🟠' : 
	            k.difficulty == 'easy' ? '🟢' : 
	            '\\-',
	        k.solved ? '✅' : '❌',
	        k.file.mday,
	        k.pattern,
	        ...new Set([...k.file.inlinks, ...k.file.outlinks]) // Combine inlinks and outlinks into a set
	    ])
   );
}
```


```dataview
TABLE choice(myLibrary , "✅", "❌") as Available, ("![|80](" + coverUrl + ")") as Cover, totalPage as "Pages", category as Genre, rating as Rating, dateRead as "Finished"
FROM "Books" AND #literature 
SORT status desc, dateRead desc, title
```