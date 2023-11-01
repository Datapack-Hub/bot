`team list [<team>]`

Lists all teams, with their display names and the amount of entities in them. The optional `<team>` can be used to specify a particular team.

`team add <team> [<displayName>]`

Creates a team with the given name and optional display name. `<displayName>` defaults to `<team>` when unspecified.

`team remove <team>`

Deletes the specified team.

`team empty <team>`

Removes all members from the named team.

`team join <team> [<members>]`

Assigns the specified entities to the specified team. If no entities is specified, makes the executor join the team.

`team leave <members>`

Makes the specified entities leave their teams.

`team modify <team> <_option_> <_value_>`

Modifies the options of the specified team.