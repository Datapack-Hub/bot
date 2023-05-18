import disnake
import requests
from bs4 import BeautifulSoup
from disnake.ext import commands
from bot_token import token
from markdownify import markdownify as md

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents)

logs_channel = 1108080080711852042
description = ""


# MESSAGE COMMANDS


@bot.message_command(name="Redirect to Help Channel")
async def claim(inter: disnake.MessageCommandInteraction):
    redi_ban_role = bot.get_guild(935560260725379143).get_role(1108093399053111387)
    if inter.guild.id == 935560260725379143:
        if redi_ban_role not in inter.author.roles:
            embed = disnake.Embed(
                color=disnake.Color.orange(),
                title="This question would be more fitting inside of a Help Channel!",
                description="""It seems like someone here found your question to be 
                more fitting in our help channels! \nHelp channels are the perfect 
                place to ask questions and to be answered by anyone including our 
                experienced helpers!\nVisit <#1051227454980755546> or 
                <#1051225367807000706> if you require assistance.\nCheck out 
                <#935570290317086841> for tips on asking questions efficiently.""",
            )

            embed.set_author(
                name=(
                    "Requested by "
                    + inter.author.name
                    + "#"
                    + inter.author.discriminator
                ),
                icon_url=inter.author.display_avatar,
            )

            embed.set_footer(
                text="If you feel this function was misused, please contact staff."
            )
            await inter.target.reply(embed=embed)

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Redirect to Help Channel**"),
                description=(
                    str(inter.user.name)
                    + "#"
                    + str(inter.user.discriminator)
                    + " redirected a message by "
                    + str(inter.user.name)
                    + "#"
                    + str(inter.user.discriminator)
                    + "! \nMessage Link: <#"
                    + str(inter.channel.id)
                    + ">"
                ),
            )
            channel = bot.get_channel(logs_channel)
            await channel.send(embed=embed)

        else:
            await inter.response.send_message(
                "You are blacklisted from doing this. If you believe this is a mistake please contact a staff member.",
                ephemeral=True,
            )

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Redirect to Help Channel**"),
                description=(
                    str(inter.user.name)
                    + "#"
                    + str(inter.user.discriminator)
                    + "> tried redirecting a message by <@"
                    + str(inter.target.author.id)
                    + "> \nMessage Link: <#"
                    + str(inter.channel.id)
                    + ">"
                ),
            )
            channel = bot.get_channel(logs_channel)
            await channel.send(embed=embed)
    else:
        await inter.response.send_message(
            "You can only use this in the [Datapack Hub discord server](<https://dsc.gg/datapack>)!",
            ephemeral=True,
        )
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Redirect to Help Channel**"),
            description=(
                str(inter.user.name)
                + "#"
                + str(inter.user.discriminator)
                + " tried using this in a different server lol"
            ),
        )
        channel = bot.get_channel(logs_channel)
        await channel.send(embed=embed)


# SLASH COMMANDS

# /syntax


@bot.slash_command(
    title="syntax", description="Shows the correct syntax of any minecraft command"
)
async def syntax(inter: disnake.ApplicationCommandInteraction, command: str):
    request = requests.get("https://minecraft.fandom.com/wiki/commands/" + command)
    request = BeautifulSoup(request.content, "html.parser")
    description_v2 = (
        "This command does not exist! Make sure to check spelling before trying again."
    )

    if "There is currently no text in this page. You can" not in str(request.text):
        h2s = request.find_all("h2")
        if (
            "This article describes content that may be included in Bedrock Edition."
            in request.text
        ):
            bedrock_notice = " (Bedrock Only)"
        else:
            bedrock_notice = ""
        for h2 in h2s:
            if "Syntax" in h2.text:
                if not command == "execute":
                    dl = h2.find_next("dl")

                else:
                    dl = h2.find_next("dl").find_next("dl")
                description_v2 = md(str(dl), convert=["code", "li","ul"]).replace(
                    "/wiki", "https://minecraft.fandom.com/wiki"
                )
                print(description_v2)

    embed = disnake.Embed(
        title=command.title() + " Syntax" + bedrock_notice,
        description=description_v2,
        color=disnake.Colour.orange(),
    )

    await inter.response.send_message(embed=embed)

    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/syntax` Command**"),
        description=(
            str(inter.user.name)
            + "#"
            + str(inter.user.discriminator)
            + " looked up the following command: `"
            + str(command)
            + "`"
        ),
    )
    channel = bot.get_channel(logs_channel)
    await channel.send(embed=embed)


# /folderstructure
@bot.slash_command()
async def folderstructure(inter):
    pass


@folderstructure.sub_command(description="Shows the folderstructure for resourcepacks")
async def resourcepack(inter: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        title="Resourcepack Folderstructure",
        description="""```
.
├── pack.mcmeta
├── pack.png
└── assets    
    ├── icons    
    ├── minecraft    
    │   ├── sounds.json    
    │   ├── blockstates    
    │   ├── font    
    │   ├── gpu_warnlist.json    
    │   ├── icons    
    │   ├── lang    
    │   ├── models    
    │   ├── particles    
    │   ├── resourcepacks    
    │   ├── shaders    
    │   ├── sounds    
    │   ├── texts    
    │   └── textures    
    ├── pack.mcmeta    
    └── realms        
        ├── lang        
        └── textures
        ```""",
        color=disnake.Colour.orange(),
    )
    await inter.response.send_message(embed=embed)
    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/folderstructure` Command**"),
        description=(
            str(inter.user.name)
            + "#"
            + str(inter.user.discriminator)
            + " looked up the folderstructure of `resourcepacks`"
        ),
    )
    channel = bot.get_channel(logs_channel)
    await channel.send(embed=embed)


@folderstructure.sub_command(description="Shows the folderstructure for datapacks")
async def datapack(inter: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        title="Datapack Folderstructure",
        description="""```
.
├── pack.mcmeta
├── pack.png
└── data
    └── <namespace>
        ├── advancements
        ├── functions
        ├── item_modifiers
        ├── loot_tables
        ├── predicates
        ├── recipes
        ├── structures
        ├── chat_type
        ├── damage_type
        │   ├── tags 
        │   ├── blocks
        │   ├── entity_types
        │   ├── fluids
        │   ├── functions
        │   ├── game_events
        │   ├── items
        │   ├── chat_type
        │   └── damage_type
        ├── dimension
        ├── dimension_type
        └── worldgen
            ├── biome
            ├── configured_carver
            ├── configured_feature
            ├── density_function
            ├── noise
            ├── noise_settings
            ├── placed_feature
            ├── processor_list
            ├── structure
            ├── structure_set
            ├── template_pool
            ├── world_preset
            └── flat_level_generator_preset
        ```""",
        color=disnake.Colour.orange(),
    )
    await inter.response.send_message(embed=embed)
    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/folderstructure` Command**"),
        description=(
            str(inter.user.name)
            + "#"
            + str(inter.user.discriminator)
            + " looked up the folderstructure of `datapacks`"
        ),
    )
    channel = bot.get_channel(logs_channel)
    await channel.send(embed=embed)


# ON STARTUP
@bot.event
async def on_ready():
    embed = disnake.Embed(color=disnake.Colour.green(), title="**Bot started**")
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(logs_channel)
    await channel.send(embed=embed)


bot.run(token)
