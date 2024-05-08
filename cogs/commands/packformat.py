import disnake
import requests
import variables
import dph
from bs4 import BeautifulSoup
from disnake.ext import commands
from markdownify import markdownify as md
import json

type_enum = commands.option_enum(["resourcepack", "datapack"])


class PackFormatCommand(commands.Cog, name="packformat"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="packformat",
        description="Shows the packformat history of datapacks/resourcepacks",
    )
    async def packformat(
        self, inter: disnake.ApplicationCommandInteraction, version: str = "default"
    ):
        
        request = requests.get("https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.json",timeout=5000,
            headers={"User-Agent": "Datapack Helper Discord Bot"},)


        request = BeautifulSoup(request.content, "html.parser")
        description = ""
        print("geasdsd")

        
        if version.lower() == "snapshots":
            version = "snapshot"
        if version.lower() == "releases":
            version = "release"
        
        if "w" in version.lower() and not ("a" in version.lower() or "b" in version.lower() or "c" in version.lower()):
            version += "a"
        
        request = requests.get("https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.json",timeout=5000,headers={"User-Agent": "Datapack Helper Discord Bot"})
        request = BeautifulSoup(request.content, "html.parser")
        
        json_data = json.loads(request.text)
        
        versions_array = []
        output_array = []
        output = ""
        i = 0
        
        if version == "default":
            output_array.append(f"**Latest Releases:**\n")
            for entry in json_data:
                if i < 3 and (entry['type'] == "release"):
                    versions_array.append(f"**{entry['id']}**: \nDatapacks: `{entry['data_pack_version']}`    Resourcepacks: `{entry['resource_pack_version']}`\n")  
                    i += 1
                if i >= 3:
                    versions_array.reverse()
                    output_array += versions_array
                    break
            output_array.append(f"\n**Latest Snapshot:**\n")       
            for entry in json_data:
                if entry['type'] == "snapshot":
                    output_array.append(f"**{entry['id']}**: \nDatapacks: `{entry['data_pack_version']}`    Resourcepacks: `{entry['resource_pack_version']}`\n")  
                    break
            output_array.append("\n_Only showing recent formats. To view specific versions use `/packformat version:<id>`_")
        else:
            for entry in json_data:
                if entry['type'] == version:
                    output_array.append(f"**{entry['id']}**: \nDatapacks: `{entry['data_pack_version']}`    Resourcepacks: `{entry['resource_pack_version']}`\n")
                elif entry['id'] == version:
                    output_array.append(f"**{entry['id']}**: \nDatapacks: `{entry['data_pack_version']}`    Resourcepacks: `{entry['resource_pack_version']}`")
            output_array.reverse()
            if len(output_array) > 10:
                output_array = output_array[(len(output_array)-10):]
                output_array.append("\n_Only showing the 10 most recent formats. To view specific versions use `/packformat version:<id>`_")
        
        
        for item in output_array:
            output += item
        
        if version == "snapshot":
            version = "Snapshots"
            
        if version == "release":
            version = "Releases"
        
        if version == "default":
            version = "Latest"
            
        if output != "":
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=(f"Pack Format ({version})"),
                description=output,
            )
            await inter.response.send_message(embed=embed)
        else: 
            embed = disnake.Embed(
                color=disnake.Colour.red(),
                title=(f"❌ Version does not exist"),
                description=f"Failed to find pack format for version `{version}`",
            )
            await inter.response.send_message(embed=embed,ephemeral=True)
            
        await dph.log("`/packformat` Command", f"{inter.user.name} looked up the pack format for `{version}` (Server: **{inter.guild.name}**)","orange",self)