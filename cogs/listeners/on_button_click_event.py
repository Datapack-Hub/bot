import disnake
from disnake.ext import commands
import variables
import datetime


class OnButtonClick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        print("asdasd")
        if inter.component.custom_id == "resolve_question_button":
            role = self.bot.get_guild(variables.main_guild).get_role(
                variables.helper_role
            )
            if (inter.channel.owner.id == inter.user.id) or (role in inter.user.roles):
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
                    title=("**`Resolve Help Channel` Button**"),
                    description=(str(inter.user.name) + " resolved a help channel"),
                )
                channel = self.bot.get_channel(variables.logs)
                await channel.send(embed=embed)

            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="❌ Resolve Help Channel",
                    description="You can't do this since you are neither a helper nor the owner of this channel!",
                )
                await inter.response.send_message(embed=embed, ephemeral=True)
                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`Resolve Help Channel` Button**"),
                    description=(
                        str(inter.user.name) + " failed resolving a help channel"
                    ),
                )
                channel = self.bot.get_channel(variables.logs)
                await channel.send(embed=embed)

        if inter.component.custom_id == "summon_helpers_button":
            creation_time = inter.channel.create_timestamp
            current_time = datetime.datetime.now(creation_time.tzinfo)
            time_difference = current_time - creation_time

            time_difference_seconds = time_difference.total_seconds()
            time_difference_minutes = time_difference_seconds / 60

            role = self.bot.get_guild(variables.main_guild).get_role(
                variables.helper_role
            )
            channel = inter.channel.parent.id
            if (inter.channel.owner.id == inter.author.id) or (
                role in inter.author.roles
            ):
                if time_difference_minutes >= 30:
                    embed = disnake.Embed(
                        color=disnake.Colour.blue(),
                        title=("**🙇 Helpers Arise!**"),
                        description=(
                            "Please note that you still might not immediately get a response since all helpers are human beings and volunteers (and also might be sleeping right now)"
                        ),
                    )
                    embed.set_footer(
                        text=("Requested by " + inter.user.name),
                        icon_url=inter.user.avatar,
                    )

                    await inter.response.send_message(
                        "<@&" + str(variables.helper_role) + ">",
                        embed=embed,
                        allowed_mentions=disnake.AllowedMentions(roles=True),
                    )

                    embed = disnake.Embed(
                        color=disnake.Colour.orange(),
                        title=("**Someone will come and help soon!**"),
                        description=(
                            "💬 While you wait, take this time to provide more context and details. What are you trying to achieve overall - maybe there's an easier way to solve this problem\n\n🙇 ~~If it's been 30 minutes and you`re still waiting for someone to help, hit the __Summon Helpers__ button to call the official helpers here~~ **Someone has already summoned the helpers in this help channel!**\n\n✅ Once your question has been resolved (or you no longer need it), hit the __Resolve Question__ button or run /resolve"
                        ),
                    )
                    resolve_question_button = disnake.ui.Button(
                        label="Resolve Question",
                        custom_id="resolve_question_button",
                        style=disnake.ButtonStyle.green,
                        emoji="✅",
                    )

                    await inter.message.edit(
                        embed=embed, components=[resolve_question_button]
                    )

                    # Logging
                    embed = disnake.Embed(
                        color=disnake.Colour.orange(),
                        title=("**`Summon Helpers` Button**"),
                        description=(str(inter.user.name) + " summoned helper"),
                    )
                    channel = self.bot.get_channel(variables.logs)
                    await channel.send(embed=embed)

                else:
                    embed = disnake.Embed(
                        color=disnake.Colour.red(),
                        title=("**🕑 Be patient!**"),
                        description=(
                            "All helpers are volunteers and thus can't always respond instantly. We'd therefore advise you to give them some time! If you still haven't gotten an answer in `"
                            + str(30 - int(time_difference_minutes))
                            + " minutes` feel free to use this again to ping all helpers :D"
                        ),
                    )
                    await inter.response.send_message(embed=embed, ephemeral=True)
                    # Logging
                    embed = disnake.Embed(
                        color=disnake.Colour.orange(),
                        title=("**`Summon Helpers` Button**"),
                        description=(
                            str(inter.user.name) + " failed summoning Helpers"
                        ),
                    )
                    channel = self.bot.get_channel(variables.logs)
                    await channel.send(embed=embed)
            else:
                embed = disnake.Embed(
                    color=disnake.Color.red(),
                    title="❌ Summon Helpers",
                    description="You can't do this since you are neither a helper nor the owner of this channel!",
                )
                await inter.response.send_message(embed=embed, ephemeral=True)

                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`Summon Helpers` Button**"),
                    description=(str(inter.user.name) + " failed summoning Helpers"),
                )
                channel = self.bot.get_channel(variables.logs)
                await channel.send(embed=embed)

        if inter.component.custom_id == "newsletter_unsubscribe_button":
            with open("newsletter_subscribers.txt") as file:
                file_text = file.readlines()
                subscribers = []

            for line in file_text:
                clean_line = line.strip()
                subscribers.append(clean_line)

            if str(inter.user.id) in subscribers:
                with open("newsletter_subscribers.txt", "a") as file:
                    file.seek(0)
                    file.truncate()
                    subscribers.remove(str(inter.user.id))
                    for subscriber in subscribers:
                        file.write(subscriber + "\n")

            embed = disnake.Embed(
                color=disnake.Color.light_gray(),
                title="😔 Sad to see you go",
                description="Successfully unsubscribed you from our newsletter!\nIn case you decide otherwise or this was on accident yout can use `/newsletter` to resubscribe",
            )
            await inter.response.send_message(embed=embed)

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**`Unsubscribe` Button**"),
                description=(
                    str(inter.user.name) + " unsubscribed from the newsletter"
                ),
            )
            channel = self.bot.get_channel(variables.logs)
            await channel.send(embed=embed)
