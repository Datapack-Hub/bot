import disnake
from disnake.ext import commands
from command_data.links import LINKS

class LinkCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="link",
        description="Links to datapack-related discord servers, tools, bots, and more.",
    )
    async def link(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        link: str = commands.Param(choices=sorted([item["name"] for item in LINKS]))
    ):
        await inter.response.defer()
        
        # Get link
        res = next((item for item in LINKS if item["name"] == link), None)
        
        # Error handling
        if not res:
            return await inter.response.send_message(f"The invite `{link}` does not exist.",ephemeral=True)

        # Output embed
        embed = disnake.Embed(
            color=disnake.Colour.orange(), 
            title=res["name"]
        )
        embed.add_field("About",res["about"],inline=False)
        embed.add_field("Link",res["link"],inline=False)

        # Send message
        await inter.edit_original_message(embed=embed)