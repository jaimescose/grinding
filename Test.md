```dataviewjs
let pages = dv.pages('"Coding"').where(p => p.includes("blind75") );
for (let group of pages.groupBy(b => b.primaryCategory)) {
   dv.header(3, group.key);
   dv.table(group.rows.file.name);
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
                  k.file.link,
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