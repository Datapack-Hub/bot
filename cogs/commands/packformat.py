import disnake
from disnake.ext import commands
import variables
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

class packformat_command(commands.Cog, name='packformat'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command()
    async def packformat(self,inter):
        pass


    @packformat.sub_command(description="Shows history of resourcepack pack formats")
    async def resourcepack(self,inter: disnake.ApplicationCommandInteraction):
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
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)


    @packformat.sub_command(description="Shows history of datapack pack formats")
    async def datapack(self,inter: disnake.ApplicationCommandInteraction):
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
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)