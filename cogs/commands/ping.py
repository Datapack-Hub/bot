import disnake
from disnake.ext import commands

infos = commands.option_enum(
    ["logs default", "me", "editor", "logs other", "update rp 1.19.3+"]
)


class PingCommand(commands.Cog, name="ping"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="info",
        description="Returns bot ping",
    )
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        ping = round((self.bot.latency * 1000), 2)
        await inter.response.send_message(
            "🏓 Current Bot Ping: " + str(ping) + "ms", ephemeral=True
        )
