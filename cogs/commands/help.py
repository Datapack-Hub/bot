import disnake
from disnake.ext import commands
import variables

commands_enum = commands.option_enum(
    [
        "invite",
        "help",
        "eliminate",
        "resolve",
        "newsletter",
        "syntax",
        "template",
        "info",
        "folderstructure",
        "packformat"
    ]
)


class HelpCommand(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="Help",
        description="Gives you information about any command this bot adds"
    )
    
    async def help(
        self, inter: disnake.ApplicationCommandInteraction, command: commands_enum = "all"
    ):
        if command == "all":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 Help**"),
                description="Here's a list of all the commands this bot adds, use `/help command:<command>` to learn more about a specific command!\n\n</template:1150431763324207226>: Sends a datapack/resourcepack template\n</folderstructure resourcepack:1144257590105227299>",
            )
        elif command == "invite":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Datapack Hub command**"),
                description="invite",
            )
        elif command == "help":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Datapack Hub command**"),
                description="help",
            )
        elif command == "eliminate":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Datapack Hub command**"),
                description="eliminate",
            )


        await inter.response.send_message(embed=embed)
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/help` Command**"),
            description=(
                str(inter.user.name) + " looked up `" + str(command) + "`"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
