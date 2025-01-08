import requests

vanilla_files_req = requests.get("https://api.github.com/repos/misode/mcmeta/git/trees/data?recursive=1").json()

VANILLA_FILES = [item["path"] for item in vanilla_files_req["tree"] if item["type"] == "blob"]