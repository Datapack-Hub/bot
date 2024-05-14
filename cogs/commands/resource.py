import disnake
import variables
import dph
from disnake.ext import commands

resources = commands.option_enum(
    [
        "misode",
        "mcstacker",
        "taglib",
        "minecraft wiki",
        "cloudwolf",
        "crafting (thedestruc7i0n)",
        "smithed",
        "minecraft tools",
        "minecraftjson",
        "mcassets"
    ]
)


class ResourceCommand(commands.Cog, name="resource"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="resource",
        description="Shows links for useful minecraft resources",
    )
    async def resource(
        self, inter: disnake.ApplicationCommandInteraction, resource: resources
    ):
        match resource:
            case "misode":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**📖 Misode**"),
                    description="Awesome website with generators for almost everything. Also contains a technical changelog for new versions, guides on how to use some features, a performance report inspector and more!\n\n**Full list of generators**: Loot Tables, Predicates, Item Modifiers, Advancements, Recipes, Text Components, Damage Types, Chat Types, Trim Materials, Trim Patterns, pack.mcmetas, Dimensions, Dimension Types, Biomes, Configured Carvers, Configured Features, Placed Features, Density Functions, Noise, Noise Settings, Structures, Structure Sets, Processor Lists, Template Pools, World Presets, Flat World Presets, World Settings, Block Tags, Entity Type Tags, Fluid Tags, Game Event Tags, Item Tags, Biome Tags, Structure Tags, Blockstates, Models, Fonts, Atlases\n\nLink: https://misode.github.io/",
                )
            case "mcstacker":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 MCStacker**"),
                    description="Allows you to generate lots of different types of commands! Especially useful for long `/give` commands for items with custom names and lore and other things of the like.\n\nLink: https://mcstacker.net/",
                )
            case "mcassets":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 MC Assets**"),
                    description="A cloud storage for all default files in Minecraft's assets and data folders, plus some additional tags and lists with helpful information.\n\nLink: https://mcasset.cloud/",
                )
            case "taglib":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 Taglib**"),
                    description="A libary of (entity, block, item, etc.) tags containing probably every tag you'll ever need!\n\nLink: https://github.com/HeDeAnTheonlyone/Taglib",
                )
            case "minecraft wiki":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 Minecraft Wiki**"),
                    description="Contains information about everything minecraft, including datapacking related features!\n\nLink: https://minecraft.wiki/",
                )
            case "cloudwolf":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 Cloudwolf**"),
                    description="Great Youtube channel with lots of tutorials and explanations on advanced datapacking!\n\nLink: https://www.youtube.com/@CloudWolfMinecraft",
                )
            case "crafting (thedestruc7i0n)":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 Crafting (thedestruc7i0n)**"),
                    description="Great looking, self explanatory generator for crafting recipes\n\nLink: https://crafting.thedestruc7i0n.ca/",
                )
            case "smithed":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 Smithed**"),
                    description="Great libaries, also has datapacking conventions and allows you to upload your own packs!\n\nLink: https://smithed.dev/",
                )
            case "minecraft tools":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 Minecraft Tools**"),
                    description="General minecraft tools, especially useful in datapacking because of it's tellraw generator!\n\nLink: https://minecraft.tools/",
                )
            case "minecraftjson":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=("**📖 minecraftjson**"),
                    description="JSON generator for tellraws, titles and books!\n\nLink: https://www.minecraftjson.com/",
                )

        await inter.response.send_message(embed=embed)
        
        await dph.log("`/resource` Command", f"A user looked up the `{resource}` resource","orange",self)
