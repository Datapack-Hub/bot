import disnake
from disnake.ext import commands
import variables


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # slow_count.start()
        embed = disnake.Embed(color=disnake.Colour.green(), title="**Bot started**")
        print(f"Logged in as {self.bot.user}")
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
