import disnake
import variables
import dph
from disnake.ext import commands


class OnGuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open(file=f"{variables.full_path}/highlighter_servers.txt", mode="r") as file:
            lines = file.readlines()
            
        with open(f"{variables.full_path}/highlighter_servers.txt", "w") as file:
            for line in lines:
                if not str(inter.guild.id) in line:
                    file.write(line)
        await dph.log("**Removed From guild**","Bot was removed from a server","red",self)