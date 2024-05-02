For this example, we will be using a stick for detection. For different items, replace `stick` with the id of your chosen item.
**Note**: You can use any item for this, but if it has existing right-click functionality (like placing a block), it will keep that.

This is the command to give you a stick with the custom food component (You can run this in the chat to test it, or put it in a function to trigger when you want):
```hs
give @s stick[minecraft:food={nutrition:0, saturation:0, can_always_eat:true, eat_seconds:999999999}]
```

`click_food.json` (located in your packs `advancements` folder)

```json
{
  "criteria": {
    "requirement": {
      "trigger": "minecraft:using_item",
      "conditions": {
        "item": {
          "items": [
            "minecraft:stick"
          ]
        }
      }
    }
  },
  "rewards": {
    "function": "namespace:rightclick_run"
  }
}
```

`rightclick_run.mcfunction` (located in your packs `functions` folder)

```hs
# revokes the advancement from the player so it can be used again
advancement revoke @s only namespace:click_food

# announces the use of the item in chat, feel free to replace this with whatever
say I successfully used food component detection!
```
