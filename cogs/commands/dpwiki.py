import discord

from command_data.dpwiki import GUIDES, WIKI_PAGES, generate_dpwiki_data
from components.views import WikiPage


async def page_autocomplete(ctx: discord.AutocompleteContext):
    await generate_dpwiki_data()
    matches = [v["title"] for v in WIKI_PAGES if ctx.value.lower() in v["title"].lower()][:20]

    return matches


async def guide_autocomplete(ctx: discord.AutocompleteContext):
    await generate_dpwiki_data()
    matches = [v["title"] for v in GUIDES if ctx.value.lower() in v["title"].lower()][:20]

    return matches


class DPWikiCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    dpwiki = discord.SlashCommandGroup(
        name="dpwiki",
        description="Quick link to pages from datapack.wiki (our wiki site)",
    )

    @dpwiki.command(name="page", description="View a wiki page from datapack.wiki")
    async def page(
        self,
        inter: discord.ApplicationContext,
        page: discord.Option = discord.Option(autocomplete=page_autocomplete),
    ):
        this_page = next((x for x in WIKI_PAGES if x["title"].lower() == str(page).lower()), None)

        if not this_page:
            return await inter.respond("Could not find this wiki page.")

        return await inter.respond(view=WikiPage(this_page))

    @dpwiki.command(name="guide", description="View a guide from datapack.wiki")
    async def guide(
        self,
        inter: discord.ApplicationContext,
        guide: discord.Option = discord.Option(autocomplete=guide_autocomplete),
    ):
        this_page = next((x for x in GUIDES if x["title"].lower() == str(guide).lower()), None)

        if not this_page:
            return await inter.respond("Could not find this guide.")

        return await inter.respond(view=WikiPage(this_page))
