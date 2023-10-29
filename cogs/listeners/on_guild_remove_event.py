import disnake
import variables
from disnake.ext import commands


class OnGuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.red(),
            title=("**Left Guild**"),
            description=(
                "Bot was removed from the **"
                + str(guild.name)
                + "** server (owned by **"
                + str(guild.owner.name)
                + "**, "
                + str(guild.member_count)
                + " members)"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
