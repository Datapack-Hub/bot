import disnake
from disnake.ext import commands
from command_data.info import INFO

class InfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="info",
        description="Quick access to FAQs including code editors, Minecraft logs, etc.",
    )
    async def info(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        info: str = commands.Param(choices=sorted([item["name"] for item in INFO]))
    ):
        await inter.response.defer()
        
        # Get info
        res = next((item for item in INFO if item["name"] == info), None)
        
        # Error handling
        if not res:
            return await inter.response.send_message(f"The info `{info}` does not exist.",ephemeral=True)

        # Output embed
        embed = disnake.Embed(
            color=disnake.Colour.orange(), 
            title=res["name"],
            description=res["content"]
        )
        
        if res["image"] is not None: embed.set_image(res["image"])

        # Send message
        await inter.edit_original_message(embed=embed)