import disnake
from disnake.ext import commands
import variables


class OnGuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.green(),
            title=("**Joined New Guild**"),
            description=(
                "Bot was added to the **"
                + str(guild.name)
                + "** (**"
                + str(guild.id)
                + "**) server"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
