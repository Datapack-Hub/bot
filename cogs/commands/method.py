import os

import disnake
import variables
from disnake.ext import commands

methods = os.listdir("./method")

for idx, ele in enumerate(methods):
    methods[idx] = ele.replace(".md", "")

methods_enum = commands.option_enum(methods)


class MethodCommand(commands.Cog, name="method"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="method",
        description="Shows information about methods commonly used in datapacks",
    )
    async def method(
        self, inter: disnake.ApplicationCommandInteraction, method: methods_enum
    ):
        opened_file = open("./method/" + str(method) + ".md")
        file_content = opened_file.read()
        print("Method Description: " + file_content)
        opened_file.close()

        embed = disnake.Embed(
            title=("⚙️" + method.title()),
            description=file_content,
            color=disnake.Colour.orange(),
        )

        await inter.response.send_message(embed=embed)

        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/method` Command**"),
            description=(
                str(inter.user.name)
                + " gained knowledge about `"
                + method
                + "`! (Server: **"
                + inter.guild.name
                + "**)"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
