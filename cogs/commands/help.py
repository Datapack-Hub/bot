import disnake
import variables
import dph
from disnake.ext import commands

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
        command: commands_enum = "all",
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
**/highlighter**: Allows you to toggle the `mcfunction` syntax highlighter
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
            case "newsletter":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/newsletter`**"),
                    description="Subscribes/unsubscribes you to/from our DM-Newsletter, which will notify you each time something relevant to datapacks happens (for example: new snapshot with datapack related changes, new website/tool release, etc.)",
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
                    description="Shows information about stuff outside of minecraft which might help you improve your datapacking experience\nSyntax: `/info info:<info>`\nAviable infos: `logs default`, `me`, `editor`, `logs other`, `update rp 1.19.3+` **MORE COMING SOON**",
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
                    description="Shows the datapack/resourcepack packformat for a specific version or multiple versions\nSyntax: `/packformat [resourcepacks|datapacks|<minecraft version>]` ",
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
                    description="Shows link and short explanation to a resource helpful on your datapacking journey\nSyntax: `/resource resource:<reource>`\nAviable resources: `misode`, `mcstacker`, `taglib`, `minecraft wiki`, `cloudwolf`, `crafting (thedestruc7i0n)`, `smithed`, `minecraft tools`, `minecraftjson`",
                )
            case "highlighter":
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**🚑 `/highlighter`**"),
                    description="Allows users with `manage_guild` permissions to toggle the `mcfunction` syntax highlighter using an interface\nSyntax: `/highlighter`",
                ) 


        await inter.response.send_message(embed=embed)
        
        await dph.log("`/help` Command", f"A user looked up help for `{command}`","orange",self)