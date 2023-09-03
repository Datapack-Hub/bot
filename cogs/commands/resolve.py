import disnake
from disnake.ext import commands
import variables


class resolve_command(commands.Cog, name="resolve"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(title="resolve", description="Marks question as resolved")
    async def resolve(self, inter: disnake.ApplicationCommandInteraction):
        role = self.bot.get_guild(variables.main_guild).get_role(variables.helper_role)

        try:
            channel = inter.channel.parent.id
            if (inter.channel.owner.id == inter.author.id) or (
                role in inter.author.roles
            ):
                if (
                    channel == variables.datapack_help_channel
                    or variables.resourcepack_help_channel
                ):
                    resolved_tag = inter.channel.parent.get_tag_by_name("RESOLVED")
                    await inter.channel.add_tags(resolved_tag)
                    embed = disnake.Embed(
                        color=disnake.Color.green(),
                        title=":white_check_mark: Closed Question",
                        description="Closed the channel and market it as resolved! \nIf you have more questions feel free to ask them in a new channel!",
                    )
                    await inter.response.send_message(embed=embed)
                    await inter.channel.edit(archived=True)
                    # Logging
                    embed = disnake.Embed(
                        color=disnake.Colour.orange(),
                        title=("**`/resolve` Command**"),
                        description=(str(inter.user.name) + " resolved a help channel"),
                    )
                    channel = self.bot.get_channel(variables.logs)
                    await channel.send(embed=embed)
                    await inter.response.send_message(embed=embed)
                elif role not in inter.author.roles:
                    embed = disnake.Embed(
                        color=disnake.Color.red(),
                        title="❌ Resolve Help Channel",
                        description="You can only do this in one of our help channels",
                    )
                    await inter.response.send_message(embed=embed, ephemeral=True)

            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="❌ Resolve Help Channel",
                    description="Only the creator of this question and helpers can mark it as resolved",
                )
                await inter.response.send_message(embed=embed, ephemeral=True)

        except:
            embed = disnake.Embed(
                color=disnake.Color.orange(),
                title="Resolve Help Channel",
                description="You can only do this in one of our help channels",
            )

            await inter.response.send_message(embed=embed, ephemeral=True)
