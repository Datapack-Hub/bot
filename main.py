# * IMPORTING
# Local Files
import bot_token


# Cogs
# TODO import cogs.message_commands.fancify as fancify

# ? reconsider/rework this: import cogs.commands.eliminate as eliminate
import cogs.commands.folderstructure as folderstructure
import cogs.commands.help as help
import cogs.commands.info as info
import cogs.commands.invite as invite
import cogs.commands.method as method
import cogs.commands.packformat as packformat
import cogs.commands.ping as ping
import cogs.commands.resource as resource
import cogs.commands.syntax as syntax
import cogs.commands.template as template
import cogs.commands.highlighter as highlighter_command
import cogs.commands.vanilla as vanilla

import cogs.listeners.on_button_click as on_button_click
import cogs.listeners.on_guild_join as on_guild_join
import cogs.listeners.on_guild_remove as on_guild_remove
import cogs.listeners.on_message as on_message
import cogs.listeners.on_ready as on_ready
# Other Stuff
import disnake
from disnake.ext import commands

# * SETUP BOT
# Set Intents
intents = disnake.Intents.default()

intents.message_content = True

# Set Activity Status
activity = disnake.Activity(
    name="out for your commands",
    type=disnake.ActivityType.watching,
)

# Initialize
bot = commands.Bot(command_prefix="?", intents=intents, activity=activity)
   
    
# * ADD COGS

# Slash Commands
bot.add_cog(syntax.SyntaxCommand(bot))
bot.add_cog(method.MethodCommand(bot))
bot.add_cog(folderstructure.FolderStructureCommand(bot))
bot.add_cog(invite.InviteCommand(bot))
bot.add_cog(packformat.PackFormatCommand(bot))
bot.add_cog(info.InfoCommand(bot))
bot.add_cog(template.TemplateCommand(bot))
bot.add_cog(help.HelpCommand(bot))
bot.add_cog(ping.PingCommand(bot))
bot.add_cog(resource.ResourceCommand(bot))
bot.add_cog(highlighter_command.HighlighterCommand(bot))
bot.add_cog(vanilla.VanillaCommand(bot))


# Listeners
bot.add_cog(on_message.OnMessage(bot))
bot.add_cog(on_button_click.OnButtonClick(bot))
bot.add_cog(on_guild_join.OnGuildJoin(bot))
bot.add_cog(on_guild_remove.OnGuildRemove(bot))
bot.add_cog(on_ready.OnReady(bot))

# * RUN BOT
bot.run(bot_token.token)
