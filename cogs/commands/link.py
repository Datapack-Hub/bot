import discord
from command_data.links import LINKS
from components.views import LinkView

class LinkCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="link",
        description="Links to datapack-related discord servers, tools, bots, and more.",
    )
    async def link(
        self, 
        inter: discord.ApplicationContext, 
        link: str = discord.Option(choices=sorted([item["name"] for item in LINKS]))
    ):
        
        # Get link
        res = next((item for item in LINKS if item["name"] == link), None)
        
        # Error handling
        if not res:
            return await inter.response.send_message(f"The invite `{link}` does not exist.",ephemeral=True)

        # Send message
        await inter.respond(view=LinkView(res))