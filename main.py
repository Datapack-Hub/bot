# invite link, don't share for now: https://discord.com/oauth2/authorize?client_id=1108074519308017734&scope=bot&permissions=517611048000

import disnake
import requests
from bs4 import BeautifulSoup
from disnake.ext import commands
from bot_token import token
from markdownify import markdownify as md
import os
import asyncio
import variables
import datetime
from disnake.ext import tasks

intents = disnake.Intents.all()

activity = disnake.Activity(
    name="out for your commands",
    type=disnake.ActivityType.watching,
)

bot = commands.Bot(
    command_prefix="?",
    intents=intents,
    activity=activity,
    test_guilds=variables.test_guilds,
)

logs_channel = variables.logs
guild = variables.main_guild
redirect_ban_role = variables.redirect_ban_role
datapack_channel = variables.datapack_help_channel
resourcepack_channel = variables.resourcepack_help_channel
suggestion_channel = variables.suggestion_channel
intro_channel = variables.intro_channel
methods_channel = variables.methods_channel
helper_role = variables.helper_role

description = ""

# WEIRD ENUM STUFF
invites = commands.option_enum(
    [
        "datapack hub",
        "minecraft commands",
        "shader labs",
        "bot",
        "smithed",
        "blockbench",
        "optifine",
        "fabric",
    ]
)

infos = commands.option_enum(["logs", "me", "editor"])

methods = os.listdir("./method")

for idx, ele in enumerate(methods):
    methods[idx] = ele.replace(".txt", "")

methods_enum = commands.option_enum(methods)


# CLASSES
class SubmitMethod(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput(
                label="Title",
                placeholder="Title of method",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Description",
                placeholder="Description of method",
                custom_id="description",
                style=disnake.TextInputStyle.paragraph,
                min_length=10,
                max_length=1024,
            ),
        ]
        super().__init__(
            title="Submit New Method", custom_id="submitmethod", components=components
        )

    async def callback(self, inter: disnake.ModalInteraction):
        method_name = inter.text_values["name"]
        method_content = inter.text_values["description"]

        embed = disnake.Embed(
            title=method_name, description=method_content, color=disnake.Color.orange()
        )

        accept_button = disnake.ui.Button(
            label="Accept",
            custom_id="accept_method_button",
            style=disnake.ButtonStyle.green,
            emoji="✅",
        )
        deny_button = disnake.ui.Button(
            label="Deny",
            custom_id="deny_method_button",
            style=disnake.ButtonStyle.red,
            emoji="❌",
        )
        edit_button = disnake.ui.Button(
            label="Edit",
            custom_id="edit_method_button",
            style=disnake.ButtonStyle.secondary,
            emoji="✏️",
        )

        channel = bot.get_channel(methods_channel)
        await channel.send(
            embed=embed, components=[accept_button, deny_button, edit_button]
        )

        await inter.response.send_message(
            "Successfully submitted method suggestion!", ephemeral=True
        )

    async def on_error(self, error: Exception, inter: disnake.ModalInteraction):
        await inter.response.send_message(
            f"Oops, something went wrong.```\n{' '.join(error.args)}```", ephemeral=True
        )


