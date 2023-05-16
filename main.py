import disnake
from disnake.ext import commands
from bot_token import token

intents = disnake.Intents.all()

bot = commands.Bot(
    command_prefix="?", 
    intents=intents, 
    test_guilds=[935560260725379143]
)

logs_channel = 1108080080711852042

# MESSAGE COMMANDS

@bot.message_command(name="Redirect to Help Channel")
async def claim(inter: disnake.MessageCommandInteraction):
    redi_ban_role = bot.get_guild(935560260725379143).get_role(1108093399053111387)
    if not redi_ban_role in inter.author.roles:
        await inter.response.send_message(
            "Notified <@" + str(inter.target.author.id) + ">! Abusing this command will result in punishment.", ephemeral=True
        )
        await inter.target.reply(content="imagine if this just works!")

        # Logging

        embed = disnake.Embed(color=disnake.Colour.orange(), 
                            title=("**Redirect to Help Channel**"),
                            description=("<@" + str(inter.user.id) + "> redirected a message by <@" + str(inter.target.author.id) +">! \nMessage Link: <#" + str(inter.channel.id) + ">")
                            )
        channel = bot.get_channel(logs_channel)
        await channel.send(embed=embed)
    else:
        await inter.response.send_message(
            "You are blacklisted from doing this. If you believe this is a miskate please contact a staff member.", ephemeral=True
        )

        # Logging
        embed = disnake.Embed(color=disnake.Colour.orange(), 
                            title=("**Redirect to Help Channel**"),
                            description=("<@" + str(inter.user.id) + "> tried redirecting a message by <@" + str(inter.target.author.id) +">! \nMessage Link: <#" + str(inter.channel.id) + ">")
                            )
        channel = bot.get_channel(logs_channel)
        await channel.send(embed=embed)


# ON STARTUP
@bot.event
async def on_ready():
    emb = disnake.Embed(color=disnake.Colour.green(), title=("**Bot started**"))
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(logs_channel)
    await channel.send(embed=emb)


bot.run(token)
