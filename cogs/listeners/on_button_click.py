import disnake
import variables
import dph
from disnake.ext import commands
import json

class OnButtonClick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        
        if inter.component.custom_id == "dph_highlighter_on":
            button = disnake.ui.Button(
                style = disnake.ButtonStyle.red,
                custom_id = "dph_highlighter_off",
                label = "Disable"
            )
        
            embed = disnake.Embed(
                title="`mcfunction` Highlighter (ENABLED)",
                description="The **`mcfunction` Highlighter** adds syntax highlighting to all **mcfunction code in codeblocks**. This is achvieved by **deleting** the message originally sent and **replacing it using a webhook** (with the original senders name and profile picture). \nYou always can **re-enable** this option at any time after disabling it!\n**Does not apply retroactively to already sent messages**",
                color= disnake.Color.blue()
            )
            
            with open(file=f"{variables.full_path}/highlighter_servers.txt", mode="a") as file:
                file.write(f"\n{inter.guild.id}")
            
            await inter.response.edit_message(embed=embed,components=button)

        elif inter.component.custom_id == "dph_highlighter_off":
            button = disnake.ui.Button(
                style = disnake.ButtonStyle.green,
                custom_id = "dph_highlighter_on",
                label = "Enable"
            )
        
            embed = disnake.Embed(
                title="`mcfunction` Highlighter (DISABLED)",
                description="The **`mcfunction` Highlighter** adds syntax highlighting to all **mcfunction code in codeblocks**. This is achvieved by **deleting** the message originally sent and **replacing it using a webhook** (with the original senders name and profile picture). \nYou can always **disable** this option at any time after enabling it!\n**Does not apply retroactively to already sent messages**",
                color= disnake.Color.blue()
            )
                    
            with open(file=f"{variables.full_path}/highlighter_servers.txt", mode="r") as file:
                lines = file.readlines()
                
            with open(f"{variables.full_path}/highlighter_servers.txt", "w") as file:
                for line in lines:
                    if not str(inter.guild.id) in line:
                        file.write(line)
                
            await inter.response.edit_message(embed=embed,components=button)
            
        else:
            print(inter.component.custom_id)