from io import BytesIO
from pathlib import Path

import disnake
from aiofiles import open
from disnake.ext import commands

import dph

Template = commands.option_enum(["datapack", "resourcepack"])


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
        template: Template = "datapack",
    ):
        match template:
            case "datapack":
                # Get the directory where the script is located
                script_dir = Path(__file__).resolve().parent

                # Construct the full path to the 'datapack.zip' file
                datapack_path = script_dir / "templates" / "datapack.zip"

                async with open(datapack_path, "rb") as fp:
                    content = BytesIO(await fp.read())
                    await inter.response.send_message(
                        "📁 Here is a basic datapack template for 1.20.6:",
                        file=disnake.File(content, "Datapack Template UNZIP PLEASE.zip"),
                    )

            case "resourcepack":
                # Get the directory where the script is located
                script_dir = Path(__file__).resolve().parent

                # Construct the full path to the 'datapack.zip' file
                resourcepack_path = script_dir / "templates" / "resourcepack.zip"

                async with open(resourcepack_path, "rb") as fp:
                    content = BytesIO(await fp.read())
                    await inter.response.send_message(
                        "📁 Here is a basic resourcepack template for 1.20.6:",
                        file=disnake.File(content, "Resourcepack Template UNZIP PLEASE.zip"),
                    )

        await dph.log("`/template` Command", f"A user got themselves a `{template}` template","orange",self)

