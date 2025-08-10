import discord
import variables
from components.views import AdminMessageView

class AdminCommands(discord.Cog):
    def __init__(self, bot):
        self.bot: discord.Bot = bot
                         
    @discord.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Guilds announce (to system channel, ie general)
        if message.content.startswith("dh!gannounce\n") and message.author.id in variables.ADMINS:
            msg = message.content.replace("dh!gannounce\n","")
            
            title = msg.splitlines()[0]
            desc = "\n".join(msg.split('\n')[1:])
            
            msgview = AdminMessageView(title, desc)
            
            for server in self.bot.guilds:
                if server.system_channel:
                    try:
                        await server.system_channel.send(view=msgview)
                    except:
                        print("Failed to send the message to " + server.name)
        
        # Staff announce (to public updates channel of each guild, usually staff only)
        if message.content.startswith("dh!sannounce\n") and message.author.id in variables.ADMINS:
            msg = message.content.replace("dh!sannounce\n","")
            
            title = msg.splitlines()[0]
            desc = "\n".join(msg.split('\n')[1:])
            
            msgview = AdminMessageView(title, desc)
            
            for server in self.bot.guilds:
                if server.public_updates_channel:
                    try:
                        await server.public_updates_channel.send(view=msgview)
                    except:
                        print("Failed to send the message to " + server.name)