import disnake
from disnake.ext import commands



class HighlighterCommand(commands.Cog, name="highlighter"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(
        title="Highlighter",
        description="Allows you to toggle the serverwide mcfunction syntax highlighter",
    )
    async def highlighter(self,inter: disnake.ApplicationCommandInteraction,):
                embed = disnake.Embed(
                    title="`mcfunction` Highlighter (CURRENTLY DISABLED GLOBALLY)",
                    description="The **`mcfunction` Highlighter** adds syntax highlighting to all **mcfunction code in codeblocks**. This is achvieved by **deleting** the message originally sent and **replacing it using a webhook** (with the original senders name and profile picture).It **does not apply retroactively** to already sent messages.\nExample:\n```mcfunction\nexecute as @a if predicate namespace:predicate run function namespace:function```\n->\n```ansi\n[35mexecute [34mas [36m@a [34mif predicate [33mnamespace:predicate [34mrun [35mfunction [33mnamespace:function```\n_([Source Code by bth123](https://github.com/bth123/mcf-ansi-highlighter))_",
                    color= disnake.Color.red()
                )
                
                await inter.response.send_message(embed=embed,ephemeral=True)
                
