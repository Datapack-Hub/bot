`... append from (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>]`

`... append string (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>] [<start>] [<end>]`

`... append value <value>`

Append the source data or direct value data onto the _end_ of the pointed-to list.

`... insert <index> from (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>]`

`... insert <index> string (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>] [<start>] [<end>]`

`... insert <index> value <value>`

Insert the source data or direct value data into the pointed-to list as element `<index>`, then shift higher elements one position upward.

`... merge from (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>]`

`... merge string (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>] [<start>] [<end>]`

`... merge value <value>`

Merge the source data or direct value data into the pointed-to object.

`... prepend from (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>]`

`... prepend string (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>] [<start>] [<end>]`

`... prepend value <value>`

Prepend the source data or direct value data onto the _beginning_ of the pointed-to list.

`... set from (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>]`

`... set string (block <sourcePos>|entity <source>|storage <source>) [<sourcePath>] [<start>] [<end>]`

`... set value <value>`

Set the tag specified by `<targetPath>` to the source data or direct value data.