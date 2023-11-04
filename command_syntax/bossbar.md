`bossbar add <id> <name>`

Create a new bossbar.

`bossbar get <id> (max|players|value|visible)`

Return the requested setting as a `result` of the command.

`bossbar list`

Display a list of existing bossbars.

`bossbar remove <id>`

Remove an existing bossbar.

`bossbar set <id> (color|max|name|players|style|value|visible)`

`... color (blue|green|pink|purple|red|white|yellow)`

Set the text color (if no color was specified as part of a text component) and bar color. Defaults to `white` upon creation.

`... max <max>`

Set the bossbar's maximum value. Defaults to `100` upon creation.

`... name <name>`

Set the bossbar's name.

`... players [<targets>]`

Change the set of players to whom the bar is visible. Defaults to none upon creation.

`... style (notched_6|notched_10|notched_12|notched_20|progress)`

Set the bossbar's visual amount of segments: continuous, 6 segments, 10 segments, 12 segments, or 20 segments. Defaults to `progress` upon creation.

`... value <value>`

Set the bossbar's current value. Defaults to `0` upon creation.

`... visible <visible>`

Set the bossbar's visibility. Defaults to `true` upon creation.