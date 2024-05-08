import os
import re

import disnake
import variables
import dph
from disnake.ext import commands

from cogs.listeners.highlighter.highlighter import Hl

newsletter_unsubscribe_button = disnake.ui.Button(
    label="Unsubscribe",
    custom_id="newsletter_unsubscribe_button",
    style=disnake.ButtonStyle.gray,
)

def replace_code_blocks(message):
    pattern = re.compile(r'```mcf(?:unction)?\n([\s\S]+?)```', re.DOTALL)

    def replace_function(match):
        code_block_content = match.group(1).strip()
        return f'```ansi\n{Hl.highlight(code_block_content)}\n```'

    edited_message = pattern.sub(replace_function, message)

    return edited_message

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                         
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        
        highlighter_servers = dph.get_highlighter_server_list()
        
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
                
            if "memberlist" in message.content and "role" not in message.content:
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
        
        if re.findall(r'```mcf(?:unction)?\n([\s\S]+?)```',message.content) and (not message.author.bot) and (str(message.guild.id) in highlighter_servers):
            if message.channel.type == disnake.ChannelType.public_thread:
                hooks = await message.channel.parent.webhooks()
                
                for hook in hooks:
                    if hook.name == "DPH":
                        break
                else:
                    hook = await message.channel.parent.create_webhook(name="DPH")
                
                await message.delete()
                try:
                    await hook.send(replace_code_blocks(message.content),wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,thread=message.channel,allowed_mentions=disnake.AllowedMentions.none())
                except:
                    await hook.send(message.content,wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,thread=message.channel,allowed_mentions=disnake.AllowedMentions.none(),components=[disnake.ui.Button(style=disnake.ButtonStyle.red,disabled=True,label="Syntax highlighting failed")])
            else:
                hooks = await message.channel.webhooks()
                
                for hook in hooks:
                    if hook.name == "DPH":
                        break
                else:
                    hook = await message.channel.create_webhook(name="DPH")
                
                await message.delete()
                await hook.send(replace_code_blocks(message.content),wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,allowed_mentions=disnake.AllowedMentions.none())
