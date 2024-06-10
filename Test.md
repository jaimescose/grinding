```dataviewjs
let group = dv.pages('"Coding"').where(p => p.includes("blind75") );
for (let group of pages.groupBy(b => b.primaryCategory)) {
   dv.header(3, group.key);
   dv.table(
	   ["Name", "Difficulty", "Solved", "Updated at", "],
	   group.rows.sort(k => k.file.mtime, 'desc')
	    .map(k => [
		    k.file.link,
		    k.difficulty === 'hard' ? '🔴' : 
			    k.difficulty == 'medium' ? '🟠' : 
	            k.difficulty == 'easy' ? '🟢' : 
	            '\\-',
	        k.solved ? '✅' : '❌',
	        k.file.mday,
	        k.pattern
	    ])
   );
}
```

```dataviewjs
for (
  let group of dv.pages('#companies/Amazon')
                 .groupBy(p => p.difficulty)
  ) {
  dv.header(3, group.key?.charAt(0)?.toUpperCase() + group.key?.slice(1));
  dv.table(
    ["Name", "difficulty", "solved"],
    
    group.rows.map(k => [
                  
                  k.difficulty === 'hard' ? '🔴' : 
                    k.difficulty == 'medium' ? '🟠' : 
                    k.difficulty == 'easy' ? '🟢' : 
                    '\\-', 
                  k.solved ? '✔️' : '❌'
                ]
           )
    )
}
```