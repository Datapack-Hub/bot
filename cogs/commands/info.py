import discord
from command_data.info import INFO
from components.views import InfoView

class InfoCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="info",
        description="Quick access to FAQs including code editors, Minecraft logs, etc.",
    )
    async def info(
        self, 
        inter: discord.ApplicationContext, 
        info: str = discord.Option(choices=sorted([item["name"] for item in INFO]))
    ):
        
        # Get info
        res = next((item for item in INFO if item["name"] == info), None)
        
        # Error handling
        if not res:
            return await inter.response.send_message(f"The info `{info}` does not exist.",ephemeral=True)

        # Send message
        await inter.respond(view=InfoView(res))