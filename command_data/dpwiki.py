import requests

versions_req = requests.get("https://datapack.wiki/search.json").json()

PAGES = []
GUIDES = []

for page in versions_req:
    out = {
        "title": page["title"],
        "url": "https://datapack.wiki" + page["url"],
        "description": page["description"]
    }
    
    if page["url"].startswith("/wiki"): 
        out["type"] = "wiki"
        PAGES.append(out)
        
    if page["url"].startswith("/guide"): 
        out["type"] = "guide"
        GUIDES.append(out)