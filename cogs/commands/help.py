import disnake
import dph
from disnake.ext import commands

COMMANDS = [
    {
        "command":"template",
        "short":"Shows a template for datapacks or resource packs",
        "long":"**About**\nSends a datapack/resource pack template.\nSyntax: `/template [type:datapack|resourcepack>]` (defaults to `datapack`)"
    },
    {
        "command":"invite",
        "short":"Shows invites to useful datapack related servers",
        "long":"**About**\nShows invites to useful datapack related servers\n\n**Syntax:**\n `/invite invite:<server>`\n\n**Available invites:**\n - `datapack hub`\n- `minecraft commands`\n- `shader labs`\n- `bot`\n- `smithed`\n- `blockbench`\n- `optifine`\n- `fabric`\n- `minecraft`\n- `dataworld (fr)`\n- `animated java`\n- `datapack jam`"
    },
    {
        "command":"packformat",
        "short":"Shows the `pack_format` for a specific version",
        "long":"**About**\nShows the `pack_format` (for use in `pack.mcmeta`) for a specific version(s)\n\n**Syntax:**\n `/packformat [version:latest|snapshots|releases|<minecraft version>]` "
    },
    {
        "command":"folderstructure",
        "short":"Shows the folder structure for datapacks/resource packs",
        "long":"**About**\nShows the folder structure for datapacks/resource packs as a folder tree.\n\n**Syntax:**\n `/folderstructure [type:datapack|resourcepack]` (defaults to `datapack`)"
    },
    {
        "command":"syntax",
        "short":"Shows the syntax of any Minecraft command",
        "long":"**About**\nShows the syntax of any Minecraft command\n\n**Syntax:**\n `/syntax command:<command>`"
    },
    {
        "command":"info",
        "short":"Shows a quick guide about certain tips/tools you can use",
        "long":"**About**\nShows a quick guide about certain tips/tools you can use\n\n**Syntax:**\n `/info info:<name>`\n\n**Available Guides**: \n- `logs default`\n- `me`\n- `editor`\n- `logs other`\n- `update rp 1.19.3+`\n- `update dp 1.21+`"
    },
    {
        "command":"method",
        "short":"Shows a full-size guide for certain common datapack concepts",
        "long":"**About**\nShows a full-size guide for certain common datapack concepts\n\n**Syntax:**\n `/method method:<name>`\n\n**Available Guides**:\n- `random number`\n- `raycast`\n- `slowcast`\n- `rightclick detection`\n- `rightclick detection coas`\n- `rightclick detection EoE`\n- `rightclick detection`\n- `rightclick detection interaction`\n- `rightclick detection food`\n- `custom gui`\n- `custom item crafting recipe`\n- `array iteration`\n- `player id system`"
    },
    {
        "command":"resource",
        "short":"Links to external datapack resources",
        "long":"**About**\nLinks to external datapack resources\n\n**Syntax:**\n `/resource resource:<name>`\n\n**Available Resources**:\n- `misode`\n- `mcstacker`\n- `taglib`\n- `minecraft wiki`\n- `cloudwolf`\n- `crafting`\n- `smithed`\n- `minecraft tools`\n- `minecraftjson`"
    },
    {
        "command":"highlighter",
        "short":"Information about the automatic syntax highlighter for mcfunction",
        "long":"**About**\nInformation about the automatic syntax highlighter for mcfunction\n\n**Syntax:**\n `/highlighter`"
    },
    {
        "command":"ping",
        "short":"Returns the ping of the bot",
        "long":"**About**\nReturns the ping of the bot\n\n**Syntax:**\n `/ping`"
    }
]


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
        command: str = commands.Param("*",choices=[item["command"] for item in COMMANDS]),
    ):
        if command == "*":
            content = "Datapack Helper is a bot run by the team at **Datapack Hub** to help you with your datapacking experience. With this bot, teaching people how to create datapacks (as well as making them yourself) is much quicker and easier.\n\n**Commands**:\n"
            for cmd in COMMANDS:
                content += f"- `/{cmd['command']}`: {cmd['short']}\n"
            content += "\nYou can use `/help <command>` to find out more about a command."
            
            embed = disnake.Embed(
                color=disnake.Colour.orange(), 
                title="Datapack Helper", 
                description=content,
            )
                
            await inter.response.send_message(embed=embed)
        else:
            cmd = next((item for item in COMMANDS if item["command"] == command), None)
            if not cmd:
                return await inter.response.send_message(f"The command `{command}` does not exist.",ephemeral=True)

            embed = disnake.Embed(
                color=disnake.Colour.orange(), 
                title=f"About the command`/{command}`", 
                description=cmd["long"],
            )
                
            await inter.response.send_message(embed=embed)

        await dph.log("`/help` Command", f"A user looked up help for `{command}`","orange",self)