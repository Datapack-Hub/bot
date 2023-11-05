import disnake
import requests
import variables
from bs4 import BeautifulSoup
from disnake.ext import commands
from markdownify import markdownify as md

type_enum = commands.option_enum(["resourcepack", "datapack"])


class PackFormatCommand(commands.Cog, name="packformat"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="packformat",
        description="Shows the packformat history of datapacks/resourcepacks",
    )
    async def packformat(
        self, inter: disnake.ApplicationCommandInteraction, type: type_enum = "datapack"
    ):
        request = requests.get(
            "https://minecraft.wiki/w/Pack_format",
            timeout=5000,
            headers={"User-Agent": "Datapack Helper Discord Bot"},
        )

        request = BeautifulSoup(request.content, "html.parser")

        description = ""
        match type:
            case "resourcepack":
                table_body = request.find("tbody")

                for row in table_body.find_all("tr"):
                    cells = row.find_all("td")

                    if len(cells) >= 2:
                        pack_format = cells[0].get_text(strip=True)
                        version_range = cells[1].get_text(strip=True)
                        description += (
                            f"Format: `{pack_format}` Version(s): `{version_range}`\n"
                        )

                embed = disnake.Embed(
                    color=disnake.Color.purple(),
                    title="📦 Resourcepack Pack Format History",
                    description=description.rsplit("\n", 1)[0],
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
                channel = self.bot.get_channel(variables.logs)
                await channel.send(embed=embed)

            case "datapack":
                datapack_table_body = request.find_all("table")[1]

                for row in datapack_table_body.find_all("tr"):
                    cells = row.find_all("td")

                    if len(cells) >= 2:
                        pack_format = cells[0].get_text(strip=True)
                        version_range = cells[1].get_text(strip=True)
                        description += (
                            f"Format: `{pack_format}` Version(s): `{version_range}`\n"
                        )

                embed = disnake.Embed(
                    color=disnake.Color.purple(),
                    title="📦 Datapack Pack Format History",
                    description=description.rsplit("\n", 1)[0],
                )

                await inter.response.send_message(embed=embed)
                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`/packformat` Command**"),
                    description=(
                        str(inter.user.name)
                        + " looked up the packformat history of `datapacks` (Server: **"
                        + inter.guild.name
                        + "**)"
                    ),
                )
                channel = self.bot.get_channel(variables.logs)
                await channel.send(embed=embed)
