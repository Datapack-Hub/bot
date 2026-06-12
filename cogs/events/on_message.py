import re

import discord

from static.highlighter.highlighter import Hl


def replace_code_blocks(message: str):
    pattern = re.compile(r"```mcf(?:unction)?\n([\s\S]+?)```", re.DOTALL)

    def replace_function(match: re.Match[str]) -> str:
        code_block_content = match.group(1).strip()
        return f"```ansi\n{Hl.highlight(code_block_content)}\n```"

    edited_message = pattern.sub(replace_function, message)

    # edited_message += "\n-# Syntax highlighted by <@1108074519308017734> using [bth123's highlighter](<https://github.com/bth123/mcf-ansi-highlighter>)"

    return edited_message


class OnMessage(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_message(self, message: discord.Message):
        if re.findall(r"```mcf(?:unction)?\n([\s\S]+?)```", message.content, re.IGNORECASE) and (
            not message.author.bot
        ):
            content = message.content
            
            if content.startswith("\\```mcf"):
                return
            
            if len(replace_code_blocks(content)) >= 2000:
                await message.reply("_**ERROR**: Can't apply syntax highlighting due to message length limitations_")
            else:
                if (
                    isinstance(message.channel, discord.Thread)
                    and message.channel.type is discord.ChannelType.public_thread
                ):
                    parent = message.channel.parent
                    if parent is None:
                        return  # should never happen since the parent of a thread should always be a channel? idk

                    hooks = await parent.webhooks()

                    for hook in hooks:
                        if hook.name == "DPH Syntax Highlighter":
                            break
                    else:
                        hook = await parent.create_webhook(name="DPH Syntax Highlighter")

                    await message.delete()

                    try:
                        await hook.send(
                            replace_code_blocks(content),
                            wait=False,
                            username=message.author.display_name,
                            avatar_url=message.author.display_avatar.url,
                            thread=message.channel,
                            allowed_mentions=discord.AllowedMentions.none(),
                        )
                    except:
                        await hook.send(
                            content,
                            wait=False,
                            username=message.author.display_name,
                            avatar_url=message.author.display_avatar.url,
                            thread=message.channel,
                            allowed_mentions=discord.AllowedMentions.none(),
                            view=discord.ui.View(
                                discord.ui.Button(
                                    style=discord.ButtonStyle.red,
                                    disabled=True,
                                    label="Syntax highlighting failed",
                                )
                            ),
                        )
                else:
                    # TODO: i do not want to figure out types for this
                    hooks = await message.channel.webhooks()  # type: ignore

                    for hook in hooks:
                        if hook.name == "DPH Syntax Highlighter":
                            break
                    else:
                        hook = await message.channel.create_webhook(name="DPH Syntax Highlighter")  # type: ignore #asd

                    await message.delete()
                    try:
                        await hook.send(
                            replace_code_blocks(content),
                            wait=False,
                            username=message.author.display_name,
                            avatar_url=message.author.display_avatar.url,
                            allowed_mentions=discord.AllowedMentions.none(),
                        )
                    except:
                        await hook.send(
                            content,
                            wait=False,
                            username=message.author.display_name,
                            avatar_url=message.author.display_avatar.url,
                            allowed_mentions=discord.AllowedMentions.none(),
                            view=discord.ui.View(
                                discord.ui.Button(
                                    style=discord.ButtonStyle.red,
                                    disabled=True,
                                    label="Syntax highlighting failed",
                                )
                            ),
                        )
