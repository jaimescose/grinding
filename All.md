
```dataviewjs
let pages = dv.pages('"coding"');
for (let group of pages.groupBy(p => p.category)) {
   dv.header(3, group.key);
   dv.table(
	   ["Name", "Difficulty", "Solved", "Topics", "Pattern", "Time", "Space", "Updated at"],
	   group.rows.sort(k => k.file.mtime, 'desc')
	    .map(k => [
		    k.file.link,
		    k.difficulty === 'hard' ? '🔴' : 
			    k.difficulty == 'medium' ? '🟠' : 
	            k.difficulty == 'easy' ? '🟢' : 
	            '\\-',
	        k.solved ? '✅' : '❌',
	        k.topics,
	        k.oneLiner,
	        k.time,
	        k.space,
	        k.file.mday
	        // Array.from(new Set([...k.file.inlinks, ...k.file.outlinks])) // Combine inlinks and outlinks into a set and convert back to an array
	    ])
   );
}
```