import discord
from command_data.packformat import VERSIONS
from components.views import PackFormatView

async def version_autocomplete(
    ctx: discord.AutocompleteContext
):
    matches = ["Recent Versions", "Recent Snapshots"]
    matches += [v["id"] for v in VERSIONS if ctx.value.lower() in v["id"].lower()][:20]
    
    return matches

class PackFormatCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="packformat",
        description="View pack format history",
    )
    async def packformat(
        self, 
        inter: discord.ApplicationContext, 
        version: str = discord.Option(default="Recent Versions",autocomplete=version_autocomplete)
    ):
        # Get all pack formats
        if version == "Recent Versions":
            pack_formats = [v for v in VERSIONS if v["type"] == "release"][:10]
        elif version == "Recent Snapshots":
            pack_formats = [v for v in VERSIONS if v["type"] != "release"][:10]
        else:
            pack_formats = [next((item for item in VERSIONS if item["id"] == version), None)]
            
            if not pack_formats[0]:
                return await inter.respond("This version does not exist.")
        
        # Output
        out = ""
        if len(pack_formats) == 1:
            format = pack_formats[0]
            
            dpv = str(format["data_pack_version"]["major"])
            if format["data_pack_version"]["minor"] != 0:
                dpv += "." + str(format["data_pack_version"]["minor"])
            
            rpv = str(format["resource_pack_version"]["major"])
            if format["resource_pack_version"]["minor"] != 0:
                rpv += "." + str(format["resource_pack_version"]["minor"])
            
            out = f"**Datapack:** `{dpv}`\n**Resource Pack:** `{rpv}`"
        else:
            for format in pack_formats:
                dpv = str(format["data_pack_version"]["major"])
                if format["data_pack_version"]["minor"] != 0:
                    dpv += "." + str(format["data_pack_version"]["minor"])
                
                rpv = str(format["resource_pack_version"]["major"])
                if format["resource_pack_version"]["minor"] != 0:
                    rpv += "." + str(format["resource_pack_version"]["minor"])
                    
                out += f"- **{format['id']}**: Datapack: `{dpv}` • Resource Pack: `{rpv}`\n"
        
        # Send message
        await inter.respond(view=PackFormatView(version, out))
