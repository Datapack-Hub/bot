from io import BytesIO
import discord
import variables
from pathlib import Path
from command_data.templates import DATAPACKS, RESOURCEPACKS

class TemplateCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="template",
        description="Download a pre-made template for datapacks and resource packs",
    )
    async def template(
        self, 
        inter: discord.ApplicationContext, 
        type: str = discord.Option(choices=["Datapack", "Resource Pack"])
    ):
        await inter.defer()
        
        if type == "Datapack":
            # Pick default template
            default = DATAPACKS[0]
            
            template_path = Path(variables.__file__).resolve().parent / "static" / "templates" / default["file"]
            
            await inter.respond(
                content=f"**{type}** template for latest version `{default['versions']}`",
                file=discord.File(template_path, f"DP: {default['versions']}.zip"),
                view=DropDownView(DATAPACKS)
            )
        else:
            # Pick default template
            default = RESOURCEPACKS[0]
            
            template_path = Path(variables.__file__).resolve().parent / "static" / "templates" / default["file"]
            
            await inter.respond(
                content=f"**{type}** template for latest version `{default['versions']}`.",
                file=discord.File(template_path, f"Template: {default['versions']}.zip"),
                view=DropDownView(RESOURCEPACKS)
            )

class VersionDropdown(discord.ui.Select):
    def __init__(self, data):
        self.data = data

        super().__init__(
            placeholder="Select a different Minecraft version",
            options=[discord.SelectOption(label=item["versions"], emoji="📂") for item in data]
        )

    async def callback(self, inter: discord.MessageInteraction):
        selected = [i for i in self.data if i["versions"] == self.values[0]][0]
        
        template_path = Path(variables.__file__).resolve().parent / "static" / "templates" / selected["file"]
            
        await inter.response.edit_message(
            content=f"Template for latest version `{selected['versions']}`.",
            attachments=[],
            files=[discord.File(template_path, f"Template: {selected['versions']}.zip")]
        )
        
class DropDownView(discord.ui.View):
    def __init__(self, data: list):
        super().__init__()

        self.add_item(VersionDropdown(data))