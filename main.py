import disnake
import requests
from bs4 import BeautifulSoup
from disnake.ext import commands
from bot_token import token
from markdownify import markdownify as md

intents = disnake.Intents.all()

activity = disnake.Activity(
    name="out for your commands",
    type=disnake.ActivityType.watching,
)

bot = commands.Bot(command_prefix="?", intents=intents, activity=activity)

logs_channel = 1108080080711852042
description = ""

# WEIRD ENUM STUFF
invites = commands.option_enum(["datapack hub", "minecraft commands", "shader labs", "bot", "smithed", "blockbench", "optifine", "fabric"])


# FUNCTIONS
def get_log_channel():
    global channel
    channel = bot.get_channel(logs_channel)


# MESSAGE COMMANDS


# redirect to help channel
@bot.message_command(name="Redirect to Help Channel")
async def claim(inter: disnake.MessageCommandInteraction):
    redi_ban_role = bot.get_guild(935560260725379143).get_role(1108093399053111387)
    if inter.guild.id != 935560260725379143:
        await inter.response.send_message(
            "You can only use this in the [Datapack Hub discord server](<https://dsc.gg/datapack>)!",
            ephemeral=True,
        )
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Redirect to Help Channel**"),
            description=(
                str(inter.user.name) + " tried using this in a different server lol"
            ),
        )
        get_log_channel()
        await channel.send(embed=embed)
        return
    if redi_ban_role in inter.author.roles:
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
                + "> tried redirecting a message by <@"
                + str(inter.target.author.id)
                + "> \nMessage Link: <#"
                + str(inter.channel.id)
                + ">"
            ),
        )
        get_log_channel()
        await channel.send(embed=embed)
        return

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
        name=("Requested by " + inter.author.name),
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
            + " redirected a message by "
            + str(inter.user.name)
            + "! \nMessage Link: <#"
            + str(inter.channel.id)
            + ">"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


# SLASH COMMANDS


# /syntax
@bot.slash_command(
    title="syntax", description="Shows the correct syntax of any minecraft command"
)
async def syntax(inter: disnake.ApplicationCommandInteraction, command: str):
    request = requests.get(
        f"https://minecraft.fandom.com/wiki/commands/{command}", timeout=5000
    )
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
                if command.lower != "execute" and not "trigger":
                    dl = h2.find_next("dl")
                elif command == "execute":
                    dl = h2.find_next("dl").find_next("dl")
                elif command == "trigger":
                    dl = "`trigger <objective>`\n   Adds `1` to the current value of `<objective>`.\n`trigger <objective> add <value>`\n    Adds `<value>` to the current value of `<objective>`.\n?`trigger <objective> set <value>`\n Sets the value of `<objective>` to `<value>`."

                if command.lower != "trigger":
                    dl = h2.find_next("dl")
                    description_v2 = md(str(dl), convert=["code", "li", "ul"]).replace(
                        "/wiki", "https://minecraft.fandom.com/wiki"
                    )
                else:
                    description_v2 = dl
                
            
                print(description_v2)

    embed = disnake.Embed(
        title=command.title() + " Syntax" + bedrock_notice,
        description=description_v2,
        color=disnake.Colour.orange(),
    )
    
    embed.set_footer(
        text = ("Information borrowed from: minecraft.fandom.com/wiki/Commands/" + command)
        )

    await inter.response.send_message(embed=embed)

    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/syntax` Command**"),
        description=(
            str(inter.user.name)
            + " looked up the following command: `"
            + str(command)
            + "`"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


# /resolve
@bot.slash_command(title="resolve", description="Marks question as resolved")
async def resolve(inter: disnake.ApplicationCommandInteraction):
    helper_role = bot.get_guild(935560260725379143).get_role(935561184806060073)

    try:
        channel = inter.channel.parent.id
        if (inter.channel.owner.id == inter.author.id) or (
            helper_role in inter.author.roles
        ):
            if channel == 1051225367807000706 or 1051227454980755546:
                resolved_tag = inter.channel.parent.get_tag_by_name("RESOLVED")
                await inter.channel.add_tags(resolved_tag)
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title="Resolve Help Channel",
                    description=":white_check_mark:   Marked this channel as resolved!",
                )
                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`/resolve` Command**"),
                    description=(str(inter.user.name) + " resolved a help channel`"),
                )
                get_log_channel()
                await channel.send(embed=embed)
                await inter.response.send_message(embed=embed)
            else:
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title="Resolve Help Channel",
                    description="You can only do this in one of our help channels",
                )
                await inter.response.send_message(embed=embed, ephemeral=True)

        else:
            embed = disnake.Embed(
                color=disnake.Color.orange(),
                title="Resolve Help Channel",
                description="Only the creator of this question and helpers can mark it as resolved",
            )
            await inter.response.send_message(embed=embed, ephemeral=True)

    except:
        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title="Resolve Help Channel",
            description="You can only do this in one of our help channels",
        )

        await inter.response.send_message(embed=embed, ephemeral=True)


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
            str(inter.user.name) + " looked up the folderstructure of `resourcepacks`"
        ),
    )
    get_log_channel()
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
        ├── tags 
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
            str(inter.user.name) + " looked up the folderstructure of `datapacks`"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