class EditMethod(disnake.ui.Modal):
    def __init__(self, id: int, title: str, description: str) -> None:
        components = [
            disnake.ui.TextInput(
                label="Title",
                placeholder="Title of method",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50,
                value=title,
            ),
            disnake.ui.TextInput(
                label="Description",
                placeholder="Description of method",
                custom_id="description",
                style=disnake.TextInputStyle.paragraph,
                min_length=10,
                max_length=1024,
                value=description,
            ),
        ]
        super().__init__(
            title="Edit Method",
            custom_id="submitmethod_" + str(id),
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        method_name = inter.text_values["name"]
        method_content = inter.text_values["description"]

        msg_id = inter.custom_id.split("_")[1]

        embed = disnake.Embed(
            title=method_name, description=method_content, color=disnake.Color.orange()
        )

        accept_button = disnake.ui.Button(
            label="Accept",
            custom_id="accept_method_button",
            style=disnake.ButtonStyle.green,
            emoji="✅",
        )
        deny_button = disnake.ui.Button(
            label="Deny",
            custom_id="deny_method_button",
            style=disnake.ButtonStyle.red,
            emoji="🗑️",
        )
        edit_button = disnake.ui.Button(
            label="Edit",
            custom_id="edit_method_button",
            style=disnake.ButtonStyle.secondary,
            emoji="✏️",
        )

        msg = bot.get_message(msg_id)
        await msg.edit(
            embed=embed, components=[accept_button, deny_button, edit_button]
        )

        await inter.response.send_message(
            "Successfully edited method suggestion!", ephemeral=True
        )

    async def on_error(self, error: Exception, inter: disnake.ModalInteraction):
        await inter.response.send_message(
            f"Oops, something went wrong.```\n{' '.join(error.args)}```", ephemeral=True
        )


# FUNCTIONS
def get_log_channel():
    global channel
    channel = bot.get_channel(logs_channel)


# MESSAGE COMMANDS


# redirect to help channel
@bot.message_command(name="Redirect to Help Channel")
async def claim(inter: disnake.MessageCommandInteraction):
    redi_ban_role = bot.get_guild(guild).get_role(1031577795748450346)
    if inter.guild.id != guild:
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
        description="It seems like someone here found your question to be more fitting in our help channels! \nHelp channels are the perfect place to ask questions and to be answered by anyone including our experienced helpers!\nVisit <#"
        + str(datapack_channel)
        + "> or <#"
        + str(resourcepack_channel)
        + "> if you require assistance.\nCheck out <#935570290317086841> for tips on asking questions efficiently.",
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
        text=(
            "Information borrowed from: minecraft.fandom.com/wiki/Commands/" + command
        )
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


# /method
@bot.slash_command(
    title="method",
    description="Shows information about methods commonly used by datapacks",
)
async def method(inter: disnake.ApplicationCommandInteraction, method: methods_enum):
    opened_file = open(("./method/" + str(method) + ".txt"), "r")
    file_content = opened_file.read()
    print("Method Description: " + file_content)
    opened_file.close()

    embed = disnake.Embed(
        title=method.title(), description=file_content, color=disnake.Colour.orange()
    )

    await inter.response.send_message(embed=embed)


# /submit-method
@bot.slash_command(
    title="submitmethod",
    description="Submit a method to be usable by the `/method` command",
)
async def submitmethod(inter: disnake.CommandInteraction):
    await inter.response.send_modal(modal=SubmitMethod())


# /resolve
@bot.slash_command(title="resolve", description="Marks question as resolved")
async def resolve(inter: disnake.ApplicationCommandInteraction):
    role = bot.get_guild(guild).get_role(helper_role)

    try:
        channel = inter.channel.parent.id
        if (inter.channel.owner.id == inter.author.id) or (role in inter.author.roles):
            if channel == datapack_channel or resourcepack_channel:
                resolved_tag = inter.channel.parent.get_tag_by_name("RESOLVED")
                await inter.channel.add_tags(resolved_tag)
                embed = disnake.Embed(
                    color=disnake.Color.green(),
                    title=":white_check_mark: Resolve Help Channel",
                    description="Marked this channel as resolved!",
                )
                await inter.response.send_message(embed=embed)
                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`/resolve` Command**"),
                    description=(str(inter.user.name) + " resolved a help channel`"),
                )
                get_log_channel()
                await channel.send(embed=embed)
                await inter.response.send_message(embed=embed)
            elif not role in inter.author.roles:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="❌ Resolve Help Channel",
                    description="You can only do this in one of our help channels",
                )
                await inter.response.send_message(embed=embed, ephemeral=True)

        else:
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="❌ Resolve Help Channel",
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
@bot.slash_command(
    title="info",
    description="Gives you more information about an external feature to improve your datapacking experience",
)
async def info(inter: disnake.ApplicationCommandInteraction, info: infos):
    if info == "logs":
        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title="Logs :wood:",
            description="The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! \nTo open the logs:\n 1. **Enable** logs in the Minecraft **Launcher** \n2. **Start** your **game** (or restart it if you already have an open instance) \n3. Enjoy **spotting errors** getting much **easier**!",
        )
        embed.set_image(
            url="https://media.discordapp.net/attachments/1129493191847071875/1129494068603396096/how-to-logs.png?width=1277&height=897"
        )

    elif info == "me":
        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title="Datapack Helper <:datapackhelper:1129499893216579614>",
            description="Woah, you are interested in me? :exploding_head: \nWell of course, I would be too! :sunglasses: \nI am a (some would argue the greatest :fire:) bot to help you with everything datapacks! Wether you are looking for a simple template, forgot how to enable the logs or want to know which pack format is the latest, I got you covered! :cold_face: :hot_face:\nAll of this is made possible by the amazing team of Datapack Hub! :duck:",
        )

    elif info == "editor":
        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title="Datapack Helper",
            description='While you can make datapacks using any ordinary text editor, our prefered editor of choice is [VSCode](https://code.visualstudio.com/)! \nIt is aviable for Windows, Linux and MacOS (which means it runs on almost all devices) and has lots of great extensions which make the creation of datapacks a whole lot easier!\n\nOur favourite VSCode extensions are:\n[language-mcfunction](https://marketplace.visualstudio.com/items?itemName=arcensoth.language-mcfunction) - Provides beautiful syntax highlighting for .mcfunction\n[Data-pack Helper Plus](https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server) - Despite how "datapack" is spelled in the title, this adds some really helpful features like auto completion for commands!\n[NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt) - Allows you to view 3D models of your `.nbt` files, directly in VSCode!\n[Datapack Icons](https://marketplace.visualstudio.com/items?itemName=SuperAnt.mc-dp-icons) - Adds cool icons to datapack folders and files',
        )

    await inter.response.send_message(embed=embed)
    embed = disnake.Embed(
        color=disnake.Colour.orange(),
        title=("**`/info` Command**"),
        description=(str(inter.user.name) + " gained knowledge about `" + info + "`!"),
    )
    get_log_channel()
    await channel.send(embed=embed)


