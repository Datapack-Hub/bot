import disnake
from disnake.ext import commands
import variables
import os
import re

newsletter_unsubscribe_button = disnake.ui.Button(
    label="Unsubscribe",
    custom_id="newsletter_unsubscribe_button",
    style=disnake.ButtonStyle.gray,
)


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        intro_channel = self.bot.get_channel(variables.intro_channel)
        newsletter_channel = self.bot.get_channel(
            variables.newsletter_broadcast_channel
        )

        if ("<@" + str(variables.bot_id) + ">") in message.content:
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("👋 Hey there!"),
                description=(
                    "I am Datapack Helper a discord bot focused on helping you with everything datapacks and maintained by [Datapack Hub](https://discord.datapackhub.net)!\nTo learn about my commands run `/help` (not implemented yet) and to report bugs and similar feel free to report them [here](https://discord.datapackhub.net) (channels private till bot goes public)."
                ),
            )
            await message.reply(embed=embed)

        elif message.channel == intro_channel:
            await message.add_reaction("👋")

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**Intro Channel Reaction**"),
                description=(
                    "Reacted with :wave: to "
                    + message.author.name
                    + "'s message in <#"
                    + intro_channel
                    + ">"
                ),
            )
            channel = self.bot.get_channel(variables.logs)
            await channel.send(embed=embed)
        elif ("flyrr_" == message.author.name) and (">.< shutdown" in message.content):
            methods = os.listdir(".\\method")
            commands.option_enum(methods)

            # Logging
            embed = disnake.Embed(
                color=disnake.Colour.purple(),
                title=("**Magic** :sparkles:"),
                description=(
                    "The bot was forced to shutdown by some strange magical power...\nNew Contents: `"
                    + str(methods)
                    + "`"
                ),
            )
            channel = self.bot.get_channel(variables.logs)
            await channel.send(embed=embed)
            await self.bot.close()

        # BROADCAST NEWSLETTER
        elif ("flyrr_" == message.author.name) and (">.< give me the names ahh" in message.content):
            
            guild = message.guild
            n = 0
            members = []
            for member in guild.members:
                members.append(member.name)
                
            print("summon text_display ~ ~ ~ {Tags:[\"rotate\"],text:'{\"text\":\""+ members[0] +"\\\n"+ members[1] +"\\\n"+ members[2] +"\\\n"+ members[3] +"\\\n"+ members[4] +"\\\n"+ members[5] +"\\\n"+ members[6] +"\\\n"+ members[7] +"\\\n"+ members[8] +"\\\n"+ members[9] +"\"}'}`")
            members = members[10:]
                    
                
        elif message.channel == newsletter_channel:
            if (message.author.id == 880000911848636468) or (message.author.id == 543741360478355456):
                hide_unsub_button = False
                edit_last = False
                no_title = False
                hide_author = False
                custom_color = False

                channel = message.channel
                text = message.content
                title = ""
                lines = text.splitlines()
                description = text
                subscribers = []

                if "!!NO-TITLE" not in text:
                    title = lines[0]
                    description = description.replace(title, "")
                else:
                    description = description.replace("!!NO-TITLE", "")
                    no_title = True

                if ((title == "" in text) and (no_title is not True)) or (
                    len(lines) < 2
                ):
                    await message.add_reaction("❌")

                else:
                    print(str(len(lines)))

                    if "!!HIDE-UNSUB-BUTTON" in text:
                        hide_unsub_button = True
                        description = description.replace("!!HIDE-UNSUB-BUTTON", "")
                    if "!!EDIT-LAST" in text:
                        edit_last = True
                        description = description.replace("!!EDIT-LAST", "")
                    if "!!HIDE-AUTHOR" in text:
                        hide_author = True
                        description = description.replace("!!HIDE-AUTHOR", "")
                    if "!!CUSTOM-COLOR" in text:
                        custom_color = True
                        r_value = (re.search(r"!!CUSTOM-COLOR\s+(\d+)", text)).group(1)
                        b_value = (
                            re.search(r"!!CUSTOM-COLOR\s+\d+\s+(\d+)", text)
                        ).group(1)
                        g_value = (
                            re.search(r"!!CUSTOM-COLOR\s+\d+\s+\d+\s+(\d+)", text)
                        ).group(1)
                        description = re.sub(
                            r"!!CUSTOM-COLOR\s+\d+\s+\d+\s+\d+", "", description
                        )

                    with open("newsletter_subscribers.txt") as file:
                        description_copy = description
                        file_text = file.readlines()
                        subscribers = []

                        for line in file_text:
                            clean_line = line.strip()
                            subscribers.append(clean_line)

                        print(subscribers)

                        for subscriber in subscribers:
                            description_copy = description
                            user = self.bot.get_user(int(subscriber))
                            print(">>" + subscriber + "," + str(user))

                            description_copy = description_copy.replace(
                                "{{username}}", ("<@" + str(subscriber) + ">")
                            )
                            description_copy = description_copy.replace(
                                "{{bot}}", ("<@" + str(variables.bot_id) + ">")
                            )

                            if custom_color is not True:
                                embed = disnake.Embed(
                                    color=disnake.Colour.orange(),
                                    title=title,
                                    description=description_copy,
                                )
                            else:
                                embed = disnake.Embed(
                                    color=disnake.Color.from_rgb(
                                        int(r_value), int(g_value), int(b_value)
                                    ),
                                    title=title,
                                    description=description_copy,
                                )

                            if hide_author is False:
                                embed.set_footer(
                                    text=(
                                        "Message written and broadcasted by "
                                        + message.author.name
                                    ),
                                    icon_url=message.author.display_avatar,
                                )
                            else:
                                embed.set_footer(
                                    text=("Message provided by Datapack Hub"),
                                    icon_url="https://media.discordapp.net/attachments/1129493191847071875/1144716754292056126/ob0WaKM.png",
                                )

                            if edit_last is True:
                                dm_message = await user.history(limit=1).flatten()
                                message_obect = dm_message[0]
                                message_id = message_obect.id
                                print(message_id)
                                dm_message = await user.fetch_message(message_id)

                                if hide_unsub_button is True:
                                    await dm_message.edit(embed=embed, components=[])
                                    await message.add_reaction("🤫")
                                else:
                                    await dm_message.edit(
                                        embed=embed,
                                        components=[newsletter_unsubscribe_button],
                                    )
                                await message.add_reaction("✏️")
                            else:
                                if hide_unsub_button is True:
                                    await user.send(embed=embed)
                                    await message.add_reaction("🤫")
                                else:
                                    print(user)
                                    await user.send(
                                        embed=embed,
                                        components=[newsletter_unsubscribe_button],
                                    )
                                await message.add_reaction("📣")
            else:
                await message.delete()
