import requests

from utils.log import setup_logger

logger = setup_logger("vanilla_data")
logger.info("Fetching vanilla file list...")
vanilla_files_req = requests.get(
    "https://api.github.com/repos/misode/mcmeta/git/trees/data?recursive=1", timeout=5
).json()

VANILLA_FILES: list[str] = [item["path"] for item in vanilla_files_req["tree"] if item["type"] == "blob"]
logger.info("Successfully fetched vanilla file list.")
