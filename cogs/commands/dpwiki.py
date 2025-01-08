import disnake
from disnake.ext import commands
from command_data.dpwiki import PAGES, GUIDES

class DPWikiCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="dpwiki"
    )
    async def dpwiki(
        self, 
        inter: disnake.ApplicationCommandInteraction
    ):
        pass
    
    @dpwiki.sub_command(
        name="page",
        description="VIew a wiki page from datapack.wiki"
    )
    async def page(
        self,
        inter: disnake.ApplicationCommandInteraction,
        page: str
    ):
        # Defer response
        await inter.response.defer()
        
        this_page = next((x for x in PAGES if x["title"].lower() == page.lower()), None)
        
        if not this_page:
            return await inter.edit_original_message("Could not find this wiki page.")
        
        embed = disnake.Embed(
            title=page,
            description="View this wiki page on datapack.wiki: " + this_page["url"],
            url=this_page["url"],
            colour=disnake.Colour.orange()
        )
        
        return await inter.edit_original_message(embed=embed)
        
    @page.autocomplete("page")
    async def version_autocomplete(
        self, 
        search: str
    ):
        matches = [v["title"] for v in PAGES if search.lower() in v["title"].lower()][:20]
        
        return matches
    
    @dpwiki.sub_command(
        name="guide",
        description="View a guide from datapack.wiki"
    )
    async def guide(
        self,
        inter: disnake.ApplicationCommandInteraction,
        guide: str
    ):
        # Defer response
        await inter.response.defer()
        
        this_page = next((x for x in GUIDES if x["title"].lower() == guide.lower()), None)
        
        if not this_page:
            return await inter.edit_original_message("Could not find this guide.")
        
        embed = disnake.Embed(
            title=guide,
            description="View this guide on datapack.wiki: " + this_page["url"],
            url=this_page["url"],
            colour=disnake.Colour.orange()
        )
        
        return await inter.edit_original_message(embed=embed)
        
    @guide.autocomplete("guide")
    async def version_autocomplete(
        self, 
        search: str
    ):
        matches = [v["title"] for v in GUIDES if search.lower() in v["title"].lower()][:20]
        
        return matches