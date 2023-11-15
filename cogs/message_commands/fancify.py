import disnake
from disnake.ext import commands
import variables
import re

class FancifyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Fancify ✨")
    async def fancify(self, inter: disnake.MessageCommandInteraction,message):
        match = re.search(r'\`\`\`([\s\S]*?)\`\`\`|\`([\s\S]*?)\`',message.content)
        if not message.embeds:
            if match:
                embed = disnake.Embed(
                    title=":sparkles:",
                    description="```hs\n" + match.group(0).strip().replace("`","") + "\n```",
                    color=disnake.Colour.purple()
                ).set_footer(text="Since discord doesn't allow for the direct highlighting of mcfunction, this uses haskell to highlight text and might thus not be perfect\nRequested by " + inter.author.display_name,icon_url=inter.author.display_avatar.url)

                
            else:
                embed = disnake.Embed(
                    title=":sparkles:",
                    description="```hs\n" + message.content + "\n```",
                    color=disnake.Colour.purple()
                ).set_footer(text="Since discord doesn't allow for the direct highlighting of mcfunction, this uses haskell to highlight text and might thus not be perfect\nRequested by " + inter.author.display_name,icon_url=inter.author.display_avatar.url)      
                
            await inter.target.reply(embed=embed)
            await inter.response.send_message("Fancification successful :sparkles:", ephemeral=True)

        else:
            await inter.response.send_message("You can't fancify embeds!", ephemeral=True)
                
            