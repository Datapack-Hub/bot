HELP = """
Datapack Helper is a utility bot run by **Datapack Hub** to help you with creating datapacks. With this bot, teaching people how to create datapacks (as well as making them yourself) is much quicker and easier.
### Commands
- `/dpwiki`: Access any wiki page or guide from the Datapack Wiki
- `/folderstructure`: View the folder structure of a Minecraft datapack.
- `/packformat`: View the pack format history for Minecraft data and resource packs.
- `/info`: Quick access to FAQs including code editors, Minecraft logs, etc.
- `/link`: View a list of useful links for creating datapacks, including discord servers, tools, and more.
- `/template`: Get an empty datapack template for a specific version
- `/vanilla`: View and open any vanilla Minecraft data file from the latest version.
### Syntax Highlighter (server install only)
Datapack Helper also provides **mcfunction syntax highlighting**. Simply send a code block with the `mcfunction` language specified, and it will be automatically coloured with [bth123's highlighter](<https://github.com/bth123/mcf-ansi-highlighter>).
"""

import discord
from components.views import HelpView

class HelpCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="help",
        description="Show a list of all this bot's features.",
    )
    async def help(
        self, 
        inter: discord.ApplicationContext
    ):
        await inter.respond(view=HelpView(HELP))