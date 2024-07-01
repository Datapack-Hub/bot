import disnake
import dph
from disnake.ext import commands

FolderStructureType = commands.option_enum(["resourcepack", "datapack"])


class FolderStructureCommand(commands.Cog, name="folderstructure"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="folderstructure",
        description="Shows the folder structure of datapacks/resourcepacks",
    )
    async def folderstructure(
        self, inter: disnake.ApplicationCommandInteraction, type: FolderStructureType = "datapack"
    ):
        match type:
            case "resourcepack":
                embed = disnake.Embed(
                    title="📂 Resourcepack Folderstructure",
                    description="""```
                    .
                    ├── pack.mcmeta
                    ├── pack.png
                    └── assets    
                        ├── icons    
                        ├── minecraft
                        │   ├── sounds.json  
                        │   ├── atlases
                        │   ├── blockstates    
                        │   ├── font    
                        │   ├── icons    
                        │   ├── lang    
                        │   ├── models    
                        │   ├── particles      
                        │   ├── shaders    
                        │   ├── sounds    
                        │   ├── texts
                        |   ├── textures
                        │   └── gpu_warnlist.json        
                        └── realms        
                            ├── lang        
                            └── textures
                            ```""",
                    color=disnake.Colour.orange(),
                )
                await inter.response.send_message(embed=embed)
                
                await dph.log("`/folderstructure` Command", "A user looked up the `resourcepack` folderstructure","orange",self)

            case "datapack":
                embed = disnake.Embed(
                    title="📂 Datapack Folderstructure",
                    description="""```
                .
                ├── pack.mcmeta
                ├── pack.png
                └── data
                    └── <namespace>
                        ├── advancement
                        ├── enchantment
                        ├── enchantment_provider
                        ├── function
                        ├── item_modifier
                        ├── loot_table
                        ├── predicate
                        ├── recipe
                        ├── structure
                        ├── chat_type
                        ├── damage_type
                        ├── trim_material
                        ├── trim_pattern
                        ├── jukebox_song
                        ├── painting_variant
                        ├── wolf_variant
                        ├── tags
                        |   ├── banner_pattern
                        │   ├── block
                        │   ├── cat_variant
                        │   ├── damage_type
                        │   ├── entity_type
                        │   ├── fluid
                        │   ├── function
                        │   ├── game_event
                        │   ├── instrument
                        │   ├── item
                        │   ├── painting_variant
                        │   ├── point_of_interest_type
                        │   └── worldgen
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

                await dph.log("`/folderstructure` Command", "A user looked up the `datapack` folderstructure","orange",self)
