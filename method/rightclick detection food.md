This is an example, so you'll need to change a few things for your actual datapack:
- Change `stick` to the item you want to detect
- Change `namespace` to your namespace
- Change `custom_stick` to whatever custom data you want
**Note**: You can use any item for this, but if it has existing right-click functionality (like placing a block), it will keep that.

This is the command to give you a stick with the custom consumable component (You can run this in the chat to test it, or put it in a function to trigger when you want):
```hs
give @s minecraft:stick[minecraft:consumable={consume_seconds:999999999}, minecraft:custom_data={custom_stick:true}]
```

`click_consumable.json` (located in your pack's `advancement` folder)

```json
{
  "criteria": {
    "requirement": {
      "trigger": "minecraft:using_item",
      "conditions": {
        "item": {
          "items": [
            "minecraft:stick"
          ],
          "predicates": {
            "minecraft:custom_data": {"custom_stick": true}
          }
        }
      }
    }
  },
  "rewards": {
    "function": "namespace:rightclick_run"
  }
}
```

`rightclick_run.mcfunction` (located in your pack's `function` folder)

```hs
# revokes the advancement from the player so it can be used again
advancement revoke @s only namespace:click_consumable

# announces the use of the item in chat, feel free to replace this with whatever
say I successfully used consumable component detection!
```

## How it works
We've added a consumable component to our custom stick item, allowing it to be consumed like food. The player won't actually eat it, since `eat_seconds` is set to `999999999`, so it would take them over 30 years. The consumable component lets the player try to eat it, which can be detected using an advancement. That advancement runs a function which removes the advancement so it can be triggered again next tick, and runs whatever code you want to the item to trigger.
