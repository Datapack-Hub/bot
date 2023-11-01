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
        match type:
            case "resourcepack":
                request = requests.get(
                    "https://minecraft.wiki/w/Pack_format", timeout=5000
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

                    if (
                        value.find_previous("h2").find_next("caption").text
                        == "Data pack formats "
                    ):
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

                lines = description.split("\n")

                output_string = "\n".join(lines[1:])

                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title="📦 Resourcepack Pack Format History",
                    description=output_string,
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
                request = requests.get(
                    "https://minecraft.wiki/w/Pack_format", timeout=5000
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
                    if (
                        value.find_previous("h2").find_next("caption").text
                        == "Resource pack formats "
                    ):
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
                print(description)
                lines = description.split("\n")
                output_string = "\n".join(lines[1:])
                embed = disnake.Embed(
                    color=disnake.Color.orange(),
                    title="📦 Datapack Pack Format History",
                    description=output_string,
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
