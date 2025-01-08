import requests

versions_req = requests.get("https://datapack.wiki/search.json").json()

PAGES = []
GUIDES = []

for page in versions_req:
    out = {
        "title": page["title"],
        "url": "https://datapack.wiki" + page["url"]
    }
    
    if page["url"].startswith("/wiki"): PAGES.append(out)
    if page["url"].startswith("/guide"): GUIDES.append(out)