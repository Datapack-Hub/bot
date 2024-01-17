import disnake
import variables
from disnake.ext import commands

infos = commands.option_enum(
    ["logs default", "me", "editor", "logs other", "update rp 1.19.3+"]
)


class InfoCommand(commands.Cog, name="info"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="info",
        description="Gives you more information about an external feature to improve your datapacking experience",
    )
    async def info(self, inter: disnake.ApplicationCommandInteraction, info: infos):
        match info:
            case "logs default":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=":information_source: Default Launcher Logs",
                    description="The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! \nTo open the logs:\n 1. **Enable** logs in the Minecraft **Launcher** \n2. **Start** your **game** (or restart it if you already have an open instance) \n3. Enjoy **spotting errors** getting much **easier**!",
                )
                embed.set_image(
                    url="https://media.discordapp.net/attachments/1129493191847071875/1129494068603396096/how-to-logs.png?width=1277&height=897"
                )
            case "logs other":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=":information_source: Other Launcher Logs",
                    description="The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! Opening logs works different for different 3rd party launchers, here's a quick summary for the most popular ones\n\n**Prism Launcher**\n`Rightclick Instance` > `Edit` > `Settings` > `Console Settings: Show console while the game is running?`\n\n**Multi MC**\n`Rightclick Instance` > `Edit Instance` > `Settings` > `Console Settings: Show console while the game is running?`\n\n**Lunar Client**\n`Settings` > `Open Logs in File Explorer`",
                )

            case "me":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=":information_source: Datapack Helper <:datapackhelper:1129499893216579614>",
                    description="Woah, you are interested in me? :exploding_head: \nWell of course, I would be too! :sunglasses: \nI am a (some would argue the greatest :fire:) bot to help you with everything datapacks! Whether you are looking for a simple template, forgot how to enable the logs or want to know which pack format is the latest, I got you covered! :cold_face: :hot_face:\nAll of this is made possible by the amazing team of Datapack Hub! :duck:",
                )

            case "editor":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=":information_source: Editor",
                    description='While you can make datapacks using any ordinary text editor, our prefered editor of choice is [VSCode](https://code.visualstudio.com/)! \nIt is aviable for Windows, Linux and MacOS (which means it runs on almost all devices) and has lots of great extensions which make the creation of datapacks a whole lot easier!\n\nOur favourite VSCode extensions are:\n[syntax-mcfunction](https://marketplace.visualstudio.com/items?itemName=MinecraftCommands.syntax-mcfunction) - Provides beautiful syntax highlighting for .mcfunction\n[Data-pack Helper Plus](https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server) - Despite how "datapack" is spelled in the title, this adds some really helpful features like auto completion for commands!\n[NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt) - Allows you to view 3D models of your `.nbt` files, directly in VSCode!\n[Datapack Icons](https://marketplace.visualstudio.com/items?itemName=SuperAnt.mc-dp-icons) - Adds cool icons to datapack folders and files\n\n[Datapack Extensions](https://marketplace.visualstudio.com/items?itemName=amandin.dpc-pack) - Extension pack containing quite a few cool extensions to help with datapacking, including some of the above',
                )
            case "update rp 1.19.3+":
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title=":information_source: Updating Resourcepacks Past 1.19.3",
                    description="1.19.3 introduced a change to resourcepacks which means that textures which aren't stored in `textures/item` or `textures/block` won't be loaded into the game by default. This means that most resource packs for earlier versions won't work in 1.19.3. \n\nThere are two ways to fix this:\n- Move your custom textures into `assets/minecraft/textures/item/...`, since all textures in the `item` (or `block`) folders are loaded by default.\n- Create an atlas file for your custom textures. An atlas file basically tells Minecraft to always load the textures in your custom folder. [This video](https://youtu.be/MHWX_GaK2g0) will explain how to do this.",
                )
            # case "starting out":
            #     embed = disnake.Embed(
            #         color=disnake.Color.orange(),
            #         title="Starting Out 🧒",
            #         description='Here are some tutorials for beginners:\nBasic Datapacking Tutorial by Legitimoose: https://www.youtube.com/watch?v=ac6V5-KT6Rg\nMore uwu',
            #     )

        await inter.response.send_message(embed=embed)
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/info` Command**"),
            description=(
                str(inter.user.name)
                + " gained knowledge about `"
                + info
                + "`! (Server: **"
                + inter.guild.name
                + "**)"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