# /invite
@bot.slash_command(
    title="invite",
    description="Shows discord invite for a discord server relevant to datapacks",
)
async def invite(inter: disnake.ApplicationCommandInteraction, invite: invites):
    if invite == "datapack hub":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Datapack Hub Invite**"),
            description="Join Datapack Hub for help with your Datapacks and support regarding this bot using this link: https://dsc.gg/datapack",
        )

    elif invite == "minecraft commands":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Minecraft Commands Invite**"),
            description="Join Minecraft Commands for help regarding your Datapacks using this link: https://discord.gg/QAFXFtZ",
        )

    elif invite == "shader labs":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**ShaderLABS Invite**"),
            description="Join ShaderLABS for help regarding shaders using this link: https://discord.gg/Ayav9YPQra",
        )
    elif invite == "bot":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Datapack Helper Invite**"),
            description="Add the Datapack Helper bot to your server using this link: *COMING SOON*",
        )
    elif invite == "smithed":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Smithed Invite**"),
            description="Join Smithed for information/help regarding the smithed datapacking conventions using this link: https://smithed.dev/discord",
        )
    elif invite == "blockbench":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Blockbench Invite**"),
            description="Join Blockbench for help regarding modeling and Blockbench using this link: https://discord.gg/blockbench",
        )
    elif invite == "optifine":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Optifine Invite**"),
            description="Join Optifine for help regarding (problems with) Optifine using this link: https://discord.gg/optifine",
        )
    elif invite == "fabric":
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Fabric Invite**"),
            description="Join The Fabric Project for information/help regarding Fabric using this link: https://discord.gg/DtevV9NmaR",
        )
    
    await inter.response.send_message(embed=embed)
    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/invite` Command**"),
        description=(
            str(inter.user.name) + " looked up the invite of `" + str(invite) + "`"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


# /packformat
@bot.slash_command()
async def packformat(inter):
    pass


@packformat.sub_command(description="Shows history of resourcepack pack formats")
async def resourcepack(inter: disnake.ApplicationCommandInteraction):
    request = requests.get(
        "https://minecraft.fandom.com/wiki/Pack_format", timeout=5000
    )
    request = BeautifulSoup(request.content, "html.parser")
    description = ""
    trs = request.find_all("tr")
    for tr in trs:
        value = tr.find_next("td")
        versions = value.find_next("td")
        full_versions = versions.find_next("td")
        # print (md(str(full_versions)))
        if "—" not in md(str(full_versions)):
            full_versions = " (`" + str(full_versions) + "`)"
        else:
            full_versions = ""

        if value.find_previous("h2").find_next("span").text == "Resources":
            #   print((md(("(RP) \nValue: " + str(value) + "\nVersions: " + str(versions)),strip=['a','td'])).replace("[*verify*]",""))
            description += md(
                (
                    "Format: "
                    + str(value)
                    + "      Versions: `"
                    + str(versions)
                    + "`"
                    + full_versions
                    + "\n"
                ),
                strip=["a", "td"],
            ).replace("[*verify*]", "")
        else:
            pass

    embed = disnake.Embed(
        color=disnake.Color.orange(),
        title="Resourcepack Pack Format History",
        description=description,
    )
    await inter.response.send_message(embed=embed)

    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/packformat` Command**"),
        description=(
            str(inter.user.name)
            + " looked up the packformat history of `resourcepacks`"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


@packformat.sub_command(description="Shows history of datapack pack formats")
async def datapack(inter: disnake.ApplicationCommandInteraction):
    request = requests.get(
        "https://minecraft.fandom.com/wiki/Pack_format", timeout=5000
    )
    request = BeautifulSoup(request.content, "html.parser")
    description = ""
    trs = request.find_all("tr")
    for tr in trs:
        value = tr.find_next("td")
        versions = value.find_next("td")
        full_versions = versions.find_next("td")
        # print (md(str(full_versions)))
        if "—" not in md(str(full_versions)):
            full_versions = " (`" + str(full_versions) + "`)"
        else:
            full_versions = ""

        if value.find_previous("h2").find_next("span").text == "Data":
            #  print((md(("(RP) \nValue: " + str(value) + "\nVersions: " + str(versions)),strip=['a','td'])).replace("[*verify*]",""))
            description += md(
                (
                    "Format: "
                    + str(value)
                    + "      Versions: `"
                    + str(versions)
                    + "`"
                    + full_versions
                    + "\n"
                ),
                strip=["a", "td"],
            ).replace("[*verify*]", "")
        else:
            pass

    embed = disnake.Embed(
        color=disnake.Color.orange(),
        title="Datapack Pack Format History",
        description=description,
    )
    await inter.response.send_message(embed=embed)

    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/packformat` Command**"),
        description=(
            str(inter.user.name) + " looked up the packformat history of `datapacks`"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


# /info
@bot.slash_command()
async def info(inter):
    pass


# /info logs
@info.sub_command(description="Shows you how to access the minecraft logs")
async def logs(inter: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        color=disnake.Color.orange(),
        title="Logs :wood:",
        description="The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! \nTo open the logs:\n 1. **Enable** logs in the Minecraft **Launcher** \n2. **Start** your **game** (or restart it if you already have an open instance) \n3. Enjoy **spotting errors** getting much **easier**!",
    )
    embed.set_image(
        url="https://media.discordapp.net/attachments/1129493191847071875/1129494068603396096/how-to-logs.png?width=1277&height=897"
    )
    await inter.response.send_message(embed=embed)

    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/info` Command**"),
        description=(str(inter.user.name) + " gained knowledge about `Logs`!"),
    )
    get_log_channel()
    await channel.send(embed=embed)


