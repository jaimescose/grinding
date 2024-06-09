```dataview
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