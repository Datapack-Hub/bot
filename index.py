import discord

import variables
from cogs.commands.dpwiki import DPWikiCommand
from cogs.commands.folderstructure import FolderStructureCommand
from cogs.commands.help import HelpCommand
from cogs.commands.info import InfoCommand
from cogs.commands.link import LinkCommand
from cogs.commands.packformat import PackFormatCommand
from cogs.commands.template import TemplateCommand
from cogs.commands.vanilla import VanillaCommand
from cogs.events.on_message import OnMessage
from cogs.misc.admin import AdminCommands
from utils.log import setup_logger

# Logger setup
logger = setup_logger(__name__)

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
        discord.IntegrationType.user_install,
    },
)
logger.info("Setting up bot...")


# Commands

logger.info("Adding command cogs...")

client.add_cog(LinkCommand(client))
client.add_cog(TemplateCommand(client))
client.add_cog(InfoCommand(client))
client.add_cog(FolderStructureCommand(client))
client.add_cog(VanillaCommand(client))
client.add_cog(PackFormatCommand(client))
client.add_cog(HelpCommand(client))
client.add_cog(DPWikiCommand(client))

logger.info("Command cogs added.")

# Events
@client.event
async def on_ready():
    logger.info("Bot is ready!")


logger.info("Adding event cogs...")
client.add_cog(OnMessage(client))

# Misc Cogs
client.add_cog(AdminCommands(client))
logger.info("Event cogs added.")

logger.info("Bot setup complete.")
logger.info("Logging in...")
# Run the bot
client.run(variables.TOKEN)