# /suggest
@bot.slash_command(
    title="suggest",
    description="Suggest a new feature for the bot",
)
async def suggest(inter: disnake.ApplicationCommandInteraction, suggestion: str):
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

    embed.set_author(
        name=("Suggested by " + inter.user.name),
        icon_url=inter.user.display_avatar,
    )
    channel = bot.get_channel(suggestion_channel)
    await channel.send(embed=embed)


# OTHER EVENTS


# ON MESSAGE
@bot.event
async def on_message(message):
    intro_channel = bot.get_channel(variables.intro_channel)

    if message.channel == intro_channel:
        await message.add_reaction("👋")

        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Intro Channel Reaction**"),
            description=(
                "Reacted with :wave: to "
                + message.author.name
                + "'s message in <#"
                + intro_channel
                + ">"
            ),
        )
        get_log_channel()
        await channel.send(embed=embed)
    elif ("flyrr_" == message.author.name) and (">.< shutdown" in message.content):
        methods = os.listdir(".\\method")
        methods_enum = commands.option_enum(methods)
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.purple(),
            title=("**Magic** :sparkles:"),
            description=(
                "The bot was forced to shutdown by some strange magical power...\nNew Contents: `"
                + str(methods)
                + "`"
            ),
        )
        get_log_channel()
        await channel.send(embed=embed)
        await bot.close()


