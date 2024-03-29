# * IMPORTING

# Local Files
import bot_token
import disnake
from disnake.ext import commands

# Cogs
import cogs.message_commands.fancify as fancify

import cogs.commands.eliminate as eliminate
import cogs.commands.folderstructure as folderstructure
import cogs.commands.help as help
import cogs.commands.info as info
import cogs.commands.invite as invite
import cogs.commands.method as method
import cogs.commands.newsletter as newsletter
import cogs.commands.packformat as packformat
import cogs.commands.ping as ping
import cogs.commands.resource as resource
import cogs.commands.syntax as syntax
import cogs.commands.template as template

import cogs.listeners.on_button_click_event as on_button_click
import cogs.listeners.on_guild_join_event as on_guild_join
import cogs.listeners.on_guild_remove_event as on_guild_remove
import cogs.listeners.on_message_event as on_message
import cogs.listeners.on_ready_event as on_ready

# * SETUP BOT
# Set Intents
intents = disnake.Intents.all()

# Set Activity Status
activity = disnake.Activity(
    name="out for your commands",
    type=disnake.ActivityType.watching,
)

# Initialize
bot = commands.Bot(command_prefix="?", intents=intents, activity=activity)


# * ADD COGS
# Message Commands
bot.add_cog(fancify.FancifyCommand(bot))

# Slash Commands
bot.add_cog(syntax.SyntaxCommand(bot))
bot.add_cog(method.MethodCommand(bot))
bot.add_cog(folderstructure.FolderStructureCommand(bot))
bot.add_cog(invite.InviteCommand(bot))
bot.add_cog(newsletter.NewsletterCommand(bot))
bot.add_cog(packformat.PackFormatCommand(bot))
bot.add_cog(info.InfoCommand(bot))
bot.add_cog(template.TemplateCommand(bot))
bot.add_cog(eliminate.EliminateCommand(bot))
bot.add_cog(help.HelpCommand(bot))
bot.add_cog(ping.PingCommand(bot))
bot.add_cog(resource.ResourceCommand(bot))


# Listeners
bot.add_cog(on_message.OnMessage(bot))
bot.add_cog(on_button_click.OnButtonClick(bot))
bot.add_cog(on_guild_join.OnGuildJoin(bot))
bot.add_cog(on_guild_remove.OnGuildRemove(bot))
bot.add_cog(on_ready.OnReady(bot))


# * RUN BOT
bot.run(bot_token.token)
