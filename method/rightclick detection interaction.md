`interacted_with_interaction.json` (located in the packs `advancement` folder)

```json
{
  "criteria": {
    "requirement": {
      "trigger": "minecraft:player_interacted_with_entity",
      "conditions": {
        "entity": {
          "type": "minecraft:interaction"
        }
      }
    }
  },
  "rewards": {
    "function": "namespace:rightclick_run"
  }
}
```

`rightclick_run.mcfunction` (located in the packs `function` folder)

```hs
# announces the use of the item in chat, feel free to replace this with whatever
say Used interaction 
advancement revoke @s only namespace:interacted_with_interaction
```
