import disnake
from disnake.ext import commands
from command_data.packformat import VERSIONS
from difflib import get_close_matches
import requests

class PackFormatCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="packformat",
        description="View pack format history",
    )
    async def packformat(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        version: str = "Recent Versions"
    ):
        await inter.response.defer()
        
        # Get all pack formats
        pack_formats = requests.get("https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.json",headers={"User-Agent": "Datapack Helper -> https://discord.datapackhub.net/"}).json()
        
        if version == "Recent Versions":
            pack_formats = pack_formats[:5]
        else:
            pack_formats = [next((item for item in pack_formats if item["id"] == version), None)]
            
            if not pack_formats[0]:
                return await inter.edit_original_message("This version does not exist.")
        
        # Output embed
        out = ""
        for format in pack_formats:
            out += f"- **{format['id']}**: Datapack: `{format['data_pack_version']}` • Resource Pack: `{format['resource_pack_version']}`\n"
            
        embed = disnake.Embed(
            title=f"Pack Format: `{version}`",
            description=out,
            color=disnake.Colour.orange()
        )
        
        # Send message
        await inter.edit_original_message(embed=embed)
                
            
        
    @packformat.autocomplete("version")
    async def version_autocomplete(
        self, 
        search: str
    ):
        matches = ["Recent Versions"]
        matches += [v for v in VERSIONS if search.lower() in v.lower()][:20]
        
        return matches