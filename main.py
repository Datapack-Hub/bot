# * IMPORTING
# Libaries
import disnake
from disnake.ext import commands

# Local Files
import variables
import bot_token

# Cogs
#import cogs.message_commands.redirect_to_help_channel as redirect_to_help_channel
import cogs.commands.syntax as syntax
import cogs.commands.method as method
import cogs.commands.folderstructure as folderstructure
import cogs.commands.invite as invite
import cogs.commands.newsletter as newsletter
import cogs.commands.packformat as packformat
import cogs.commands.ping as ping
import cogs.commands.info as info
import cogs.commands.template as template
import cogs.commands.eliminate as eliminate
import cogs.commands.help as help
import cogs.listeners.on_message_event as on_message
import cogs.listeners.on_thread_create_event as on_thread_create
import cogs.listeners.on_button_click_event as on_button_click
import cogs.listeners.on_guild_join_event as on_guild_join
import cogs.listeners.on_guild_remove_event as on_guild_remove
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
bot = commands.Bot(
    command_prefix="?",
    intents=intents,
    activity=activity,
    test_guilds=variables.test_guilds
)


# * ADD COGS
# Message Commands
#bot.add_cog(redirect_to_help_channel.RedirectToHelpChannel(bot))

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

# Listeners
bot.add_cog(on_message.OnMessage(bot))
bot.add_cog(on_button_click.OnButtonClick(bot))
bot.add_cog(on_guild_join.OnGuildJoin(bot))
bot.add_cog(on_guild_remove.OnGuildRemove(bot))
bot.add_cog(on_ready.OnReady(bot))


# * RUN BOT
bot.run(bot_token.token)
