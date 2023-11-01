import disnake
import variables
from disnake.ext import commands


class OnGuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = disnake.Embed(
            color=disnake.Colour.green(),
            title=("**Joined New Guild**"),
            description=(
                "Bot was added to the **"
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
