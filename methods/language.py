import create_json


valid_langs = ["uz"]


def load_json(file_name):
    with open(file_name) as f:
        return json.load(f)


def load_lang(lang):
    if lang in valid_langs:
        return load_json(f"lang/{lang}.json")
    else:
        return load_json(f"lang/uz.json")
