`advancement (grant|revoke) <targets> everything`

Adds or removes _all_ loaded advancements.

`advancement (grant|revoke) <targets> only <advancement> [<criterion>]`

Adds or removes a single advancement or criterion.

`advancement (grant|revoke) <targets> from <advancement>`

Adds or removes an advancement and _all_ its child advancements.

Think of specifying everything _from_ that advancement to the end.

The exact order the operation is carried out in is `specified advancement > child > child's child > ...` When it operates on a child that branches, it iterates through all its children before continuing.

`advancement (grant|revoke) <targets> through <advancement>`

Specifies an advancement, and adds or removes _all_ its parent advancements, and _all_ its child advancements.

Think of specifying everything _through_ the specified advancement, going both backwards and forwards.

The exact order the operation is as if the command were executed with "until" specified, then with "from" specified: `parent > parent's parent > ... > root > specified advancement > child > child's child > ...`

`advancement (grant|revoke) <targets> until <advancement>`

Adds or removes an advancement and _all_ its parent advancements until the root for addition/removal.

Think of specifying everything from the start _until_ that advancement.

The exact order the operation is carried out in is: `parent > parent's parent > ... > root > specified advancement`.