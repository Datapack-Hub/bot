import disnake
from disnake.ext import commands
import variables
import os
from random import randrange

class eliminate_command(commands.Cog, name="eliminate"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="eliminate",
        description="You did not see this. Nobody must know. Cover up your trace.",
    )
    async def eliminate(
        self, inter: disnake.ApplicationCommandInteraction, target: disnake.User
    ):
        channel = inter.channel
        target = target.id
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "eliminated.txt")
        
        with open(file_path) as file:
                        file_text = file.readlines()
                        eliminated = []

                        for line in file_text:
                            line_2 = line
                            eliminated.append(line_2.replace("\n",""))
                        
                        print(eliminated)
                        
        if str(inter.user.id) in eliminated:
            embed = disnake.Embed(
                color=disnake.Color.red(),
                title="❓ Unknown Command",
                description=("The command you've been searching for does not exist. Never existed. Never will exist.")
            )
            
            error_code = randrange(300)
            if 0 <= error_code <= 99:
              embed.set_footer(text="Error Code: 4C656176652E")  
            elif 100 <= error_code <= 199:
              embed.set_footer(text="Error Code: 466F726765742E")  
            elif 200 <= error_code <= 299:
                embed.set_footer(text="Error Code: 45726173652E")
            elif 200 <= error_code <= 300:
                embed.set_footer(text="Err♡r C♡de: 4D 69 73 73 20 79 6F 75 20 3C 33")
                
            await inter.response.send_message(embed=embed,ephemeral=True)
            
        else:
            if str(target) in eliminated:
                with open(file_path, "a") as file:
                    file.write("\n"+str(inter.user.id))
                    
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="💥 Elimination Failed",
                    description=(
                        "<@"
                        + str(target)
                        + "> already is eliminated. You have been eliminated. 4."
                    ),
                )
                
            else:
                with open(file_path, "a") as file:
                    file.write("\n"+str(target))
                    
                embed = disnake.Embed(
                        color=disnake.Color.orange(),
                        title="🧪 Elimination Successful",
                        description=(
                            "<@"
                            + str(target)
                            + "> has successfully been eliminated. Thank you for your loyality."
                        ),
                    )
                
            await inter.response.send_message(embed=embed)

