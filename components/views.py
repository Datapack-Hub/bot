import discord

import variables


class InfoView(discord.ui.DesignerView):
    def __init__(self, info: dict[str, str | None]):
        super().__init__(timeout=None)

        container = discord.ui.Container()

        container.add_text(f"-# {variables.ICON_EMOJI} Datapack Development: Info")
        container.add_text(f"## {info['name']}")
        container.add_text(f"{info['content']}")

        if info["image"] is not None:
            gallery = discord.ui.MediaGallery().add_item(url=info["image"])

            container.add_item(gallery)

        self.add_item(container)


class LinkView(discord.ui.DesignerView):
    def __init__(self, link: dict[str, str]):
        super().__init__(timeout=None)

        container = discord.ui.Container()

        container.add_text(f"-# {variables.ICON_EMOJI} Datapack Development: Useful Link")
        container.add_text(f"## {link['name']}")
        container.add_text(f"**About:** {link['about']}")
        container.add_text(f"**Link:** {link['link']}")

        self.add_item(container)


class WikiPage(discord.ui.DesignerView):
    def __init__(self, wiki_page: dict[str, object]):
        super().__init__(timeout=None)

        container = discord.ui.Container()

        if wiki_page["type"] == "wiki":
            container.add_text(f"-# {variables.ICON_EMOJI} Datapack Wiki Page")
        else:
            container.add_text(f"-# {variables.ICON_EMOJI} Datapack Wiki Guide")

        container.add_text(f"## {wiki_page['title']}")
        container.add_text(f"**Description:** {wiki_page['description']}")
        container.add_text(f"**Link:** {wiki_page['url']}")

        self.add_item(container)


class PackFormatView(discord.ui.DesignerView):
    def __init__(self, version: str, out: str):
        super().__init__(timeout=None)

        container = discord.ui.Container()

        container.add_text(f"-# {variables.ICON_EMOJI} Minecraft Java Pack Format")

        container.add_text(f"## Pack Format: `{version}`")
        container.add_text(out)

        self.add_item(container)


class VanillaFileView(discord.ui.DesignerView):
    def __init__(self, path: str, content: str):
        super().__init__(timeout=None)

        container = discord.ui.Container()

        container.add_text(f"-# {variables.ICON_EMOJI} Datapack Development: Vanilla File")

        container.add_text(f"## `{path}`")
        if len(f"```json\n{content}```") > 3000:
            container.add_text(
                "This file is too large to show in Discord! However, you can still view this file on Github."
            )
        else:
            container.add_text(f"```json\n{content}```")

        container.add_item(
            discord.ui.ActionRow(
                discord.ui.Button(
                    label="View this file on Github",
                    url=f"https://raw.githubusercontent.com/misode/mcmeta/data/{path}",
                )
            )
        )

        self.add_item(container)


class HelpView(discord.ui.DesignerView):
    def __init__(self, content: str):
        super().__init__(timeout=None)

        container = discord.ui.Container()

        container.add_text(f"## {variables.ICON_EMOJI} Datapack Helper")

        container.add_text(content)

        row = discord.ui.ActionRow()
        row.add_button(label="GitHub", url="https://github.com/Datapack-Hub/bot")
        row.add_button(label="Datapack Hub", url="https://discord.gg/aEXsdjjdu4")

        container.add_item(row)

        self.add_item(container)


class AdminMessageView(discord.ui.DesignerView):
    def __init__(self, title: str, message: str):
        super().__init__(timeout=None)

        container = discord.ui.Container()

        container.add_text(f"-# {variables.ICON_EMOJI} Datapack Helper Announcement")

        container.add_text(f"## {title}")
        container.add_text(f"{message}")

        self.add_item(container)
