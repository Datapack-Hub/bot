import aiohttp
import disnake
from disnake.ext import commands


class VanillaCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Returns any vanilla datapack file",)
    async def vanilla(self, inter: disnake.ApplicationCommandInteraction, path: str = commands.Param(description="The path to any vanilla data file.")):
        async with aiohttp.ClientSession() as cs:
            req = await cs.get("https://raw.githubusercontent.com/misode/mcmeta/data/data/minecraft/" + path)
            text = await req.text()
        
        embed = disnake.Embed(
            title="PREVIEW: " + path,
            description=f"```json\n{text}```Click the button below to let others view this file.",
            color=disnake.Colour.orange()
        )
        
        await inter.response.send_message(embed=embed, ephemeral=True, view=ConfirmView(path, text))
    
class ConfirmView(disnake.ui.View):
    def __init__(self, path: str, text: str):
        super().__init__(timeout=10.0)
        self.path = path
        self.text = text

    @disnake.ui.button(label="Post to channel", style=disnake.ButtonStyle.green)
    async def post(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        embed = disnake.Embed(
            title=self.path,
            description=f"```json\n{self.text}```",
            color=disnake.Colour.orange()
        )
        await inter.response.send_message(embed=embed)
        self.stop()