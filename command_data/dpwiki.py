import aiohttp

from utils.log import setup_logger

WIKI_PAGES = []
GUIDES = []


async def generate_dpwiki_data():
    if len(WIKI_PAGES) > 0 or len(GUIDES) > 0:
        return  # already populated

    logger = setup_logger("dpwiki_data")
    async with aiohttp.ClientSession() as session, session.get("https://wiki.datapackhub.net/search.json") as req:
        if req.status == 200:
            for page in await req.json():
                out = {
                    "title": page["title"],
                    "url": "https://wiki.datapackhub.net" + page["url"],
                    "description": page["description"],
                }

                if page["url"].startswith("/wiki"):
                    out["type"] = "wiki"
                    WIKI_PAGES.append(out)

                if page["url"].startswith("/guide"):
                    out["type"] = "guide"
                    GUIDES.append(out)
            logger.info("Successfully fetched DPWiki data")
        else:
            logger.error("Failed to fetch DPWiki data")
