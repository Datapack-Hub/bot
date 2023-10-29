import disnake
from disnake.ext import commands
import variables


class OnButtonClick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        print("asdasd")

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