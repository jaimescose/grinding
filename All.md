
```dataviewjs
let pages = dv.pages('"coding"');
for (let group of pages.groupBy(p => p.category)) {
   dv.header(3, group.key);
   dv.table(
	   ["Name", "Difficulty", "Solved", "Topics", "Solution", "Pattern", "Time", "Space", "Updated at"],
	   group.rows.sort(k => k.file.mtime, 'desc')
	    .map(k => [
		    k.file.link,
		    k.difficulty === 'hard' ? '🔴' : 
			    k.difficulty == 'medium' ? '🟠' : 
	            k.difficulty == 'easy' ? '🟢' : 
	            '\\-',
	        k.solved ? '✅' : '❌',
	        k.topics,
	        k.code,
	        k.oneLiner,
	        k.time,
	        k.space,
	        k.file.mday
	    ])
   );
}
```