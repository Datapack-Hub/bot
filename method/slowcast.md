If you look this up, I assume you already know what a normal Raycast does.
A Slowcast is similar, but unlike a standard Raycast, it is not instant.
You might think now: "Why do we need a Slowcast for that, you can just teleport a marker slowly forward to do the same?".
You'd be right normally, but now think about having a really fast projectile.
To make it faster you would need to increase the distance the marker TPs ever tick.
This is bad when the gap between the two points becomes too big and doesn't correctly recognize when hitting something.
A Slowcast solves this problem by checking the gap between the two points in 0.2 block steps if it hits something on the way.

How do we make a Slowcast now?

First, add two commands to your load function:

```hs
scoreboard objectives add slowcastSteps dummy
scoreboard objectives add slowcastDuration dummy
```

Now you need an initialization function. This function needs to be executed as and at the player that shoots the Slowcast.

`init.mcfunction`

```hs
summon marker ~ ~ ~ {Tags:["slowcast","new"]}
execute as @e[type=marker,tag=new,limit=1] run function <namespace>:setup
execute as @e[type=marker,tag=new,limit=1] run tp ~ ~1 ~

```

Next is the setup function that gives the marker projectile all the necessary stats.
`setup.mcfunction`

```hs
tag @s remove new

# The temp scoreboards are just to set the steps and duration of the Slowcast before calling it.
scoreboard players operation @s slowcastSteps = steps temp
scoreboard players operation @s slowcastDuration = duration temp

# Here is a bit of math to show how far the Slowcast will travel
#
# slowcastDuration = 50 (50 ticks)
# slowcastSteps = 3 (3 0.2 block steps per tick)
#
# steps * duration / 5 ==> 3 * 50 / 5 = 30 blocks in 50 ticks

function <namespace>:temp_tick
```

Good, the projectile is all setup and has called the temporary tick function, which will run every tick as long as there are active Slowcasts. Let's make it.

`temp_tick.mcfunction`

```hs
execute as @e[type=marker,tag=slowcast,scores={slowcastDuration=1..}] at @s run function <namespace>:duration

execute as @e[type=marker,tag=slowcast,limit=1] run schedule function <namespace>:temp_tick 1t
```

The duration function ensures, that the Slowcast doesn't go on forever and kills it after the duration timer reaches 0.

`duration.mcfunction`

```hs
scoreboard players remove @s slowcastDuration 1

scoreboard players operation slowcastSteps temp = @s slowcastSteps
scoreboard players reset hit temp
execute positioned ^ ^ ^.2 run function <namespace>:step
scoreboard players operation @s slowcastSteps = slowcastSteps temp

execute unless score @s slowcastDuration matches 1.. run kill
```

The step function, as stated in the introduction, is responsible for checking the gap between the two points the marker teleports between in one tick for collisions and ends the function early if it hits something.

`step.mcfunction`

```hs
scoreboard players remove @s slowcastSteps 1

particle flame ~ ~ ~ .1 .1 .1 0 1

execute store result score hit temp as @e[type=!player,type=!item_display,dx=0] positioned ~-.99 ~-.99 ~-.99 if entity @s[dx=0] positioned ~.99 ~.99 ~.99 run function <namespace>:end 
execute if score hit temp matches 1 run kill

tp ~ ~ ~

execute if score @s slowcastSteps matches 1.. positioned ^ ^ ^.2 run function <namespace>:step
```

Now you have the last function necessary for the Slowcast. This one has only one important command for all of this to work, the rest is up to you, what you want to happen when hitting something. In my case, the entity just says hi.

`end.mcfunction`

```hs
say hi

# Here is the return command. It just gives the execute store a result value, that's it
return 1
```

That's it. This is how you make a Slowcast.
If you want you can tweak some parts to do stuff a bit differently, for example, switch the marker with an item display or remove the kill command after hitting something to make it a piercing projectile or much more.
