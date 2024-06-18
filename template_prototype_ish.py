import requests 
import variables
import os
import shutil

path = f"{variables.full_path}/generated/dp_template"

try: 
    shutil.rmtree(f"{path}/data/namespace")
except:
    print("Namespace folder not found")
    
os.mkdir(f"{path}/data/namespace")

headers = {'Authorization': f'token {variables.github_token}'}

response = requests.get('https://api.github.com/repos/misode/mcmeta/contents/data/minecraft?ref=data',headers=headers)

items = response.json()

folders = [item['name'] for item in items]
subfolders = []

for folder in folders:
    print(f"Fetching contents of {folder}...")
    folder_subfolders = []
    
    response = requests.get(f'https://api.github.com/repos/misode/mcmeta/contents/data/minecraft/{folder}?ref=data',headers=headers)
    items = response.json()
    
    folder_subfolders = [item['name'] for item in items if item['type'] == 'dir']
    
    print(folder_subfolders)
    
    subfolders.insert(-1,folder_subfolders)
    
print("---------------------------------------------------")
i = -1

for folder in folders:
    print(folder)
    os.mkdir(f"{path}/data/namespace/{folder}")
#    if not [] == subfolders[i]:
    for subfolder in subfolders[i]:
        os.mkdir(path=f"{path}/data/namespace/{folder}/{subfolder}")
        print(f"     -{subfolder}")
    i = i + 1

with open(f"{path}/mcmeta.json","w") as mcmeta_file:
    mcmeta_file.write("""{
    "pack":{
        "pack_format": 40,
        "description":[
            {"text":"0.20.6 Datapack Template, made with <3 by Datapack Hub","color":"#FF631A"}
        ]
    }
}
""")