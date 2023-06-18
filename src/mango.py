import os
import json
import shutil

appdata = os.getenv("appdata").replace('\\', '/')

if not os.path.isdir("./output"):
    os.mkdir("./output")
    print("MKDIR: \"./output\"")

def default_path(*paths):
    return "/".join((f"{appdata}/.minecraft/assets", *paths))

print("\n".join(os.listdir(default_path("indexes"))))
index = input("Index(Full Name): ")
with open(default_path("indexes", index)) as file:
    indexes = json.load(file)

for index_key, index_value in indexes.items():
    now = f"./output/{index_key}"
    if not os.path.isdir(now):
        os.mkdir(now)
        print(f"MKDIR: \"{now}\"")
    for item_key, item_value in index_value.items():        
        now = f"./output/{index_key}"
        for path in item_key.split("/")[:-1]: # mkdir
            now += f"/{path}"
            if os.path.isdir(now):
                continue
            os.mkdir(now)
            print(f"MKDIR: \"{now}\"")
        path = default_path(index_key, item_value["hash"][:2], item_value["hash"])
        shutil.copy(path, f'./output/{index_key}/{item_key}')
        print(f"COPY: \"{path}\" -> \"./output/{index_key}/{item_key}\"")
        if item_key.endswith(".json"):
            with open(f'./output/{index_key}/{item_key}') as file:
                data = json.load(file)
            with open(f'./output/{index_key}/{item_key}', "w", encoding="utf8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"STAGE FINISH: {index_key}")
        
        
        
