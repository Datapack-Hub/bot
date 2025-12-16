from difflib import get_close_matches

import aiohttp
import discord

from command_data.vanilla import VANILLA_FILES
from components.views import VanillaFileView


async def path_autocomplete(
    ctx: discord.AutocompleteContext,
):
    # Find matches
    matches = get_close_matches(ctx.value.lower(), VANILLA_FILES, n=25, cutoff=0.1)

    if len(matches) == 0:
        return ['Try searching for a vanilla file, for example "recipe oak_stairs"']

    return matches


class VanillaCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="vanilla",
        description="View any vanilla Minecraft data file.",
    )
    async def vanilla(
        self,
        inter: discord.ApplicationContext,
        path: discord.Option = discord.Option(autocomplete=path_autocomplete),
    ):
        await inter.defer()

        match = str(path)

        if path not in VANILLA_FILES:
            matches = get_close_matches(str(path), VANILLA_FILES, n=25, cutoff=0.1)
            match = matches[0]

            if not match:
                return await inter.respond("Could not find the file.")

        # Get file
        async with (
            aiohttp.ClientSession() as session,
            session.get(f"https://raw.githubusercontent.com/misode/mcmeta/data/{match}") as req,
        ):
            if req.status == 200:
                content = await req.text()
                await inter.respond(view=VanillaFileView(match, content))
            else:
                await inter.respond("Could not fetch the file.")
