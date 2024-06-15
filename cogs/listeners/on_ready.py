import logging
import dph
from disnake.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await dph.log("**Bot Started**","","green",self)
        logging.basicConfig()
        logging.info("Bot started!")