# ON BUTTON CLICK
@bot.listen("on_button_click")
async def button_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id == "accept_method_button":
        await inter.response.send_message("Accepted suggestion!", ephemeral=True)
        title = inter.message.embeds[0].title
        description = inter.message.embeds[0].description
        file = open("./method/" + title.lower() + ".txt", "w")

        file.write(description)
        file.close

        embed = disnake.Embed(
            title=title, description=description, color=disnake.Color.green()
        )

        await inter.message.edit(embed=embed, components=[])

    if inter.component.custom_id == "deny_method_button":
        await inter.response.send_message("Denied suggestion!", ephemeral=True)
        title = inter.message.embeds[0].title
        description = inter.message.embeds[0].description
        embed = disnake.Embed(
            title=title, description=description, color=disnake.Color.red()
        )

        await inter.message.edit(embed=embed, components=[])

    if inter.component.custom_id == "edit_method_button":
        await inter.response.send_modal(
            EditMethod(
                inter.message.id,
                inter.message.embeds[0].title,
                inter.message.embeds[0].description,
            )
        )

    if inter.component.custom_id == "resolve_question_button":
        role = bot.get_guild(guild).get_role(helper_role)
        channel = inter.channel.parent.id
        if (inter.channel.owner.id == inter.user.id) or (role in inter.user.roles):
            resolved_tag = inter.channel.parent.get_tag_by_name("RESOLVED")
            await inter.channel.add_tags(resolved_tag)
            embed = disnake.Embed(
                color=disnake.Color.green(),
                title=":white_check_mark: Resolve Help Channel",
                description="Marked this channel as resolved!",
            )
            await inter.response.send_message(embed=embed)
            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**`Resolve Help Channel` Button**"),
                description=(str(inter.user.name) + " resolved a help channel"),
            )
            channel = bot.get_channel(logs_channel)
            await channel.send(embed=embed)

        else:
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="❌ Resolve Help Channel",
                description="You can't do this since you are neither a helper nor the owner of this channel!",
            )
            await inter.response.send_message(embed=embed, ephemeral=True)
            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**`Resolve Help Channel` Button**"),
                description=(
                    str(inter.user.name) + " failed resolving a help channel`"
                ),
            )
            channel = bot.get_channel(logs_channel)
            await channel.send(embed=embed)

    if inter.component.custom_id == "summon_helpers_button":
        creation_time = inter.channel.create_timestamp
        current_time = datetime.datetime.now(creation_time.tzinfo)
        time_difference = current_time - creation_time

        time_difference_seconds = time_difference.total_seconds()
        time_difference_minutes = time_difference_seconds / 60

        role = bot.get_guild(guild).get_role(helper_role)
        channel = inter.channel.parent.id
        if (inter.channel.owner.id == inter.author.id) or (role in inter.author.roles):
            if time_difference_minutes >= 30:
                embed = disnake.Embed(
                    color=disnake.Colour.blue(),
                    title=("**🙇 Helpers Arise!**"),
                    description=(
                        "Please note that you still might not immediately get a response since all helpers are human beings and volunteers (and also might be sleeping right now)"
                    ),
                )
                await inter.response.send_message(
                    "<@&" + str(variables.helper_role) + ">",
                    embed=embed,
                    allowed_mentions=disnake.AllowedMentions(roles=True),
                )
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**Someone will come and help soon!**"),
                    description=(
                        "💬 While you wait, take this time to provide more context and details. What are you trying to achieve overall - maybe there’s an easier way to solve this problem\n\n🙇 ~~If it’s been 20 minutes and you’re still waiting for someone to help, hit the __Summon Helpers__ button to call the official helpers here~~ **Someone has already summoned the helpers in this help channel!**\n\n✅ Once your question has been resolved (or you no longer need it), hit the __Resolve Question__ button or run /resolve"
                    ),
                )
                resolve_question_button = disnake.ui.Button(
                    label="Resolve Question",
                    custom_id="resolve_question_button",
                    style=disnake.ButtonStyle.green,
                    emoji="✅",
                )

                await inter.message.edit(
                    embed=embed, components=[resolve_question_button]
                )

                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`Summon Helpers` Button**"),
                    description=(str(inter.user.name) + " summoned helper"),
                )
                channel = bot.get_channel(logs_channel)
                await channel.send(embed=embed)

            else:
                embed = disnake.Embed(
                    color=disnake.Colour.red(),
                    title=("**🕑 Be patient!**"),
                    description=(
                        "All helpers are volunteers and thus can't always respond instantly. We'd therefore advise you to give them some time! If you still haven't gotten an answer in `"
                        + str(30 - int(time_difference_minutes))
                        + " minutes` feel free to use this again to ping all helpers :D"
                    ),
                )
                await inter.response.send_message(embed=embed, ephemeral=True)
                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`Summon Helpers` Button**"),
                    description=(str(inter.user.name) + " failed summoning helpers`"),
                )
                channel = bot.get_channel(logs_channel)
                await channel.send(embed=embed)
        else:
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="❌ Summon Helpers",
                description="You can't do this since you are neither a helper nor the owner of this channel!",
            )
            await inter.response.send_message(embed=embed, ephemeral=True)

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**`Summon Helpers` Button**"),
                description=(str(inter.user.name) + " failed summoning helpers`"),
            )
            channel = bot.get_channel(logs_channel)
            await channel.send(embed=embed)


@bot.event
async def on_thread_create(thread):
    if thread.parent_id == (
        variables.datapack_help_channel or variables.resourcepack_help_channel
    ):
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Someone will come and help soon!**"),
            description=(
                "💬 While you wait, take this time to provide more context and details. What are you trying to achieve overall - maybe there’s an easier way to solve this problem\n\n🙇 If it’s been 20 minutes and you’re still waiting for someone to help, hit the __Summon Helpers__ button to call the official helpers here\n\n✅ Once your question has been resolved (or you no longer need it), hit the __Resolve Question__ button or run /resolve"
            ),
        )
        summon_helpers_button = disnake.ui.Button(
            label="Summon Helpers",
            custom_id="summon_helpers_button",
            style=disnake.ButtonStyle.blurple,
            emoji="🙇",
        )
        resolve_question_button = disnake.ui.Button(
            label="Resolve Question",
            custom_id="resolve_question_button",
            style=disnake.ButtonStyle.green,
            emoji="✅",
        )

        await thread.send(
            embed=embed, components=[summon_helpers_button, resolve_question_button]
        )


# ON GUILD JOIN
@bot.event
async def on_guild_join(guild):
    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.green(),
        title=("**Joined New Guild**"),
        description=(
            "Bot was added to the **"
            + str(guild.name)
            + "** (**"
            + str(guild.id)
            + "**) server"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)


@bot.event
async def on_guild_remove(guild):
    # Logging
    embed = disnake.Embed(
        color=disnake.Colour.red(),
        title=("**Left Guild**"),
        description=(
            "Bot was removed from the **"
            + str(guild.name)
            + "** (**"
            + str(guild.id)
            + "**) server"
        ),
    )
    get_log_channel()
    await channel.send(embed=embed)

# ON STARTUP
@bot.event
async def on_ready():
    slow_count.start()
    embed = disnake.Embed(color=disnake.Colour.green(), title="**Bot started**")
    print(f"Logged in as {bot.user}")
    get_log_channel()
    await channel.send(embed=embed)


bot.run(token)
