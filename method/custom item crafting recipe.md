# ⚠️ This is only a viable way of doing this in versions older than 1.20.5. If you are using 1.20.5 or higher, you can just use a normal recipe and include the custom data in the recipe result.

**This guide assumes that you already have the knowlege of some basic commands as well as on how crafting recipes and advancements work.**

*Text in between `<>`` is aplaceholder for your namespaces and filepaths*

To create a crafting recipe for one of your custom items, you need just a little bit more than for a normal recipe.

Becasue of the fact that you can't use nbt in a recipe, we need a small workaround.

Lets add the recipe first:

> rocket.json
```json
{
    "type": "minecraft:crafting_shaped",
    "pattern": [
        " I ",
        " I ",
        "O O"
    ],
    "key": {
        "I": {
            "item": "minecraft:iron_block"
        },
        "O": {
            "item": "minecraft:obsidian"
        }
    },
    "result": {
        "item": "minecraft:knowledge_book"
    }
}
```

As mentione before, we can't use the custom item as output, so we use a knowledge book as a placeholder.

To switch the knowledge book with our custom item, we need an advancement to react when we craft the recipe. For this we use the `recipe_crafted` trigger.
*With some trickery it is also possible to make the ingredients require certain nbt.*

> craft_rocket.json
```json
{
    "criteria": {
        "requirement": {
            "trigger": "minecraft:recipe_crafted",
            "conditions": {
                "recipe_id": "<namespace>:rocket"
            }
        }
    },
    "rewards": {
        "function": "<namespace>:craft_rocket"
    }
}
```

Last but not least we have to make the function that deals with the item switching.
You can either use a give command or, what I recommend more, define the item in a seperate loot table and use the loot command.

> craft_rocket.mcfunction
```hs
clear @s knowledge_book
loot give @s loot <namespace>:<rocket_item_loot_table>
advancemt revoke @s only <namespace>:craft_rocket
```

This is all you need to create a crafting recipe for your custom items.
