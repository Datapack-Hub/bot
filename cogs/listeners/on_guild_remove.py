import variables
import dph
from disnake.ext import commands
from disnake import Guild
from aiofiles import open


class OnGuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: Guild):
        async with open(file=f"{variables.full_path}/highlighter_servers.txt") as file:
            lines = await file.readlines()
            
        async with open(f"{variables.full_path}/highlighter_servers.txt", "w") as file:
            for line in lines:
                if str(guild.id) not in line:
                    await file.write(line)
        await dph.log("**Removed From guild**","Bot was removed from a server","red",self)