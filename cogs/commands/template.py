from io import BytesIO
import disnake
from disnake.ext import commands
import variables
from pathlib import Path
from command_data.templates import DATAPACKS, RESOURCEPACKS

class TemplateCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="template",
        description="View datapack or resource pack templates",
    )
    async def template(
        self, 
        inter: disnake.ApplicationCommandInteraction, 
        type: str = commands.Param(choices=["Datapack", "Resource Pack"])
    ):
        await inter.response.defer()
        
        if type == "Datapack":
            # Pick default template
            default = DATAPACKS[0]
            
            template_path = Path(variables.__file__).resolve().parent / "static" / "templates" / default["file"]
            
            await inter.edit_original_message(
                content=f"**{type}** template for latest version `{default['versions']}`",
                file=disnake.File(template_path, f"DP: {default['versions']}.zip"),
                view=DropDownView(DATAPACKS)
            )
        else:
            # Pick default template
            default = RESOURCEPACKS[0]
            
            template_path = Path(variables.__file__).resolve().parent / "static" / "templates" / default["file"]
            
            await inter.edit_original_message(
                content=f"**{type}** template for latest version `{default['versions']}`.",
                file=disnake.File(template_path, f"Template: {default['versions']}.zip"),
                view=DropDownView(RESOURCEPACKS)
            )

class VersionDropdown(disnake.ui.StringSelect):
    def __init__(self, data):
        self.data = data

        super().__init__(
            placeholder="Select a different Minecraft version",
            options=[disnake.SelectOption(label=item["versions"], emoji="📂") for item in data]
        )

    async def callback(self, inter: disnake.MessageInteraction):
        selected = [i for i in self.data if i["versions"] == self.values[0]][0]
        
        template_path = Path(variables.__file__).resolve().parent / "static" / "templates" / selected["file"]
            
        await inter.response.edit_message(
            content=f"Template for latest version `{selected['versions']}`.",
            attachments=[],
            files=[disnake.File(template_path, f"Template: {selected['versions']}.zip")]
        )
        
class DropDownView(disnake.ui.View):
    def __init__(self, data: list):
        super().__init__()

        self.add_item(VersionDropdown(data))