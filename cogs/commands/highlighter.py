import disnake
import variables
import dph
from disnake.ext import commands



class HighlighterCommand(commands.Cog, name="highlighter"):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(
        title="Highlighter",
        description="Allows you to toggle the serverwide mcfunction syntax highlighter",
    )
    async def highlighter(self,inter: disnake.ApplicationCommandInteraction,):
        if inter.user.guild_permissions.manage_guild:
            servers = dph.get_highlighter_server_list()
            
            if str(inter.guild.id) in servers:
                print
                button = disnake.ui.Button(
                    style = disnake.ButtonStyle.red,
                    custom_id = "dph_highlighter_off",
                    label = "Disable"
                )
            
                embed = disnake.Embed(
                    title="`mcfunction` Highlighter (ENABLED)",
                    description="The **`mcfunction` Highlighter** adds syntax highlighting to all **mcfunction code in codeblocks**. This is achvieved by **deleting** the message originally sent and **replacing it using a webhook** (with the original senders name and profile picture). \nYou can always **re-enable** this option at any time after disabling it!\n**Does not apply retroactively to already sent messages**",
                    color= disnake.Color.blue()
                )
                await inter.response.send_message(embed=embed,components=button,ephemeral=True)
                
            else:
                button = disnake.ui.Button(
                    style = disnake.ButtonStyle.green,
                    custom_id = "dph_highlighter_on",
                    label = "Enable"
                )
            
                embed = disnake.Embed(
                    title="`mcfunction` Highlighter (DISABLED)",
                    description="The **`mcfunction` Highlighter** adds syntax highlighting to all **mcfunction code in codeblocks**. This is achvieved by **deleting** the message originally sent and **replacing it using a webhook** (with the original senders name and profile picture). \nYou can always **disable** this option at any time after enabling it!\n**Does not apply retroactively to already sent messages**",
                    color= disnake.Color.blue()
                )
                await inter.response.send_message(embed=embed,components=button,ephemeral=True)  
                
            
            await dph.log("`/highlighter` Command", f"A user viewed the highlighter interaction menu","orange",self)
            
        else:
            embed = disnake.Embed(
                title="Missing Permission",
                description="You don't have permission to use this command to configure the server-wide `mcfunction` highlighter.\nMessage any of the server's administrators if you belive this to be unintentional.",
                color= disnake.Color.red()
            )
            await inter.response.send_message(embed=embed,ephemeral=True)
            await dph.log("`/highlighter` Command", f"A user attempted to use the command","red",self)