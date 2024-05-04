import os

import disnake
import variables
import dph
from disnake.ext import commands

template = commands.option_enum(["datapack", "resourcepack"])


class TemplateCommand(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="template",
        description="Provides a datapack/resourcepack template!",
    )
    async def template(
        self,
        inter: disnake.ApplicationCommandInteraction,
        template: template = "datapack",
    ):
        match template:
            case "datapack":
                # Get the directory where the script is located
                script_dir = os.path.dirname(os.path.abspath(__file__))

                # Construct the full path to the 'datapack.zip' file
                datapack_path = os.path.join(script_dir, "templates", "datapack.zip")

                with open(datapack_path, "rb") as fp:
                    await inter.response.send_message(
                        "📁 Here is a basic datapack template for 1.20.6:",
                        file=disnake.File(fp, "Datapack Template UNZIP PLEASE.zip"),
                    )

            case "resourcepack":
                # Get the directory where the script is located
                script_dir = os.path.dirname(os.path.abspath(__file__))

                # Construct the full path to the 'datapack.zip' file
                resourcepack_path = os.path.join(
                    script_dir, "templates", "resourcepack.zip"
                )

                with open(resourcepack_path, "rb") as fp:
                    await inter.response.send_message(
                        "📁 Here is a basic resourcepack template for 1.20.6:",
                        file=disnake.File(fp, "Resourcepack Template UNZIP PLEASE.zip"),
                    )

        await dph.log("`/template` Command", f"{inter.user.name} got themselves a `{template}` template (Server: **{inter.guild.name}**)","orange",self)

