import disnake
from disnake.ext import commands
import variables
import re
from cogs.message_commands.highlighter import Highlighter

class FancifyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Fancify ✨")
    async def fancify(self, inter: disnake.MessageCommandInteraction,message):
        # Find all code blocks in the message content
        p = re.compile(r"(?<!\\)(\\{2})*```(.*?(?<!\\))(\\{2})*```", flags=re.DOTALL)
        matches = re.findall(p,message.content)
        
        for match in matches:
            # Split the code block content into lines
            lines = match[1].split('\n')
            # Check if the first line is a language identifier and remove it
            if re.match(r"^[a-z]+$", lines[0]): lines = lines[1:]
            # Remove empty lines from the start and end
            while lines and lines[0] == '': lines.pop(0)
            while lines and lines[-1] == '': lines.pop()
            # Convert lines back into one string
            match_content = '\n'.join(lines)
            
            output = Highlighter.highlight(match_content)
            
            
            
        # Check if the message has no embeds, stickers, or attachments
        if (not message.embeds) and (not message.stickers) and (not message.attachments):
            # Check if matches were found
            if matches:
                # Create embed with the fancified code block
                embed = disnake.Embed(
                    description="```ansi\n" + output + "\n```",
                    color=disnake.Colour.purple()
                )

            else:
                # Fancify the entire message content
                output = Highlighter.highlight((message.content).split('\n'))
                # Create embed with the fancified message
                
            # Reply to the original message with the embed
            await inter.target.reply("```ansi\n" + output + "\n```")
            # Send a success message to the user who invoked the command
            await inter.response.send_message("Fancification successful :sparkles:", ephemeral=True)

            # Logging embed creation
            embed = disnake.Embed(
                color=disnake.Colour.orange(),
                title=("**`Fancify` Message Command**"),
                description=(
                    str(inter.user.name)
                    + "Fancified a message! "
                    + str(message.jump_url)
                    + " (Server: **"
                    + inter.guild.name
                    + "**)"
                )
            )
            # Get the logs channel and send the logging embed
            channel = self.bot.get_channel(variables.logs)
            await channel.send(embed=embed)

        else:
            # Send an error message if the message cannot be fancified
            await inter.response.send_message("You can't fancify this message!", ephemeral=True)

