from pathlib import Path
import disnake
from disnake.ext import commands
import variables
import os

template = commands.option_enum(["datapack", "resourcepack"])


class TemplateCommand(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="template",
        description="Shows discord invite for a discord server relevant to datapacks",
    )
    async def template(
        self, inter: disnake.ApplicationCommandInteraction, template: template = "datapack"
    ):
        if template == "datapack":
            # Get the directory where the script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to the 'datapack.zip' file
            datapack_path = os.path.join(script_dir, "templates", "datapack.zip")

            with open(datapack_path, "rb") as fp:
                await inter.response.send_message(
                    "📁 Here is a basic datapack template for 1.20.1:",
                    file=disnake.File(fp, "Datapack Template UNZIP PLEASE.zip"),
                )

        if template == "resourcepack":
            # Get the directory where the script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to the 'datapack.zip' file
            resourcepack_path = os.path.join(
                script_dir, "templates", "resourcepack.zip"
            )

            with open(resourcepack_path, "rb") as fp:
                await inter.response.send_message(
                    "📁 Here is a basic resourcepack template for 1.20.1:",
                    file=disnake.File(fp, "Resourcepack Template UNZIP PLEASE.zip"),
                )

        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/template` Command**"),
            description=(
                str(inter.user.name)
                + " got themselves a `"
                + str(template)
                + "` template (Server: **" + inter.guild.name + "**)"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
