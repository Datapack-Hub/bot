`attribute <target> <attribute> get [<scale>]`

Returns the total value of the specified attribute.

`attribute <target> <attribute> base get [<scale>]`

Returns the base value of the specified attribute.

`attribute <target> <attribute> base set <value>`

Overwrites the base value of the specified attribute with the given value.

`attribute <target> <attribute> modifier add <uuid> <name> <value> (add|multiply|multiply_base)`

Adds an attribute modifier with the specified properties if no modifier with the same UUID already existed.

`attribute <target> <attribute> modifier remove <uuid>`

Removes the attribute modifier with the specified UUID.

`attribute <target> <attribute> modifier value get <uuid> [<scale>]`

Returns the value of the modifier with the specified UUID.