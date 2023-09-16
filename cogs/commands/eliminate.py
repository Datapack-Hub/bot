import disnake
from disnake.ext import commands
import variables


class eliminate_command(commands.Cog, name="eliminate"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="info",
        description="Gives you more information about an external feature to improve your datapacking experience",
    )
    async def info(
        self, inter: disnake.ApplicationCommandInteraction, target: disnake.User
    ):
        user = target.id
        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title="Elimination Successful 🧪",
            description=(
                "<@"
                + str(user)
                + "> has successfully been eliminated. Thank you for taking action and being loyal to your Datapack Hub staff team"
            ),
        )
        await inter.response.send_message(embed=embed)

        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/eliminate` Command**"),
            description=(str(inter.user.name) + " eliminated `" + target.name + "`!"),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
