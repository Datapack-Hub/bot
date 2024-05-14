import os

import disnake
import variables
import dph
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
        opened_file.close()

        text = f"""# {method.title()}
        >>> {file_content}"""

        await inter.response.send_message(text)

        await dph.log("`/method` Command", f"A user looked up the `{method}` method","orange",self)
