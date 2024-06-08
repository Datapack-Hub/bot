import variables
import dph
from disnake.ext import commands


class OnGuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open(file=f"{variables.full_path}/highlighter_servers.txt", mode="a") as file:
            file.write(f"\n{guild.id}")
        await dph.log("**Added To Guild**", "Bot was added to a new server", "green",self)
