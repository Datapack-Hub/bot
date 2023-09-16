import disnake
from disnake.ext import commands
import variables


class FolderStructureCommand(commands.Cog, name="folderstructure"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def folderstructure(self, inter):
        pass

    @folderstructure.sub_command(
        description="Shows the folderstructure for resourcepacks"
    )
    async def resourcepack(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(
            title="Resourcepack Folderstructure",
            description="""```
    .
    ├── pack.mcmeta
    ├── pack.png
    └── assets    
        ├── icons    
        ├── minecraft    
        │   ├── sounds.json    
        │   ├── blockstates    
        │   ├── font    
        │   ├── gpu_warnlist.json    
        │   ├── icons    
        │   ├── lang    
        │   ├── models    
        │   ├── particles    
        │   ├── resourcepacks    
        │   ├── shaders    
        │   ├── sounds    
        │   ├── texts    
        │   └── textures    
        └── realms        
            ├── lang        
            └── textures
            ```""",
            color=disnake.Colour.orange(),
        )
        await inter.response.send_message(embed=embed)
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/folderstructure` Command**"),
            description=(
                str(inter.user.name)
                + " looked up the folderstructure of `resourcepacks`"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)

    @folderstructure.sub_command(description="Shows the folderstructure for datapacks")
    async def datapack(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(
            title="Datapack Folderstructure",
            description="""```
    .
    ├── pack.mcmeta
    ├── pack.png
    └── data
        └── <namespace>
            ├── advancements
            ├── functions
            ├── item_modifiers
            ├── loot_tables
            ├── predicates
            ├── recipes
            ├── structures
            ├── chat_type
            ├── damage_type
            ├── tags 
            │   ├── blocks
            │   ├── entity_types
            │   ├── fluids
            │   ├── functions
            │   ├── game_events
            │   ├── items
            │   ├── chat_type
            │   └── damage_type
            ├── dimension
            ├── dimension_type
            └── worldgen
                ├── biome
                ├── configured_carver
                ├── configured_feature
                ├── density_function
                ├── noise
                ├── noise_settings
                ├── placed_feature
                ├── processor_list
                ├── structure
                ├── structure_set
                ├── template_pool
                ├── world_preset
                └── flat_level_generator_preset
            ```""",
            color=disnake.Colour.orange(),
        )
        await inter.response.send_message(embed=embed)
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/folderstructure` Command**"),
            description=(
                str(inter.user.name) + " looked up the folderstructure of `datapacks`"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
