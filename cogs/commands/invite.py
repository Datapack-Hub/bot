import disnake
import dph
from disnake.ext import commands

INVITES = [
    {
        "name": "Datapack Hub",
        "about": "Datapack Hub is the #1 place to get help with and discuss datapacks. This bot was made by Datapack Hub, so you can join to get support with this bot and your datapacks!",
        "link": "https://discord.datapackhub.net/"
    },
    {
        "name": "ShaderLABS",
        "about": "ShaderLABS is a server for all kinds of Minecraft shaders, including vanilla (resource pack) shaders.",
        "link": "https://discord.gg/Ayav9YPQra"
    },
    {
        "name": "[BOT] Datapack Helper",
        "about": "Use this invite to add the Datapack Helper bot (that's me!) to your server.",
        "link": "https://bot.datapackhub.net"
    },
    {
        "name": "Smithed",
        "about": "Smithed is a community project aiming to provide a platform to share datapacks and remove all compatibility issues with datapacks. Following Smithed's conventions on compatibility make it easier for datapacks to work together",
        "link": "https://smithed.dev/discord"
    },
    {
        "name": "Blockbench",
        "about": "The Blockbench Discord is a server for support using the Blockbench app, as well as for 3D models, animation, and more.",
        "link": "https://discord.gg/blockbench"
    },
    {
        "name": "OptiFine",
        "about": "The OptiFine discord is the best place if you need help creating resource packs with OptiFine (or just generally need support with OptiFine)",
        "link": "https://discord.gg/optifine"
    },
    {
        "name": "Fabric Project",
        "about": "The Fabric Mod Loader has a support server, where you can get help with Fabric mods as well as making your own.",
        "link": "https://discord.gg/DtevV9NmaR"
    },
    {
        "name": "Minecraft",
        "about": "Join the official Minecraft Discord server, ran by Mojang Studios",
        "link": "https://discord.gg/minecraft"
    },
    {
        "name": "Animated Java",
        "about": "Join the Animated Java Discord server for help with the Animated Java Blockbench plugin",
        "link": "https://animated-java.dev/discord"
    },
    {
        "name": "Datapack Jam",
        "about": "Datapack Jam hosts mini week-long datapack competitions where you can compete with other datapackers to show your skills in a contest!",
        "link": "https://dsc.gg/datapackjam"
    },
    {
        "name": "[FR] Dataworld",
        "about": "Join DataWorld, a French-only Discord server, to get help with datapacks.",
        "link": "https://discord.gg/5y5FBz5"
    }
]


class InviteCommand(commands.Cog, name="invite"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="invite",
        description="Shows discord invite for a discord server relevant to datapacks",
    )
    async def invite(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        invite: str = commands.Param(choices=[item["name"] for item in INVITES])
    ):
        res = next((item for item in INVITES if item["name"] == invite), None)
        if not res:
            return await inter.response.send_message(f"The invite `{invite}` does not exist.",ephemeral=True)

        embed = disnake.Embed(
            color=disnake.Colour.orange(), 
            title=res["name"]
        ).add_field("About",res["about"],inline=False).add_field("Link",res["link"],inline=False)
            
        await inter.response.send_message(embed=embed)

        await inter.response.send_message(embed=embed)
        
        await dph.log("`/invite` Command", f"A user looked up the `{invite}` invite","orange",self)