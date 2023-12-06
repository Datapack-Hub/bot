For the sake of simplicity the following example will use a coas, if you want to change that you can just `carrot_on_a_stick` in the load function with `warped_fungus_on_a_stick`!

`load.mcfunction`

```hs
# adds the objective to be usable later on
scoreboard objectives add rightclick minecraft.used:minecraft.carrot_on_a_stick 
```

`main.mcfunction`

```hs
# runs the "rightclick_run" as players who used a coas (you can also specify special item nbt here by using a predicate or using "execute if data entity @s", you will still have to reset the score on EVERY click if you don't want the pack to break tho)
execute as @a[scores={rightlick=1}] run function namespace:rightclick_run 
```

`rightclick_run.mcfunction`

```hs
# announces the use of the item in chat, feel free to replace this with whatever
say Used COAS 
# sets the rightclick score to 0 so it can be used again
scoreboard players set @s rightclick 0 
```
