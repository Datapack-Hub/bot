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
        if re.findall(r'```mcf(?:unction)?\n([\s\S]+?)```',message.content) and (not message.author.bot):
            if message.channel.type == disnake.ChannelType.public_thread:
                hooks = await message.channel.parent.webhooks()
                
                for hook in hooks:
                    if hook.name == "Datapack Helper Bot yay":
                        break
                else:
                    hook = await message.channel.parent.create_webhook(name="Datapack Helper Bot yay")
                
                await message.delete()
                
                try:
                    await hook.send(replace_code_blocks(message.content),wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,thread=message.channel,allowed_mentions=disnake.AllowedMentions.none())
                    await dph.log("Syntax Highlighter", f"Sucessfully highlighted a user's message ","orange",self)
                except:
                    await hook.send(message.content,wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,thread=message.channel,allowed_mentions=disnake.AllowedMentions.none(),components=[disnake.ui.Button(style=disnake.ButtonStyle.red,disabled=True,label="Syntax highlighting failed")])
                    await dph.log("Syntax Highlighter", f"Failed highlighting a user's message ","red",self)
            else:
                hooks = await message.channel.webhooks()
                
                for hook in hooks:
                    if hook.name == "Datapack Helper Bot yay":
                        break
                else:
                    hook = await message.channel.create_webhook(name="Datapack Helper Bot yay")
                
                await message.delete()
                await hook.send(replace_code_blocks(message.content),wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,allowed_mentions=disnake.AllowedMentions.none())
                await dph.log("Syntax Highlighter", f"Sucessfully highlighted a user's message ","orange",self)