`used_eye_of_ender.json` (located in your packs `advancement` folder, you can also add an nbt tag to the nbt field in `items` to make this only run when specific eoes are used)

```json
{
  "criteria": {
    "requirement": {
      "trigger": "minecraft:using_item",
      "conditions": {
        "item": {
          "items": [
            "minecraft:ender_eye"
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

`rightclick_run` (located in your packs `function` folder)

```hs
# announces the use of the item in chat, feel free to replace this with whatever
say Used eoe
# revokes the advancement from the player so it can be used again
advancement revoke @s only namespace:used_eye_of_ender
```

If you want this method to work in worlds with strongholds, you can either block the target of ender eyes in the pack.mcmeta or killing the eye and giving it back after it being used.
