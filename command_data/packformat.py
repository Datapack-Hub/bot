import aiohttp

from utils.log import setup_logger


class VersionData:
    def __init__(self, data):
        self.id: str = data["id"]
        self.type: str = data["type"]
        self.data_pack_version_major: float = data["data_pack_version"]
        self.data_pack_version_minor: float = data["data_pack_version_minor"]
        self.resource_pack_version_major: float = data["resource_pack_version"]
        self.resource_pack_version_minor: float = data["resource_pack_version_minor"]


VERSIONS: list[VersionData] = []


async def generate_version_data():
    if len(VERSIONS) > 0:
        return  # already populated

    logger = setup_logger("version_data")
    async with (
        aiohttp.ClientSession() as session,
        session.get("https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.json") as req,
    ):
        if req.status == 200:
            VERSIONS.extend(VersionData(item) for item in await req.json(content_type="text/plain"))
            logger.info("Successfully fetched version data")
        else:
            logger.error("Failed to fetch version data")
