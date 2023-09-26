import disnake
from disnake.ext import commands
import variables

commands_enum = commands.option_enum(
    [
        "invite",
        "help",
        "eliminate",
        "newsletter",
        "syntax",
        "template",
        "info",
        "method",
        "folderstructure",
        "packformat",
        "ping"
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
                description="Here's a list of all the commands this bot adds, use `/help command:<command>` to learn more about a specific command!\n\n</template:1153330774825766951>: Sends a datapack/resourcepack template\n</invite:1153330774825766947>: Shows invites to datapacking-relevant discord servers\n</packformat:1153330774825766949>: Shows `packformat` history for datapacks/resourcepacks\n</folderstructure:1153330774825766946>: Shows folder structure for datapacks/resourcepacks\n</syntax:1153330774825766943>: Shows the syntax of any minecraft command\n</info:1153330774825766950>: Shows information about stuff outside of minecraft, which might improve your datapacking experience\n</method:1153330774825766944>: Shows how to do certain stuff using datapacks/commands\n</ping:1155920839905128478> Returns current bot latency",
            )
        elif command == "ping":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/ping`**"),
                description="Returns bot ping."
            )
        elif command == "invite":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/invite`**"),
                description="Shows invites for discord servers relevant for datapacks in one way or another\nSyntax: `/invite invite:<server>`\nAviable invites: `datapack hub`,`minecraft commands`,`shader labs`,`bot`,`smithed`,`blockbench`,`optifine`,`fabric`,`minecraft`"
            )
        elif command == "help":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/help`**"),
                description="Shows either a list of all bot commands or information about a specific bot command\nSyntax `/help command:<command>`\nAviable commands: `invite`,`help`,`eliminate`,`resolve`,`newsletter`,`syntax`,`template`,`info`,`folderstructure`,`packformat`,`ping`"
            )
        elif command == "eliminate":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/eliminate`**"),
                description="Welcome to round one. `/eliminate` others before they can `/elimnate` you. Don't try to `/eliminate` the `/eliminate`d. You didn't see this.\nSyntax: `/eliminate target:<@user>`",
            )
        elif command == "newsletter":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/newsletter`**"),
                description="Subscribes/unsubscribes you to/from our DM-Newsletter, which will notify you each time something relevant to datapacks happens (for example: new snapshot with datapack related changes, new website/tool release, etc.)",
            )
        elif command == "syntax":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/syntax`**"),
                description="Shows the syntax of any minecraft command. *Slightly* bugged at the moment, fix coming asap\nSyntax: `/syntax command:<command>`",
            )
        elif command == "template":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/template`**"),
                description="Sends a datapack/resourcepack template to the current channel\nSyntax: `/template type[datapack|resourcepack]` (defaults to `datapack`)",
            )
        elif command == "info":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/info`**"),
                description="Shows information about stuff outside of minecraft which might help you improve your datapacking experience\nSyntax: `/info info:<info>`\nAviable infos: `logs default`, `me`, `editor`, `logs other`, `update rp 1.19.3+` **MORE COMING SOON**",
            )
        elif command == "method":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/method`**"),
                description="Shows how to do certain stuff using datapacks/commands\nSyntax: `/method method:<method>`\nAviable methods: `random number`, `raycast`, `slowcast`, `rightclick detection`, `rightclick detection coas`, `rightclick detection EoE`, `rightclick detection`, `rightclick detection interaction` **MORE COMING SOON**",
            )
        elif command == "packformat":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/packformat`**"),
                description="Shows the history of datapack/resourcepack packformats\nSyntax: `/packformat type:[datapack|resourcepack]` (defaults to datapack)"
            )
        elif command == "folderstructure":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**🚑 `/folderstructure`**"),
                description="Shows the folderstructure of datapacks/resourcepacks\nSyntax: `/folderstructure type:[datapack|resourcepack]` (defaults to datapack)"
            )

        await inter.response.send_message(embed=embed)
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/help` Command**"),
            description=(
                str(inter.user.name) + " looked up `" + str(command) + "` (Server: **" + inter.guild.name + "**)"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
