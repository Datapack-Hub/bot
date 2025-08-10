import discord
from command_data.folderstructures import DATAPACK, RESOURCEPACK

class FolderStructureCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="folderstructure",
        description="View the structure of a datapack or resourcepack",
    )
    async def folderstructure(
        self, 
        inter: discord.ApplicationContext, 
        type: str = discord.Option(choices=["Datapack","Resource Pack"],default="Datapack")
    ):
        await inter.defer()
        
        if type == "Datapack":
            await inter.respond(
                content=f"```py{DATAPACK}```"
            )
        else:
            await inter.respond(
                content=f"```py{RESOURCEPACK}```"
            )