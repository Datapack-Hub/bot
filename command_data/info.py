INFO = [
    {
        "name": "Logs",
        "content": "When making or debugging Minecraft datapacks, it is useful to have the Minecraft logs open in order to view errors quickly.\n\n**To open the logs:**\n1. Enable the logs in the **Minecraft Launcher** (see image)\n2. Start Minecraft\n\nThe logs should open in a separate window. Datapack errors are shown in the when you `/reload` and are almost always in **red text** or yellow text.",
        "image": "https://media.discordapp.net/attachments/1129493191847071875/1129494068603396096/how-to-logs.png?width=1277&height=897"
    },
    {
        "name": "Logs (non-vanilla)",
        "content": "Opening the Minecraft logs is a bit different on other launchers. **We suggest you use the vanilla Minecraft launcher when making datapacks**. However, if you need to use a modded launcher, this is a guide for the most common ones:\n\n- **Prism Launcher**: `Rightclick Instance` > `Edit` > `Settings` > `Console Settings: Show console while the game is running?`\n- **Multi MC**: `Rightclick Instance` > `Edit Instance` > `Settings` > `Console Settings: Show console while the game is running?`\n- **Lunar Client**: `Settings` > `Open Logs in File Explorer`",
        "image": None
    },
    {
        "name": "Visual Studio Code",
        "content": "Visual Studio Code is the most common text editor for coding in general. For datapacks, there are some required community-made (and mojang-endorsed) extensions for syntax highlighting and autocomplete.\n\n**Download**: https://code.visualstudio.com/\n**Datapack Extensions**: [Datapack Essentials Extension Pack](https://marketplace.visualstudio.com/items?itemName=amandin.dpc-pack)",
        "image": None
    },
    {
        "name": "Updating Resource Packs Past 1.19.3",
        "content": "1.19.3 introduced a change to resourcepacks which means that textures which aren't stored in `textures/item` or `textures/block` won't be loaded into the game by default. This means that most resource packs for earlier versions won't work in 1.19.3.\n\nThere are two ways to fix this:\n- Move your custom textures into `assets/minecraft/textures/item/...`, since all textures in the `item` (or `block`) folders are loaded by default.\n- Create an atlas file for your custom textures. An atlas file basically tells Minecraft to always load the textures in your custom folder. [This video](https://youtu.be/MHWX_GaK2g0) will explain how to do this.",
        "image": None
    },
    {
        "name": "Updating Datapacks Past 1.21",
        "content": "1.21 renamed many folders that make up a Minecraft datapack, breaking virtually all datapacks from prior versions. Now, all folders which previously had plural names, except `tags`, now have singular names.\nBelow is a list of all folder names changed in 1.21:\n`structures` -> `structure`\n`advancements` -> `advancement`\n`recipes` -> `recipe`\n`loot_tables` -> `loot_table`\n`predicates` -> `predicate`\n`item_modifiers` -> `item_modifier`\n`functions` -> `function`\n`tags/functions` -> `tags/function`\n`tags/items` -> `tags/item`\n`tags/blocks` -> `tags/block`\n`tags/entity_types` -> `tags/entity_type`\n`tags/fluids` -> `tags/fluid`\n`tags/game_events` -> `tags/game_event`",
        "image": None
    },
    {
        "name": "AI can't make datapacks",
        "content": "AI generators, such as ChatGPT, Gemini, Claude, and Copilot generally **cannot be used** to make datapacks. While it might look like it gives you good datapack code, in 90% of cases it will not work. There is not enough information online about datapacks in order for them to be accurate. \n\nIf you ask for help with an AI generated datapack, you will likely be asked to start again.",
        "image": None
    }
]