import disnake
from disnake.ext import commands
import variables
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

class syntax_command(commands.Cog, name='syntax'):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(title="syntax", description="Shows the correct syntax of any minecraft command")
    async def syntax(self,inter: disnake.ApplicationCommandInteraction, command: str):
        request = requests.get(
            f"https://minecraft.fandom.com/wiki/commands/{command}", timeout=5000
        )
        request = BeautifulSoup(request.content, "html.parser")
        description_v2 = (
            "This command does not exist! Make sure to check spelling before trying again."
        )
    
        if "There is currently no text in this page. You can" not in str(request.text):
            h2s = request.find_all("h2")
            if (
                "This article describes content that may be included in Bedrock Edition."
                in request.text
            ):
                bedrock_notice = " (Bedrock Only)"
            else:
                bedrock_notice = ""
            for h2 in h2s:
                if "Syntax" in h2.text:
                    if command.lower != "execute" and not "trigger":
                        dl = h2.find_next("dl")
                    elif command == "execute":
                        dl = h2.find_next("dl").find_next("dl")
                    elif command == "trigger":
                        dl = "`trigger <objective>`\n   Adds `1` to the current value of `<objective>`.\n`trigger <objective> add <value>`\n    Adds `<value>` to the current value of `<objective>`.\n?`trigger <objective> set <value>`\n Sets the value of `<objective>` to `<value>`."
    
                    if command.lower != "trigger":
                        dl = h2.find_next("dl")
                        description_v2 = md(str(dl), convert=["code", "li", "ul"]).replace(
                            "/wiki", "https://minecraft.fandom.com/wiki"
                        )
                    else:
                        description_v2 = dl
    
                    print(description_v2)
    
        embed = disnake.Embed(
            title=command.title() + " Syntax" + bedrock_notice,
            description=description_v2,
            color=disnake.Colour.orange(),
        )
    
        embed.set_footer(
            text=(
                "Information borrowed from: minecraft.fandom.com/wiki/Commands/" + command
            )
        )
    
        await inter.response.send_message(embed=embed)
    
        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/syntax` Command**"),
            description=(
                str(inter.user.name)
                + " looked up the following command: `"
                + str(command)
                + "`"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)