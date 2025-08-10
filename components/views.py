import discord
import variables

class InfoView(discord.ui.View):
    def __init__(self, info: list[dict[str, object]]):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        container.add_text(f"-# {variables.icon_emoji} Datapack Development: Info")
        container.add_text(f"## {info['name']}")
        container.add_text(info['content'])
        
        if info['image']:
            container.add_gallery(discord.MediaGalleryItem(url=info['image']))
        
        self.add_item(container)
        
class LinkView(discord.ui.View):
    def __init__(self, link: list[dict[str, object]]):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        container.add_text(f"-# {variables.icon_emoji} Datapack Development: Useful Link")
        container.add_text(f"## {link['name']}")
        container.add_text(f"**About:** {link['about']}")
        container.add_text(f"**Link:** {link['link']}")
        
        self.add_item(container)
        
class LinkView(discord.ui.View):
    def __init__(self, link: list[dict[str, object]]):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        container.add_text(f"-# {variables.icon_emoji} Datapack Development: Useful Link")
        container.add_text(f"## {link['name']}")
        container.add_text(f"**About:** {link['about']}")
        container.add_text(f"**Link:** {link['link']}")
        
        self.add_item(container)
        
class WikiPage(discord.ui.View):
    def __init__(self, wikipage: list[dict[str, object]]):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        if wikipage['type'] == "wiki":
            container.add_text(f"-# {variables.icon_emoji} Datapack Wiki Page")
        else:
            container.add_text(f"-# {variables.icon_emoji} Datapack Wiki Guide")
            
        container.add_text(f"## {wikipage['title']}")
        container.add_text(f"**Description:** {wikipage['description']}")
        container.add_text(f"**Link:** {wikipage['url']}")
        
        self.add_item(container)
        
class PackFormatView(discord.ui.View):
    def __init__(self, version: str, out: str):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        container.add_text(f"-# {variables.icon_emoji} Minecraft Java Pack Format")
            
        container.add_text(f"## Pack Format: `{version}`")
        container.add_text(out)
        
        self.add_item(container)
        
class VanillaFileView(discord.ui.View):
    def __init__(self, path: str, content: str):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        container.add_text(f"-# {variables.icon_emoji} Datapack Development: Vanilla File")
            
        container.add_text(f"## `{path}`")
        if len(f"```json\n{content}```") > 3000: 
            container.add_text(f"This file is too large to show in Discord! However, you can still view this file on Github.")
        else:
            container.add_text(f"```json\n{content}```")
            
        container.add_item(discord.ui.Button(label="View this file on Github",url=f"https://raw.githubusercontent.com/misode/mcmeta/data/{path}"))
        
        self.add_item(container)
        
class HelpView(discord.ui.View):
    def __init__(self, content: str):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        container.add_text(f"## {variables.icon_emoji} Datapack Helper")
            
        container.add_text(content)
            
        container.add_item(discord.ui.Button(label="GitHub",url="https://github.com/Datapack-Hub/bot"))
        container.add_item(discord.ui.Button(label="Datapack Hub",url="https://discord.gg/aEXsdjjdu4"))
        
        self.add_item(container)
        
class AdminMessageView(discord.ui.View):
    def __init__(self, title: str, message: str):
        super().__init__(timeout=None)
        
        container = discord.ui.Container()
        
        container.add_text(f"-# {variables.icon_emoji} Datapack Helper Announcement")
            
        container.add_text(f"## {title}")
        container.add_text(f"{message}")
        
        self.add_item(container)