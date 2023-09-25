import disnake
from disnake.ext import commands
import os


methods = os.listdir("./method")

for idx, ele in enumerate(methods):
    methods[idx] = ele.replace(".txt", "")

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
        opened_file = open("./method/" + str(method) + ".txt")
        file_content = opened_file.read()
        print("Method Description: " + file_content)
        opened_file.close()

        embed = disnake.Embed(
            title=("⚙️"+method.title()),
            description=file_content,
            color=disnake.Colour.orange(),
        )

        await inter.response.send_message(embed=embed)
