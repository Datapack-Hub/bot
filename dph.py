import disnake
import variables

async def log(header, description,color,self):
    
    channel = self.bot.get_channel(variables.logs_channel)
    
    header.lower().title()
    
    if color == "purple":
        color = disnake.Colour.purple()
    elif color == "red":
        color = disnake.Colour.red()
    elif color == "green":
        color = disnake.Colour.green()
    elif color == "orange":
        color = disnake.Colour.orange()
              
    embed = disnake.Embed(
        title=header,
        description=(
            description
        ),
        color=color
    )
    
    await channel.send(embed=embed)

def convert_username(name):
    
    name.replace("*","\*").replace("_","\_").replace("~~","\~~")
    return name