# /info me
@info.sub_command(description="Shows some cool information about me (this bot)!")
async def me(inter: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        color=disnake.Color.orange(),
        title="Datapack Helper <:datapackhelper:1129499893216579614>",
        description="Woah, you are interested in me? :exploding_head: \nWell of course, I would be too! :sunglasses: \nI am a (some would argue the greatest :fire:) bot to help you with everything datapacks! Wether you are looking for a simple template, forgot how to enable the logs or want to know which pack format is the latest, I got you covered! :cold_face: :hot_face:\nAll of this is made possible by the amazing team of Datapack Hub! :duck:",
    )
    await inter.response.send_message(embed=embed)

    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/info` Command**"),
        description=(
            str(inter.user.name) + " gained knowledge about `our really cool bot`!"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


# /info editor
@info.sub_command(description="Shows information about our editor of choice!")
async def editor(inter: disnake.ApplicationCommandInteraction):
    embed = disnake.Embed(
        color=disnake.Color.orange(),
        title="Datapack Helper",
        description='While you can make datapacks using any ordinary text editor, our prefered editor of choice is [VSCode](https://code.visualstudio.com/)! \nIt is aviable for Windows, Linux and MacOS (which means it runs on almost all devices) and has lots of great extensions which make the creation of datapacks a whole lot easier!\n\nOur favourite VSCode extensions are:\n[language-mcfunction](https://marketplace.visualstudio.com/items?itemName=arcensoth.language-mcfunction) - Provides beautiful syntax highlighting for .mcfunction\n[Data-pack Helper Plus](https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server) - Despite how "datapack" is spelled in the title, this adds some really helpful features like auto completion for commands!\n[NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt) - Allows you to view 3D models of your `.nbt` files, directly in VSCode!\n[Datapack Icons](https://marketplace.visualstudio.com/items?itemName=SuperAnt.mc-dp-icons) - Adds cool icons to datapack folders and files',
    )
    await inter.response.send_message(embed=embed)

    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/info` Command**"),
        description=(str(inter.user.name) + " gained knowledge about `vscode`!"),
    )
    get_log_channel()
    await channel.send(embed=embed)


# OTHER EVENTS


# ON MESSAGE
@bot.event
async def on_message(message):
    cc_channel = bot.get_channel(935566919933755432)
    intro_channel = bot.get_channel(936721793677414490)

    if message.channel == cc_channel:
        if message.author.nick:
            await cc_channel.create_thread(
                name=(message.author.nick + "'s Creation"), message=message
            )
        else:
            await cc_channel.create_thread(
                name=(message.author.name + "'s Creation"), message=message
            )

        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Community Creations Thread**"),
            description=(
                "Created a thread for "
                + message.author.name
                + "'s message in <#935566919933755432>"
            ),
        )
        get_log_channel()
        await channel.send(embed=embed)
    elif message.channel == intro_channel:
        await message.add_reaction("👋")

        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Intro Channel Reaction**"),
            description=(
                "Reacted with :wave: to "
                + message.author.name
                + "'s message in <#936721793677414490>"
            ),
        )
        get_log_channel()
        await channel.send(embed=embed)


# ON STARTUP
@bot.event
async def on_ready():
    embed = disnake.Embed(color=disnake.Colour.green(), title="**Bot started**")
    print(f"Logged in as {bot.user}")
    get_log_channel()
    await channel.send(embed=embed)


bot.run(token)
