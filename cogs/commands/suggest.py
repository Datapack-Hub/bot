import disnake
from disnake.ext import commands
import variables


class suggest_command(commands.Cog, name="suggest"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="suggest", description="Suggest a new feature for the bot"
    )
    async def suggest(
        self, inter: disnake.ApplicationCommandInteraction, suggestion: str
    ):
        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title=":white_check_mark: Submitted Suggestion!",
            description=(
                'Sucessfully submitted your suggestion "'
                + suggestion
                + "\"\nIf you're lucky (or it was just really good), you might see it in one of the next bot updates!"
            ),
        )

        await inter.response.send_message(embed=embed)

        embed = disnake.Embed(
            color=disnake.Color.green(), title="New Suggestion!", description=suggestion
        )

        embed.set_footer(
            text=("Suggested by " + inter.user.name),
            icon_url=inter.user.display_avatar,
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
