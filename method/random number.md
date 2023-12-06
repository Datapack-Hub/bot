⚠️ **This is only a viable way of doing this in versions older than 1.20.2. If you are using 1.20.2 or higher, you can just use `/random`!**

Generating a random number is very useful in programming for a variety of reasons, and this is the best way to do it in a Datapack.  Put this in `data/<namespace>/loot_tables/rng.json`:

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 10
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:stone",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": 0
            }
          ]
        }
      ]
    }
  ]
}
```

You can change the values 1 and 10 to change the range. If you leave it as it is, it generates a random number between 1-10.  **To use this**, you just have to store the result of summoning this loot table:```
execute store result . . . run loot spawn ~ ~ ~ loot <namespace>:rng```
This will store the random number in wherever you specified.
