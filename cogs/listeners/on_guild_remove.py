import disnake
import variables
import dph
from disnake.ext import commands


class OnGuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await dph.log("**Removed From guild**","Bot was removed from the **"+ str(guild.name)+ "** server (owned by **"+ str(guild.owner.name)+ "**, "+ str(guild.member_count)+ " members)","red",self)