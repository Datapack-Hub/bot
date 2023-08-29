# invite link, don't share for now: https://discord.com/oauth2/authorize?client_id=1108074519308017734&scope=bot&permissions=517611048000
#* IMPORTING
# Libaries
import disnake
from disnake.ext import commands
from disnake.ext import tasks

# Local Files
import variables
import bot_token 

# Cogs
import cogs.message_commands.redirect_to_help_channel as redirect_to_help_channel
import cogs.commands.syntax as syntax
import cogs.commands.method as method
import cogs.commands.resolve as resolve
import cogs.commands.folderstructure as folderstructure
import cogs.commands.invite as invite
import cogs.commands.newsletter as newsletter
import cogs.commands.packformat as packformat
import cogs.commands.info as info
import cogs.listeners.on_message_event as on_message
import cogs.listeners.on_thread_create_event as on_thread_create
import cogs.listeners.on_button_click_event as on_button_click
import cogs.listeners.on_guild_join_event as on_guild_join
import cogs.listeners.on_guild_remove_event as on_guild_remove
import cogs.listeners.on_ready_event as on_ready

#* SETUP BOT
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
    test_guilds=variables.test_guilds,
)


#* ADD COGS
# Message Commands
bot.add_cog(redirect_to_help_channel.redirect_to_help_channel(bot))

# Slash Commands
bot.add_cog(syntax.syntax_command(bot))
bot.add_cog(method.method_command(bot))
bot.add_cog(resolve.resolve_command(bot))
bot.add_cog(folderstructure.folderstructure_command(bot))
bot.add_cog(invite.invite_command(bot))
bot.add_cog(newsletter.newsletter_command(bot))
bot.add_cog(packformat.packformat_command(bot))
bot.add_cog(info.info_command(bot))

# Listeners
bot.add_cog(on_message.on_message(bot))
bot.add_cog(on_button_click.on_button_click(bot))
bot.add_cog(on_thread_create.on_thread_create(bot))
bot.add_cog(on_guild_join.on_guild_join(bot))
bot.add_cog(on_guild_remove.on_guild_remove(bot))
bot.add_cog(on_ready.on_ready(bot))


#* RUN BOT
bot.run(bot_token.token)
