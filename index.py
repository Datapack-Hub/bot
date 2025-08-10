import discord
import variables

# intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Bot(
    intents=intents,
    activity=discord.Activity(
        name="out for your commands",
        type=discord.ActivityType.watching,
    ),
    default_command_integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install
    }
)

# Commands
from cogs.commands.link import LinkCommand
client.add_cog(LinkCommand(client))

from cogs.commands.template import TemplateCommand
client.add_cog(TemplateCommand(client))

from cogs.commands.info import InfoCommand
client.add_cog(InfoCommand(client))

from cogs.commands.folderstructure import FolderStructureCommand
client.add_cog(FolderStructureCommand(client))

from cogs.commands.vanilla import VanillaCommand
client.add_cog(VanillaCommand(client))

from cogs.commands.packformat import PackFormatCommand
client.add_cog(PackFormatCommand(client))

from cogs.commands.help import HelpCommand
client.add_cog(HelpCommand(client))

from cogs.commands.dpwiki import DPWikiCommand
client.add_cog(DPWikiCommand(client))

# Events
@client.event
async def on_ready():
    print("Bot is ready!")

from cogs.events.on_message import OnMessage
client.add_cog(OnMessage(client))

# Misc Cogs
from cogs.misc.admin import AdminCommands
client.add_cog(AdminCommands(client))

# Run the bot
client.run(variables.TOKEN)