import json
from collections import OrderedDict
from decimal import Decimal

import pyperclip
from .json_encoder import Encoder


def clean(text: str):
    try:
        text = eval(text, {"OrderedDict": OrderedDict, "Decimal": Decimal})
    except:
        pass
    return text


def text_to_json(text: str):
    clean_text = clean(text)
    return json.dumps(clean_text, ensure_ascii=False, indent=2, cls=Encoder)


def run(text: str) -> None:
    """pythonでprint出力したDictをjson形式に整形する

    Parameters
    ----------
    text : str
        printで出力された文字列
    """
    json_text = text_to_json(text)
    print(json_text)
    pyperclip.copy(json_text)

    return True
