If you've not made many datapacks, you might not be familiar with raycasting. It's a really useful tool which we can use to essentially find where the player is looking and then do stuff (such as spawn explosions 😎).

To create a raycast, we can use a **recursive function**. A recursive function is a function which will run itself over and over again. In our case, the function will run itself 0.1 blocks forward (`^ ^ ^0.1`) each time, and repeat until it hits something. It will do this all within the same tick - but bear in mind that the bigger the distance, the more laggy it will be. We can stop this unwanted behaviour by putting a distance limit on the raycast - each time it runs itself, it will count down on a scoreboard, and only repeat if it hasn't hit the limit.

**start_raycast** function:

```elixir
# Set the distance limit on the raycast. (10 x limit in blocks, so 1000 would be 100 blocks)
scoreboard players set .limit <objective> 1000

# Start the raycast
execute at @s anchored eyes positioned ^ ^ ^.1 run function <namespace>:raycast```

**raycast** function:```elixir
# Optional - place a particle, to make the raycast leave a trail
particle minecraft:dust 1 0 0 1 ~ ~ ~

# If the raycast has hit a block, do something
execute unless block ~ ~ ~ <namespace>:pass_through run setblock ~ ~ ~ diamond_block

# If the raycast hasn't hit a block, continue
execute if block ~ ~ ~ <namespace>:pass_through positioned ^ ^ ^0.1 run function <namespace>:raycast```

namespace/tags/blocks/**pass_through**.json:```
{
    "replace": false,
    "values": [
        "minecraft:air",
        "minecraft:cave_air",
        "minecraft:void_air"
    ]
}
```

This should be it! Make sure you add all the functions, and fill in all the blanks (indicated by <this>). Then, you can run the start_raycast function as a player, and it should work.
