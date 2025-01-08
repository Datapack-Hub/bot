import disnake
from disnake.ext import commands
from command_data.folderstructures import DATAPACK, RESOURCEPACK

class FolderStructureCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="folderstructure",
        description="View the structure of a datapack or resourcepack",
    )
    async def folderstructure(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        type: str = commands.Param(choices=["Datapack","Resource Pack"],default="Datapack")
    ):
        await inter.response.defer()
        
        if type == "Datapack":
            await inter.edit_original_message(
                content=f"```py{DATAPACK}```"
            )
        else:
            await inter.edit_original_message(
                content=f"```py{RESOURCEPACK}```"
            )