import discord
from command_data.vanilla import VANILLA_FILES
from difflib import get_close_matches
import requests
from components.views import VanillaFileView
            
async def path_autocomplete(
    ctx: discord.AutocompleteContext,
):
    # Find matches
    matches = get_close_matches(ctx.value.lower(), VANILLA_FILES, n=25, cutoff=0.1)
    
    if len(matches) == 0: 
        return ["Try searching for a vanilla file, for example \"recipe oak_stairs\""]
    
    return matches

class VanillaCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="vanilla",
        description="View any vanilla Minecraft data file.",
    )
    async def vanilla(
        self, 
        inter: discord.ApplicationContext, 
        path: str = discord.Option(autocomplete=path_autocomplete) 
    ):
        await inter.defer()
        
        if path not in VANILLA_FILES:
            matches = get_close_matches(path, VANILLA_FILES, n=25, cutoff=0.1)
            path = matches[0]
            
            if not path:
                return await inter.respond("Could not find the file.")
        
        # Get file
        req = requests.get("https://raw.githubusercontent.com/misode/mcmeta/data/" + path)
        
        if req.ok:
            content = req.text
            
            await inter.respond(view=VanillaFileView(path, content))
        else:
            await inter.respond("An error occurred while fetching the file.")