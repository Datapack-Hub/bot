import disnake
from disnake.ext import commands
import variables

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
    ]
)


class invite_command(commands.Cog, name="invite"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="invite",
        description="Shows discord invite for a discord server relevant to datapacks",
    )
    async def invite(
        self, inter: disnake.ApplicationCommandInteraction, invite: invites
    ):
        if invite == "datapack hub":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Datapack Hub Invite**"),
                description="Join Datapack Hub for help with your Datapacks and support regarding this bot using this link: https://dsc.gg/datapack",
            )

        elif invite == "minecraft commands":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Minecraft Commands Invite**"),
                description="Join Minecraft Commands for help regarding your Datapacks using this link: https://discord.gg/QAFXFtZ",
            )

        elif invite == "shader labs":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**ShaderLABS Invite**"),
                description="Join ShaderLABS for help regarding shaders using this link: https://discord.gg/Ayav9YPQra",
            )
        elif invite == "bot":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Datapack Helper Invite**"),
                description="Add the Datapack Helper bot to your server using this link: *COMING SOON*",
            )
        elif invite == "smithed":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Smithed Invite**"),
                description="Join Smithed for information/help regarding the smithed datapacking conventions using this link: https://smithed.dev/discord",
            )
        elif invite == "blockbench":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Blockbench Invite**"),
                description="Join Blockbench for help regarding modeling and Blockbench using this link: https://discord.gg/blockbench",
            )
        elif invite == "optifine":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Optifine Invite**"),
                description="Join Optifine for help regarding (problems with) Optifine using this link: https://discord.gg/optifine",
            )
        elif invite == "fabric":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Fabric Invite**"),
                description="Join The Fabric Project for information/help regarding Fabric using this link: https://discord.gg/DtevV9NmaR",
            )

        await inter.response.send_message(embed=embed)
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/invite` Command**"),
            description=(
                str(inter.user.name) + " looked up the invite of `" + str(invite) + "`"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
