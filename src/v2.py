import os
import json
import shutil
from pathlib import Path
from typing import Any, Dict

appdata = Path(os.getenv("appdata"))

(output := Path("./output")).mkdir(parents=True, exist_ok=True)
default_path = appdata / ".minecraft" / "assets"

print("\n".join(os.listdir(default_path / "indexes")))

index = input("Index(Full Name): ")

with open(default_path / "indexes" / index) as file:
    indexes: Dict[str, Dict[str, Any]] = json.load(file)


for index_key, index_value in indexes.items():
    (now := output / index_key).mkdir(parents=True, exist_ok=True)

    for item_key, item_value in index_value.items():
        (now / item_key).parent.mkdir(parents=True, exist_ok=True)

        path: Path = default_path / index_key / \
            item_value["hash"][:2] / item_value["hash"]

        if item_key.endswith(".json"):
            data = path.read_text("utf-8")
            with open(now / item_key, "w", encoding="utf8") as file:
                json.dump(json.loads(data), file, indent=4, ensure_ascii=False)
        else:
            shutil.copy(path, now / item_key)

        print(f"COPY: {str(path)!r} -> {str(now / item_key)!r}")
    print(f"STAGE FINISH: {index_key}")