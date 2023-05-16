import disnake
from disnake.ext import commands
from bot_token import token

intents = disnake.Intents.all()

logs_channel = 1108080080711852042

bot = commands.Bot(
    command_prefix="?", intents=intents, test_guilds=[935560260725379143]
)

# MESSAGE COMMANDS


@bot.message_command(name="Send goofy ahh message")
async def claim(inter: disnake.MessageCommandInteraction):
    await inter.response.send_message(
        "Notified <@" + str(inter.target.author.id) + ">!", ephemeral=True
    )
    await inter.target.reply(content="imagine if this just works!")


# ON STARTUP
@bot.event
async def on_ready():
    emb = disnake.Embed(color=disnake.Colour.green(), title=("**Bot started**"))
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(logs_channel)
    await channel.send(embed=emb)


bot.run(token)
