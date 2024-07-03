import disnake
import dph
from disnake.ext import commands

RESOURCES = [
    {
        "name":"Misode",
        "about":"misode.github.io is the most popular site for JSON datapack generators. This site has generators for commonly used files such as advancements, recipes, and more, as well as datapack changelogs, debug inspectors, and more.",
        "link":"https://misode.github.io/"
    },
    {
        "name":"MCStacker",
        "about":"MCStacker is a Minecraft command generator, focusing on generating commands with NBT/item components easily without having to write long commands by hand.",
        "link":"https://mcstacker.net/"
    },
    {
        "name":"Taglib",
        "about":"Taglib by HeDeAn is a repopsitory containing loads of useful entity, block, and item tags for almost any use case.",
        "link":"https://github.com/HeDeAnTheonlyone/Taglib"
    },
    {
        "name":"Minecraft Wiki",
        "about":"The Minecraft Wiki is a community-built wiki for Minecraft. It has loads of articles on useful features for datapacks.",
        "link":"https://minecraft.wiki/"
    },
    {
        "name":"Cloud Wolf",
        "about":"Cloud Wolf is a youtuber covering loads of key datapacking concepts in videos targeted at intermediate and advanced datapackers - beginners might find it difficult to understand them.",
        "link":"https://www.youtube.com/@CloudWolfMinecraft"
    },
    {
        "name":"Crafting (TheDestruc7i0n)",
        "about":"TheDestruc7i0n's crafting generator is a super easy way to generate crafting recipes instantly for use in datapacks.",
        "link":"https://crafting.thedestruc7i0n.ca/"
    },
    {
        "name":"Smithed",
        "about":"Smithed is a community project aiming to provide a platform to share datapacks and remove all compatibility issues with datapacks. Following Smithed's conventions on compatibility make it easier for datapacks to work together",
        "link":"https://smithed.net/"
    },
    {
        "name":"Minecraft Tools",
        "about":"Minecraft Tools has a really intuitive and easy GUI editor for JSON text and tellraw editor which makes creating nice-looking tellraw messages super easy",
        "link":"https://minecraft.tools/"
    },
    {
        "name":"MinecraftJson",
        "about":"MinecraftJson is a more advanced online JSON text/tellraw editor for more advanced datapackers to create customised JSON text.",
        "link":"https://minecraftjson.com/"
    },
    {
        "name":"mcmeta (vanilla files)",
        "about":"mcmeta (by Misode) is a repository containing all of the vanilla assets, data, commands, and version data for Minecraft Java edition.",
        "link":"https://github.com/misode/mcmeta"
    }
]


class ResourceCommand(commands.Cog, name="resource"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(title="resource",description="Shows links for useful datapack-related resources")
    async def resource(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        resource: str = commands.Param(choices=[item["name"] for item in RESOURCES])
    ):
        res = next((item for item in RESOURCES if item["name"] == resource), None)
        if not res:
            return await inter.response.send_message(f"The resource `{resource}` does not exist.",ephemeral=True)

        embed = disnake.Embed(
            color=disnake.Colour.orange(), 
            title=res["name"]
        ).add_field("About",res["about"],inline=False).add_field("Link",res["link"],inline=False)
            
        await inter.response.send_message(embed=embed)
        
        await dph.log("`/resource` Command", f"A user looked up the `{resource}` resource","orange",self)
