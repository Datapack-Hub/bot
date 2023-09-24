import disnake
from disnake.ext import commands
import os

commands_2 = os.listdir("./command_syntax")

for idx, ele in enumerate(commands_2):
    commands_2[idx] = ele.replace(".txt", "")

commands_enum = commands.option_enum(commands_2)


class SyntaxCommand(commands.Cog, name="syntax"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="syntax",
        description="",
    )
    async def syntax(
        self, inter: disnake.ApplicationCommandInteraction, command: str
    ):
        opened_file = open("./command_syntax/" + str(command) + ".txt")
        file_content = opened_file.read()
        print("Method Description: " + file_content)
        opened_file.close()
        embed = disnake.Embed(
            title=command,
            description=file_content,
            color=disnake.Colour.orange(),
        )

        await inter.response.send_message(embed=embed)
