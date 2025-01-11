import disnake
import variables
from disnake.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.InteractionBot = bot
                         
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        # Guilds announce (to system channel, ie general)
        if message.content.startswith("dh!gannounce\n") and message.author.id in variables.ADMINS:
            msg = message.content.replace("dh!gannounce\n","")
            
            title = msg.splitlines()[0]
            desc = "\n".join(msg.split('\n')[1:])
            
            embed = disnake.Embed(
                title=title,
                description=desc,
                colour=disnake.Colour.orange()
            )
            
            embed.set_footer(text="This is an official message from Datapack Hub.")
            
            for server in self.bot.guilds:
                if server.system_channel:
                    try:
                        await server.system_channel.send(embed=embed)
                    except:
                        print("Failed to send the message to " + server.name)
                elif server.owner:
                    try:
                        embed.set_footer(text="You are receiving this message because you own a server which this bot is in.")
                        await server.owner.send(embed=embed)
                    except:
                        print("Failed to send the message to server owner " + server.owner.global_name)
        
        # Staff announce (to public updates channel of each guild, usually staff only)
        if message.content.startswith("dh!sannounce\n") and message.author.id in variables.ADMINS:
            msg = message.content.replace("dh!sannounce\n","")
            
            title = msg.splitlines()[0]
            desc = "\n".join(msg.split('\n')[1:])
            
            embed = disnake.Embed(
                title=title,
                description=desc,
                colour=disnake.Colour.orange()
            )
            
            embed.set_footer(text="This is an official message from Datapack Hub.")
            
            for server in self.bot.guilds:
                if server.public_updates_channel:
                    try:
                        await server.public_updates_channel.send(embed=embed)
                    except:
                        print("Failed to send the message to " + server.name)
                elif server.owner:
                    try:
                        embed.set_footer(text="You are receiving this message because you own a server which this bot is in.")
                        await server.owner.send(embed=embed)
                    except:
                        print("Failed to send the message to server owner " + server.owner.global_name)