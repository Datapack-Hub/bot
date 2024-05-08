import disnake
import variables
import re

from cogs.listeners.highlighter.highlighter import Hl

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

def get_highlighter_server_list():
    server_ids = []
    with open(file=f"{variables.full_path}/highlighter_servers.txt") as file:
        for line in file:
            server_ids.append(line.replace("\n",""))
    return server_ids