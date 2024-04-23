## Give each player a unique ID
Create a scoreboard in a `load` function that runs on `/reload`
```hs
# namespace:load
scoreboard objectives add playerid dummy
```
Create a function to assign a unique id to the player
```hs
# namespace:assign_id
scoreboard players add .global playerid 1
scoreboard players operation @s playerid = .global playerid
```
Create a `tick` advancement to assign an id to a player when they first join
```json
{
  "criteria": { "requirement": { "trigger": "minecraft:tick" }},
  "rewards": { "function": "namespace:assign_id" }
}
```
## Check if an entity has the same ID as the player
Create a predicate that compares the id
```json
// namespace:match_id
{ "condition": "minecraft:entity_scores", "entity": "this", "scores": {
  "pssll.id.player": {
    "min": { "type": "minecraft:score", "target": { "type": "minecraft:fixed", "name": "#this" }, "score": "playerid" },
    "max": { "type": "minecraft:score", "target": { "type": "minecraft:fixed", "name": "#this" }, "score": "playerid" }
  }}
}
```
To use it in a function, you can do that following
```hs
scoreboard players operation #this playerid = @s playerid
say @e[predicate=namespace:match_id] HAVE THE SAME PLAYERID
```
