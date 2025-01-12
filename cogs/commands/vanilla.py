import disnake
from disnake.ext import commands
from command_data.vanilla import VANILLA_FILES
from difflib import get_close_matches
import requests

class VanillaCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="vanilla",
        description="View any vanilla Minecraft data file.",
    )
    async def vanilla(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        path: str
    ):
        await inter.response.defer()
        
        if path not in VANILLA_FILES:
            matches = get_close_matches(path, VANILLA_FILES, n=25, cutoff=0.1)
            path = matches[0]
            
            if not path:
                return await inter.edit_original_message("Could not find the file.")
        
        # Get file
        req = requests.get("https://raw.githubusercontent.com/misode/mcmeta/data/" + path)
        
        if req.ok:
            content = req.text
            if len(f"```json\n{content}```") > 3000: 
                embed = disnake.Embed(
                    title=path,
                    description=f"This file is too big to show in discord! However, you can download it [here](https://raw.githubusercontent.com/misode/mcmeta/data/{path}).",
                    color=disnake.Colour.orange()
                )
                return await inter.edit_original_message(embed=embed)
            embed = disnake.Embed(
                title=path,
                description=f"```json\n{content}```",
                color=disnake.Colour.orange()
            )
            await inter.edit_original_message(embed=embed)
        else:
            await inter.edit_original_message("An error occurred while fetching the file.")
            
        
    @vanilla.autocomplete("path")
    async def path_autocomplete(
        self, 
        inter: disnake.ApplicationCommandInteraction,
        search: str
    ):
        # Find matches
        matches = get_close_matches(search, VANILLA_FILES, n=25, cutoff=0.1)
        
        if len(matches) == 0: 
            return ["Try searching for a vanilla file, for example \"recipe oak_stairs\""]
        
        return matches