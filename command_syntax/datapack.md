`datapack disable <name>`

`datapack enable <name>`

Enable the specified pack.

`datapack enable <name> (first|last)`

Load this pack before (lowest priority) or after (highest priority) all others (lowest or highest priority).

`datapack enable <name> (before|after) <existing>`

Load this pack just before (lower priority) or after (higher priority) an _existing_ pack.

`datapack list [available|enabled]`

List all data packs, or list only the available/enabled ones. Hovering over the data packs in the chat output shows their description defined in their `pack.mcmeta`.