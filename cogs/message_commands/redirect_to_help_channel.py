import disnake
from disnake.ext import commands
import variables


class RedirectToHelpChannel(commands.Cog, name="help_redir"):
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Redirect to Help Channel")
    async def claim(self, inter: disnake.MessageCommandInteraction):
        redi_ban_role = self.bot.get_guild(variables.main_guild).get_role(
            1031577795748450346
        )
        if inter.guild.id != variables.main_guild:
            await inter.response.send_message(
                "You can only use this in the [Datapack Hub discord server](<https://dsc.gg/datapack>)!",
                ephemeral=True,
            )
            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Redirect to Help Channel**"),
                description=(
                    str(inter.user.name) + " tried using this in a different server lol"
                ),
            )
            channel = self.bot.get_channel(variables.logs)
            await channel.send(embed=embed)
            return
        if redi_ban_role in inter.author.roles:
            await inter.response.send_message(
                "You are blacklisted from doing this. If you believe this is a mistake please contact a staff member.",
                ephemeral=True,
            )

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Redirect to Help Channel**"),
                description=(
                    str(inter.user.name)
                    + "> tried redirecting a message by <@"
                    + str(inter.target.author.id)
                    + "> \nMessage Link: <#"
                    + str(inter.channel.id)
                    + ">"
                ),
            )
            channel = self.bot.get_channel(variables.logs)
            await channel.send(embed=embed)
            return

        embed = disnake.Embed(
            color=disnake.Color.orange(),
            title="This question would be more fitting inside of a Help Channel!",
            description="It seems like someone here found your question to be more fitting in our help channels! \nHelp channels are the perfect place to ask questions and to be answered by anyone including our experienced helpers!\nVisit <#"
            + str(variables.datapack_help_channel)
            + "> or <#"
            + str(variables.resourcepack_help_channel)
            + "> if you require assistance.\nCheck out <#935570290317086841> for tips on asking questions efficiently.",
        )

        embed.set_footer(
            text=("Requested by " + inter.author.name),
            icon_url=inter.author.display_avatar,
        )

        embed.set_footer(
            text="If you feel this function was misused, please contact staff."
        )
        await inter.target.reply(embed=embed)

        # Logging
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**Redirect to Help Channel**"),
            description=(
                str(inter.user.name)
                + " redirected a message by "
                + str(inter.user.name)
                + "! \nMessage Link: <#"
                + str(inter.channel.id)
                + ">"
            ),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)
