import disnake
from disnake.ext import commands
import variables
import asyncio

class on_thread_create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_create(self,thread):
        await asyncio.sleep(1)
        if (thread.parent_id == variables.datapack_help_channel) or (thread.parent_id == variables.resourcepack_help_channel):
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Someone will come and help soon!**"),
                description=(
                    "💬 While you wait, take this time to provide more context and details. What are you trying to achieve overall - maybe there's an easier way to solve this problem\n\n🙇 If it's been 30 minutes and you're still waiting for someone to help, hit the __Summon Helpers__ button to call the official helpers here\n\n✅ Once your question has been resolved (or you no longer need it), hit the __Resolve Question__ button or run /resolve"
                ),
            )
            summon_helpers_button = disnake.ui.Button(
                label="Summon Helpers",
                custom_id="summon_helpers_button",
                style=disnake.ButtonStyle.blurple,
                emoji="🙇",
            )
            resolve_question_button = disnake.ui.Button(
                label="Resolve Question",
                custom_id="resolve_question_button",
                style=disnake.ButtonStyle.green,
                emoji="✅",
            )

            await thread.send(
                embed=embed, components=[summon_helpers_button, resolve_question_button]
            )