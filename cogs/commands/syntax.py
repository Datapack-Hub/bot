import os

import disnake
import dph
from disnake.ext import commands

commands_2 = os.listdir("./command_syntax")

for idx, ele in enumerate(commands_2):
    commands_2[idx] = ele.replace(".md", "")

commands_enum = commands.option_enum(commands_2)


class SyntaxCommand(commands.Cog, name="syntax"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="syntax",
        description="Outputs syntax of any minecraft command",
    )
    async def syntax(self, inter: disnake.ApplicationCommandInteraction, command: str):
        try:
            opened_file = open("./command_syntax/" + str(command) + ".md")
            file_content = opened_file.read()
            opened_file.close()
            embed = disnake.Embed(
                title=("📜 /" + (str(command.replace("/","")))),
                description=file_content,
                color=disnake.Colour.orange(),
            )
        except FileNotFoundError:
            embed = disnake.Embed(
                title="❌ Command Not Found",
                description="Make sure to check for typos and keep in mind that the bot does not include bedrock commands :>",
                color=disnake.Colour.red(),
            )

        await inter.response.send_message(embed=embed)
        await dph.log("`/syntax` Command", f"A user looked up the syntax of `{command}`","orange",self)