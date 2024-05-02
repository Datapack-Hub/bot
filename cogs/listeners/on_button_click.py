import disnake
import variables
import dph
from disnake.ext import commands


class OnButtonClick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        print("how does one press a button when the button does not exist")
