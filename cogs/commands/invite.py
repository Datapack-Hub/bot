import disnake
import dph
from disnake.ext import commands

invites = commands.option_enum(
    [
        "datapack hub",
        "minecraft commands",
        "shader labs",
        "bot",
        "smithed",
        "blockbench",
        "optifine",
        "fabric",
        "minecraft",
        "dataworld (fr)",
        "animated java",
        "datapack jam"
    ]
)


class InviteCommand(commands.Cog, name="invite"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="invite",
        description="Shows discord invite for a discord server relevant to datapacks",
    )
    async def invite(
        self, inter: disnake.ApplicationCommandInteraction, invite: invites
    ):
        match invite:
            case "datapack hub":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪 Datapack Hub Invite**"),
                    description="Join Datapack Hub for help with your Datapacks and support regarding this bot using this link: https://dsc.gg/datapack",
                )

            case "minecraft commands":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Minecraft Commands Invite**"),
                    description="Join Minecraft Commands for help regarding your Datapacks using this link: https://discord.gg/QAFXFtZ",
                )

            case "shader labs":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪ShaderLABS Invite**"),
                    description="Join ShaderLABS for help regarding shaders using this link: https://discord.gg/Ayav9YPQra",
                )
            case "bot":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Datapack Helper Invite**"),
                    description="Add the Datapack Helper bot to your server using this link: https://bot.datapackhub.net",
                )
            case "smithed":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Smithed Invite**"),
                    description="Join Smithed for information/help regarding the smithed datapacking conventions using this link: https://smithed.dev/discord",
                )
            case "blockbench":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Blockbench Invite**"),
                    description="Join Blockbench for help regarding modeling and Blockbench using this link: https://discord.gg/blockbench",
                )
            case "optifine":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Optifine Invite**"),
                    description="Join Optifine for help regarding (problems with) Optifine using this link: https://discord.gg/optifine",
                )
            case "fabric":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Fabric Invite**"),
                    description="Join The Fabric Project for information/help regarding Fabric using this link: https://discord.gg/DtevV9NmaR",
                )
            case "minecraft":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Minecraft Invite**"),
                    description="Join the official minecraft discord server using this link: https://discord.gg/minecraft",
                )
            case "dataworld (fr)":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪DataWorld Invite**"),
                    description="Join DataWorld, a french-only discord server, to get help with datapacks using the link: https://discord.gg/5y5FBz5 \nRejoins Data World pour obtenir de l'aide sur les datapacks avec le lien: https://discord.gg/5y5FBz5",
                )
            case "animated java":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**Animated Java Invite**"),
                    description="Join the Animated Java discord server for help with the Animated Java Blockbench plugin using this link: https://animated-java.dev/discord",
                )
            case "datapack jam":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**Datapack Jam Invite**"),
                    description="Join the Datapack Jam discord server to test your skill in fun jams: https://dsc.gg/datapackjam",
                )
            case _:
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚪Datapack Helper Invite**"),
                )

        await inter.response.send_message(embed=embed)
        
        await dph.log("`/invite` Command", f"A user looked up the `{invite}` invite","orange",self)