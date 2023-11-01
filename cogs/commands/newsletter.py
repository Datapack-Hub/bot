import disnake
import variables
from disnake.ext import commands

newsletter_unsubscribe_button = disnake.ui.Button(
    label="Unsubscribe",
    custom_id="newsletter_unsubscribe_button",
    style=disnake.ButtonStyle.gray,
)


class NewsletterCommand(commands.Cog, name="newsletter"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="newsletter",
        description="EXPERIMENTAL!! Subscribes/Unsubscribes you to our datapack related DM newsletter.",
    )
    async def newsletter(self, inter: disnake.ApplicationCommandInteraction):
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
                    color=disnake.Colour.yellow(),
                    title=("**📰 Datapack Newsletter**"),
                    description="Unsubscribed you from out DM Datapack Newsletter!\n**This is an experimental feature and might get discontinued at any time without warning**",
                )

                await inter.response.send_message(embed=embed, ephemeral=True)

                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`/newsletter` Experimental Command**"),
                    description=(
                        str(inter.user.name)
                        + " unsubscribed from the newsletter (Server: **"
                        + inter.guild.name
                        + "**)"
                    ),
                )
                channel = self.bot.get_channel(variables.logs)
                await channel.send(embed=embed)

            else:
                with open("newsletter_subscribers.txt", "a") as file:
                    file.write(str(inter.user.id) + "\n")

                subscribers.append(str(inter.user.id))

                embed = disnake.Embed(
                    color=disnake.Colour.yellow(),
                    title=("**📰 Datapack Newsletter**"),
                    description="Added you to our DM Datapack Newsletter! If everything worked correctly, you should also have just recieved your first DM from this bot :D\n**This is an experimental feature and might get discontinued at any time without warning**",
                )
                await inter.response.send_message(embed=embed, ephemeral=True)

                inter.user.create_dm()

                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**👋 Hey there!**"),
                    description="Welcome to the Datapack Hub `Datapack Newsletter`! :eyes: \nFrom now on you will recieve an epic summary message whenever something relevant happens in the datapacking universe! :sparkles:\nIf you wish to unsubscribe click the `Unsubscribe` Button or use `/newsletter` again",
                )

                await inter.user.send(
                    embed=embed, components=[newsletter_unsubscribe_button]
                )

                # Logging
                embed = disnake.Embed(
                    color=disnake.Colour.orange(),
                    title=("**`/newsletter` Experimental Command**"),
                    description=(
                        str(inter.user.name)
                        + " subscribed to the newsletter (Server: **"
                        + inter.guild.name
                        + "**)"
                    ),
                )
                channel = self.bot.get_channel(variables.logs)
                await channel.send(embed=embed)

            print(subscribers)
