# Raycasting Guide

**Raycasting** is when we shoot a line from the player's eyes in the direction they are looking. We use this to get what the player is looking at, and do something to it, such as spawning an explosion.

Raycasting is very simple. All we need do is run a **recursive function**. This function will run at the player's eyes, check if there is a block at `~ ~ ~`, and if there is not, then move 0.1 blocks forward and run itself again. This creates a loop, which will eventually hit a block.

**start_raycast** function:
```elixir
# Set the distance limit on the raycast. (10 x limit in blocks, so 1000 would be 100 blocks)
scoreboard players set .limit <any objective> 1000

# Start the raycast
execute at @s anchored eyes positioned ^ ^ ^.1 run function <namespace>:raycast
```
**raycast** function:
```elixir
# Remove one from the limit
scoreboard players remove .limit <objective> 1

# Optional - place a particle, to make the raycast leave a trail
particle minecraft:dust 1 0 0 1 ~ ~ ~

# If the raycast has hit a block, do something
execute unless block ~ ~ ~ #<namespace>:pass_through run setblock ~ ~ ~ diamond_block

# If the raycast hasn't hit a block, continue, but only if the limit is 1 or more (1..)
execute if block ~ ~ ~ #<namespace>:pass_through positioned ^ ^ ^0.1 if score .limit <objective> matches 1.. run function <namespace>:raycast```

namespace/tags/block/**pass_through**.json:```
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