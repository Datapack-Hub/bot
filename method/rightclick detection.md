Get more detailed info about individual methods using the respective `/method`s

## Warped Fungus on a Stick (WFOAS)/Carrot on a Stick (COAS)

This method works by using an `item.used` scoreboard objective which triggers when using either of the two items and then running commands as/at players with a score of 1 or higher.

Pros:

- easy to pull off
- works in any world
- doesn't require additional entities

Cons:

- wfoas attracts striders/coas pigs and rabbit

Depends:

- detects up to 5 clicks/second when holding right click

## Food component

This method works by using an item with a very long eating time which will never finish, in combination with an advancement to detect when you begin eating it.

Pros:

- can detect clicks from any item
- works in any world
- doesn't require additional entities
- doesn't need to run every tick
- doesn't attract mobs

Cons:

- only works in 1.20.5+
- slows player down when holding right click

Depends:

- detects up to 20 clicks/second when holding right click
- bound to the player, not a specific location

## Eye of Ender (EoE)

This method works by using an advancement to detect whenever a player uses an eye of ender and then executing code as/at them.

Pros:

- doesn't require additional entities
- doesn't attract mobs
- doesn't need to run every tick

Cons:

- slows player down when holding right click
- only works in worlds without strongholds (there are ways to work around this, although these are way less performant)

Depends:

- detects up to 20 clicks/second when holding right click
- bound to the player, not a specific location

## Interaction Entities

This method works by using an advancement to check whether a player interacted with an interaction entity and then executing code

Pros:

- see "depends"
- can also detect left clicks

Cons:

- requires an additional entity

Depends:

- detects up to 5 clicks/second when holding right click
- bound to a specific location, not player
- can't be interacted through
