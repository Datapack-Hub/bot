import discord
from command_data.dpwiki import PAGES, GUIDES
from components.views import WikiPage

async def page_autocomplete(
    ctx: discord.AutocompleteContext
):
    matches = [v["title"] for v in PAGES if ctx.value.lower() in v["title"].lower()][:20]
    
    return matches

async def guide_autocomplete(
    ctx: discord.AutocompleteContext
):
    matches = [v["title"] for v in GUIDES if ctx.value.lower() in v["title"].lower()][:20]
    
    return matches

class DPWikiCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    dpwiki = discord.SlashCommandGroup(name="dpwiki", description="Quick link to pages from datapack.wiki (our wiki site)")
    
    @dpwiki.command(
        name="page",
        description="View a wiki page from datapack.wiki"
    )
    async def page(
        self,
        inter: discord.ApplicationContext,
        page: str = discord.Option(autocomplete=page_autocomplete)
    ):
        this_page = next((x for x in PAGES if x["title"].lower() == page.lower()), None)
        
        if not this_page:
            return await inter.respond("Could not find this wiki page.")
        
        return await inter.respond(view=WikiPage(this_page))
    
    @dpwiki.command(
        name="guide",
        description="View a guide from datapack.wiki"
    )
    async def guide(
        self,
        inter: discord.ApplicationContext,
        guide: str = discord.Option(autocomplete=guide_autocomplete)
    ):
        this_page = next((x for x in GUIDES if x["title"].lower() == guide.lower()), None)
        
        if not this_page:
            return await inter.respond("Could not find this guide.")
        
        return await inter.respond(view=WikiPage(this_page))