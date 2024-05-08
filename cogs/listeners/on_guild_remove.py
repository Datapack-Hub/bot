import disnake
import variables
import dph
from disnake.ext import commands


class OnGuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open(file=f"{variables.full_path}/highlighter_servers.txt", mode="w+") as file:
               for line in file:
                   line.replace(f"{guild.id}","")
        await dph.log("**Removed From guild**","Bot was removed from the **"+ str(guild.name)+ "** server (owned by **"+ str(guild.owner.name)+ "**, "+ str(guild.member_count)+ " members)","red",self)