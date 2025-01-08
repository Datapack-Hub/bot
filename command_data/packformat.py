import requests

versions_req = requests.get("https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.json").json()

VERSIONS = [item["id"] for item in versions_req]