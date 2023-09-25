`/execute . . .`

*   `... align <axes> -> execute`
*   `... anchored <anchor> -> execute`
*   `... as <targets> -> execute`
*   `... at <targets> -> execute`
*   `... facing (<pos>|entity <targets> <anchor>) -> execute`
*   `... in <dimension> -> execute`
*   `... on <relation> -> execute`
*   `... positioned (<pos>|as <targets>|over <heightmap>) -> execute`
*   `... rotated (<rot>|as <targets>) -> execute`
*   `... store (result|success) . . .`
    *   `... block <targetPos> <path> <type> <scale> -> execute`
    *   `... bossbar <id> (max|value) -> execute`
    *   `... entity <target> <path> <type> <scale> -> execute`
    *   `... score <targets> <objective> -> execute`
    *   `... storage <target> <path> <type> <scale> -> execute`
*   `... summon <entity> -> execute`
*   `... (if|unless) . . .`
    *   `... biome <pos> <biome> -> execute`
    *   `... block <pos> <block> -> execute`
    *   `... blocks <start> <end> <destination> (all|masked) -> execute`
    *   `... data . . .`
        *   `... block <sourcePos> <path> -> execute`
        *   `... entity <source> <path> -> execute`
        *   `... storage <source> <path> -> execute`
    *   `... dimension <dimension> -> execute`
    *   `... function <function> -> execute`
    *   `... entity <entities> -> execute`
    *   `... loaded <pos> -> execute`
    *   `... predicate <predicate> -> execute`
    *   `... score <target> <targetObjective> . . .`
        *   `... (<|<=|=|>|>=) <source> <sourceObjective> -> execute`
        *   `... matches <range> -> execute`
*   `... run <command>`

where `-> execute` represents the start of another subcommand.