import disnake
import dph
from disnake.ext import commands

INFO = [
    {
        "name": "Output Logs",
        "about": "The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! To open the logs:\n 1. **Enable** logs in the Minecraft **Launcher** \n2. **Start** your **game** (or restart it if you already have an open instance) \n3. Enjoy **spotting errors** getting much **easier**!",
        "image": "https://media.discordapp.net/attachments/1129493191847071875/1129494068603396096/how-to-logs.png?width=1277&height=897"
    },
    {
        "name": "Output Logs (other launchers)",
        "about": "The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! Opening logs works different for different 3rd party launchers, here's a quick summary for the most popular ones:\n\n**Prism Launcher**\n`Rightclick Instance` > `Edit` > `Settings` > `Console Settings: Show console while the game is running?`\n\n**Multi MC**\n`Rightclick Instance` > `Edit Instance` > `Settings` > `Console Settings: Show console while the game is running?`\n\n**Lunar Client**\n`Settings` > `Open Logs in File Explorer`",
        "image": None
    },
    {
        "name": "Datapack Helper",
        "about": "Datapack Helper is a public discord bot run by [Datapack Hub](https://datapackhub.net). I have features such as:\n- Automatic syntax highlighting for mcfunction\n- Commands for resources, information about datapacks, guides, and more!\n- Commands for finding pack formats, folder structures\n- Syntax for all minecraft commands\n- Exhaustive guides for common datapacking concepts\n\n**Invite**: https://bot.datapackhub.net/",
        "image": None
    },
    {
        "name": "Visual Studio Code",
        "about": "Visual Studio Code is the most common code editor for datapacks. It is multipurpose for all files and programming languages, but there are special community-made (and mojang-endorsed) extensions for creating datapacks.\n\n**Download**: https://code.visualstudio.com/\n**Datapack Extensions**: [Datapack Essentials Extension Pack](https://marketplace.visualstudio.com/items?itemName=amandin.dpc-pack)",
        "image": None
    },
    {
        "name": "Updating Resource Packs Past 1.19.3",
        "about": "1.19.3 introduced a change to resourcepacks which means that textures which aren't stored in `textures/item` or `textures/block` won't be loaded into the game by default. This means that most resource packs for earlier versions won't work in 1.19.3.\n\nThere are two ways to fix this:\n- Move your custom textures into `assets/minecraft/textures/item/...`, since all textures in the `item` (or `block`) folders are loaded by default.\n- Create an atlas file for your custom textures. An atlas file basically tells Minecraft to always load the textures in your custom folder. [This video](https://youtu.be/MHWX_GaK2g0) will explain how to do this.",
        "image": None
    },
    {
        "name": "Updating Datapacks Past 1.21",
        "about": "1.21 renamed many folders that make up a Minecraft datapack, breaking virtually all datapacks from prior versions. Most plural folder names were renamed to their singular variant. For example, the `functions` folder in previous versions is now named `function`. The only folder that is still plural is `tags`.\nBelow is a list of all folder names changed in 1.21:\n`structures` -> `structure`\n`advancements` -> `advancement`\n`recipes` -> `recipe`\n`loot_tables` -> `loot_table`\n`predicates` -> `predicate`\n`item_modifiers` -> `item_modifier`\n`functions` -> `function`\n`tags/functions` -> `tags/function`\n`tags/items` -> `tags/item`\n`tags/blocks` -> `tags/block`\n`tags/entity_types` -> `tags/entity_type`\n`tags/fluids` -> `tags/fluid`\n`tags/game_events` -> `tags/game_event`",
        "image": None
    }
]



class InfoCommand(commands.Cog, name="info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="info",description="Show information about certain features")
    async def info(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        info: str = commands.Param(choices=[item["name"] for item in INFO])
    ):
        current = next((item for item in INFO if item["name"] == info), None)
        if not current:
            return await inter.response.send_message(f"The info `{info}` does not exist.",ephemeral=True)

        embed = disnake.Embed(
            color=disnake.Colour.orange(), 
            title=current["name"],
            description=current["about"]
        )
        
        if current["image"] is not None:
            embed.set_image(current["image"])
            
        await inter.response.send_message(embed=embed)
        
        await dph.log("`/info` Command", f"A user looked up the `{info}` info","orange",self)