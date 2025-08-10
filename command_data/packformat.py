import requests

versions_req = requests.get("https://raw.githubusercontent.com/misode/mcmeta/summary/versions/data.json").json()

VERSIONS = [{
    "id": item["id"],
    "type": item["type"],
    "data_pack_version": {
        "major": item["data_pack_version"],
        "minor": item["data_pack_version_minor"]
    },
    "resource_pack_version": {
        "major": item["resource_pack_version"],
        "minor": item["resource_pack_version_minor"]
    }
} for item in versions_req]