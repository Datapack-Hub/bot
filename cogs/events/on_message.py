import disnake
import variables
from disnake.ext import commands
import re
from static.highlighter.highlighter import Hl


def replace_code_blocks(message: disnake.Message, author: disnake.Member):
    pattern = re.compile(r'```mcf(?:unction)?\n([\s\S]+?)```', re.DOTALL)

    def replace_function(match):
        code_block_content = match.group(1).strip()
        return f'```ansi\n{Hl.highlight(code_block_content)}\n```'

    edited_message = pattern.sub(replace_function, message)
    
    edited_message += f"\n-# Syntax highlighted by <@1108074519308017734> using [bth123's highlighter](<https://github.com/bth123/mcf-ansi-highlighter>)"

    return edited_message

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                         
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if re.findall(r'```mcf(?:unction)?\n([\s\S]+?)```',message.content) and (not message.author.bot):
            content = (message.content)
            if len(replace_code_blocks(content, message.author)) >= 2000:
                await message.reply("_**ERROR**: Can't apply syntax highlighting due to message length limitations_")
            else: 
                if message.channel.type == disnake.ChannelType.public_thread:
                    hooks = await message.channel.parent.webhooks()

                    for hook in hooks:
                        if hook.name == "DPH Syntax Highlighter":
                            break
                    else:
                        hook = await message.channel.parent.create_webhook(name="DPH Syntax Highlighter")

                    await message.delete()

                    try:
                        await hook.send(replace_code_blocks(content, message.author),wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,thread=message.channel,allowed_mentions=disnake.AllowedMentions.none())
                    except:
                        await hook.send(content,wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,thread=message.channel,allowed_mentions=disnake.AllowedMentions.none(),components=[disnake.ui.Button(style=disnake.ButtonStyle.red,disabled=True,label="Syntax highlighting failed")])
                else:
                    hooks = await message.channel.webhooks()

                    for hook in hooks:
                        if hook.name == f"DPH Syntax Highlighter":
                            break
                    else:
                        hook = await message.channel.create_webhook(name=f"DPH Syntax Highlighter") #asd

                    await message.delete()
                    await hook.send(replace_code_blocks(content, message.author),wait=False,username=message.author.display_name,avatar_url=message.author.display_avatar.url,allowed_mentions=disnake.AllowedMentions.none())
