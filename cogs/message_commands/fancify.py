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
                    description="```hs\n" + match.group(0).strip().replace("`","") + "\n```",
                    color=disnake.Colour.purple()
                )
                
            else:
                embed = disnake.Embed(
                    description="```hs\n" + message.content + "\n```",
                    color=disnake.Colour.purple()
                )  
                
            await inter.target.reply(embed=embed,allowed_mentions=None)
            await inter.response.send_message("Fancification successful :sparkles:", ephemeral=True)

        else:
            await inter.response.send_message("You can't fancify embeds!", ephemeral=True)
                
            