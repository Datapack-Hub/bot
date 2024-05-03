In Minecraft, you can create arrays within data storages like this:

```hs
data merge storage namespace:main {array:[1,2,3,4,5]}
```

Array iteration allows you to **check each array element individually** and perform actions on them.

For this example, let's use the previously created array and print out each element individually. Our first step is to create an initializing function that will call our main function at the end:
`namespace:array_iteration/init`

```hs
# Get amount of all the elements in the array to avoid looping twice.
execute store result score $len OBJECTIVE run data get storage namespace:main array[]

# Set current amount of iterations to 0
scoreboard players set $current OBJECTIVE 0

function namespace:array_iteration/main
```

Next, we create our main function:
`namespace:array_iteration/main`

```hs
# Print out current element
tellraw @a {"storage":"namespace:main","nbt":"array[0]"}

# Indicate successful iteration
scoreboard players add $current OBJECTIVE 1

# Switch onto the next element in the array
data modify storage namespace:main array append from storage namespace:main array[0]
data remove storage namespace:main array[0]

# Call itself unless it exceeded array's length
execute unless score $current OBJECTIVE >= $len OBJECTIVE run function namespace:array_iteration/main
```

This is was a basic example of array iteration in minecraft.
