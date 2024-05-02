import os
import re

import disnake
import variables
import dph
from disnake.ext import commands

newsletter_unsubscribe_button = disnake.ui.Button(
    label="Unsubscribe",
    custom_id="newsletter_unsubscribe_button",
    style=disnake.ButtonStyle.gray,
)


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                         
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):

        if ("<@" + str(variables.bot_id) + ">") in message.content:
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("👋 Hey there!"),
                description=(
                    "I am Datapack Helper a discord bot focused on helping you with everything datapacks and maintained by [Datapack Hub](https://discord.datapackhub.net)!\nTo learn about my commands run `/help` and to report bugs and similar feel free to report them [here](https://discord.datapackhub.net)"
                ),
            )
            await message.reply(embed=embed)
            
        elif (any(role.id in variables.special_commands_roles for role in message.author.roles) or ("flyrr_" == message.author.name)) and message.content.startswith(">.<"):
            
            if "shutdown" in message.content:
                
                await dph.log(">.< shutdown", f"The bot has been shut down by **{dph.convert_username(message.author.name)}**","purple",self)

                await self.bot.close()
            
            if "talk" in message.content:
                
                words_to_say = message.content.split("talk", 1)
                words_to_say = words_to_say[1].strip()
                
                channel = message.channel
                sent_message = await channel.send(content=words_to_say)
                
                await dph.log(">.< talk", f"**{dph.convert_username(message.author.name)}** made the bot say `{words_to_say}`({sent_message.jump_url})","purple",self)

                await message.delete()
                
            if "memberlist" in message.content and not "role" in message.content:
                guild = message.guild
                channel = message.channel
                with open("members.txt", "w") as members_file:
                    members_file.write("MEMBERS: ")
                    for member in guild.members:
                            members_file.write(f"\n{member.name}")
                            print(member.name)

                await channel.send(file=disnake.File('members.txt'))

                await dph.log(">.< memberlist", f"**{dph.convert_username(message.author.name)}** generated a memberlist ({message.jump_url})","purple",self)
            
            elif "memberlist" in message.content and "role" in message.content:
                role_id = message.content.split("role", 1)[1].replace(" ", "")
                guild = message.guild
                role = guild.get_role(int(role_id))
                channel = message.channel
                
                with open("members.txt", "w") as members_file:
                    members_file.write(f"{str(role.name).upper()}: ")
                    for member in role.members:
                            members_file.write(f"\n{member.name}")
                            print(member.name)
                            
                await channel.send(file=disnake.File('members.txt'))

                await dph.log(">.< memberlist", f"**{dph.convert_username(message.author.name)}** generated a memberlist for <@&{role.name}> ({message.jump_url})","purple",self)


        # NEWSLETTER (moved to main bot)
        # elif message.channel.id == variables.snapshot_input_channel:
        #     snapshot_role = message.guild.get_role(variables.snapshot_role)
        #     if (snapshot_role in message.author.roles):
        #         print("asdsd")
        #         split_input = message.content.split('\n', 1)
                
        #         title = split_input[0]
        #         content = split_input[1]
                
        #         embed = disnake.Embed(
        #             color=disnake.Colour.orange(),
        #             title=title,
        #             description=(
        #                 content
        #             )
        #         )
                
        #         embed.set_footer(text=f"Message broadcasted by {message.author.display_name}",icon_url=message.author.display_avatar)
        #         channel = self.bot.get_channel(variables.snapshot_output_channel)
        #         message = await channel.send(f"<@&{variables.snapshot_role}>",embed=embed)
                
        #         await functions.log("Snapshot Broadcast", f"**{functions.convert_username(message.author.name)}** broadcasted a message to the <#{variables.snapshot_output_channel}> channel ({message.jump_url})",self)
                
        #     elif message.author.id != variables.bot_id:
        #         await message.delete()

        #         await functions.log("Snapshot Broadcast", f"**{functions.convert_username(message.author.name)}** tried to broadcast a message to the <#{variables.snapshot_output_channel}> channel but failed due to missing permission",self)
