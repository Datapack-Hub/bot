import disnake
import dph
from disnake.ext import commands

CommandsEnum = commands.option_enum(
    [
        "invite",
        "help",
        "syntax",
        "template",
        "info",
        "method",
        "folderstructure",
        "packformat",
        "resource",
        "highlighter",
        "ping"
    ]
)


class HelpCommand(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="Help",
        description="Gives you information about any command this bot adds",
    )
    async def help(
        self,
        inter: disnake.ApplicationCommandInteraction,
        command: CommandsEnum = "all",
    ):
        match command:
            case "all":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 Help**"),
                    description="""
Here's a list of all the commands this bot adds, use `/help command:<command>` to learn more about a specific command!
**/template**: Sends a datapack/resourcepack template
**/invite**: Shows invites to datapacking-relevant discord servers
**/packformat**: Shows the datapack/resourcepack packformat for a specific version or multiple versions
**/folderstructure**: Shows folder structure for datapacks/resourcepacks
**/syntax**: Shows the syntax of any minecraft command
**/info:**: Shows information about stuff outside of minecraft, which might improve your datapacking experience
**/method**: Shows how to do certain stuff using datapacks/commands
**/resource**: Gives you the link to any resource useful for datapacking
**/highlighter**: Informs you about the bot's `mcfunction` syntax highlighter function. _([Source Code by bth123](https://github.com/bth123/mcf-ansi-highlighter))_
**/ping**: Returns current bot latency""",
                )
            case "ping":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/ping`**"),
                    description="Returns bot ping.",
                )
            case "invite":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/invite`**"),
                    description="Shows invites for discord servers relevant for datapacks in one way or another\nSyntax: `/invite invite:<server>`\nAviable invites: `datapack hub`,`minecraft commands`,`shader labs`,`bot`,`smithed`,`blockbench`,`optifine`,`fabric`,`minecraft`,`dataworld (fr)`, `animated java`,`datapack jam`",
                )
            case "help":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/help`**"),
                    description="Shows either a list of all bot commands or information about a specific bot command\nSyntax `/help command:<command>`\nAviable commands: `invite`,`help`,`eliminate`,`resolve`,`newsletter`,`syntax`,`template`,`info`,`folderstructure`,`packformat`,highlighter,`ping`",
                )
            case "syntax":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/syntax`**"),
                    description="Shows the syntax of any minecraft command\nSyntax: `/syntax command:<command>`",
                )
            case "template":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/template`**"),
                    description="Sends a datapack/resourcepack template to the current channel\nSyntax: `/template type[datapack|resourcepack]` (defaults to `datapack`)",
                )
            case "info":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/info`**"),
                    description="Shows information about stuff outside of minecraft which might help you improve your datapacking experience\nSyntax: `/info info:<info>`\nAviable infos: `logs default`, `me`, `editor`, `logs other`, `update rp 1.19.3+`, `update dp 1.21+` **MORE COMING SOON**",
                )
            case "method":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/method`**"),
                    description="Shows how to do certain stuff using datapacks/commands\nSyntax: `/method method:<method>`\nAviable methods: `random number`, `raycast`, `slowcast`, `rightclick detection`, `rightclick detection coas`, `rightclick detection EoE`, `rightclick detection`, `rightclick detection interaction`,`rightclick detection food`,`custom gui`,`custom item crafting recipe`,`array iteration`, `player id system` **MORE COMING SOON**",
                )
            case "packformat":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/packformat`**"),
                    description="Shows the datapack/resourcepack packformat for a specific version or multiple versions\nSyntax: `/packformat [latest|snapshots|releases|<minecraft version>]` ",
                )
            case "folderstructure":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/folderstructure`**"),
                    description="Shows the folderstructure of datapacks/resourcepacks\nSyntax: `/folderstructure type:[datapack|resourcepack]` (defaults to datapack)",
                )
            case "resource":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/resource`**"),
                    description="Shows link and short explanation to a resource helpful on your datapacking journey\nSyntax: `/resource resource:<reource>`\nAviable resources: `misode`, `mcstacker`, `taglib`, `minecraft wiki`, `cloudwolf`, `crafting (thedestruc7i0n)`, `smithed`, `minecraft tools`, `minecraftjson`\n_([Source Code by bth123](https://github.com/bth123/mcf-ansi-highlighter))_",
                )
            case "highlighter":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/highlighter`**"),
                    description="Informs you about the bot's `mcfunction` syntax highlighter function. \nSyntax: `/highlighter`",
                ) 
            case _:
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**⚠️ `Invalid command`**"),
                    description="Please use `/help` to see a list of all commands",
                ),

        await inter.response.send_message(embed=embed)
        
        await dph.log("`/help` Command", f"A user looked up help for `{command}`","orange",self)