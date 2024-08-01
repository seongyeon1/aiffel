import json

def open_json(file_path: str) -> dict[str, int]:
    with open(file_path, "r", encoding="utf-8") as file:
        word_to_index = json.load(file)
    return word_to_index