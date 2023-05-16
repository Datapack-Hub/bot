import disnake
from disnake.ext import commands
from bot_token import token

intents = disnake.Intents.all()

bot = commands.Bot(
    command_prefix="?", intents=intents, test_guilds=[935560260725379143]
)

logs_channel = 1108080080711852042

# MESSAGE COMMANDS


@bot.message_command(name="Redirect to Help Channel")
async def claim(inter: disnake.MessageCommandInteraction):
    redi_ban_role = bot.get_guild(935560260725379143).get_role(1108093399053111387)
    if redi_ban_role not in inter.author.roles:
        await inter.response.send_message(
            "Notified <@"
            + str(inter.target.author.id)
            + ">! Abusing this command will result in punishment.",
            ephemeral=True,
        )
        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title="This question would be more fitting inside of a Help Channel!",
            description="""Help channels are our way of handeling datapack development 
            related questions like yours, which is why you are recieving this message! 
            Once you send a message/create a post there, every person in this server 
            will be able to help you, including our experienced Helpers which you can 
            ping (after some time of course, don't be impatient) if nobody else seems 
            to know how to help you.\nIf you need help regarding Resource Packs, 
            head to <#1051227454980755546> and if you are experiencing struggles 
            developing your datapack <#1051225367807000706>! If you haven't already 
            check out <#935570290317086841> which has some tips for asking your 
            questions in the most efficent way!""",
        )

        embed.set_author(
            name=(
                "Requested by " + inter.author.name + "#" + inter.author.discriminator
            ),
            icon_url=inter.author.display_avatar,
        )

        embed.set_footer(
            text="If you feel this function was used unfitting/inappropriate on purpose, please contact a staff member."
        )
        await inter.target.reply(embed=embed)

        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Redirect to Help Channel**"),
            description=(
                "<@"
                + str(inter.user.id)
                + "> redirected a message by <@"
                + str(inter.target.author.id)
                + ">! \nMessage Link: <#"
                + str(inter.channel.id)
                + ">"
            ),
        )
        channel = bot.get_channel(logs_channel)
        await channel.send(embed=embed)

    else:
        await inter.response.send_message(
            "You are blacklisted from doing this. If you believe this is a miskate please contact a staff member.",
            ephemeral=True,
        )

        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Redirect to Help Channel**"),
            description=(
                "<@"
                + str(inter.user.id)
                + "> tried redirecting a message by <@"
                + str(inter.target.author.id)
                + ">! \nMessage Link: <#"
                + str(inter.channel.id)
                + ">"
            ),
        )
        channel = bot.get_channel(logs_channel)
        await channel.send(embed=embed)


# ON STARTUP
@bot.event
async def on_ready():
    embed = disnake.Embed(color=disnake.Colour.green(), title=("**Bot started**"))
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(logs_channel)
    await channel.send(embed=embed)


bot.run(token)
