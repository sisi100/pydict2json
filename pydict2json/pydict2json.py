import json
from collections import OrderedDict

import pyperclip
from fire import Fire


def run(text: str) -> None:
    """pythonでprint出力したDictをjson形式に整形する

    Parameters
    ----------
    text : str
        printで出力された文字列
    """

    param = dict(ensure_ascii=False, indent=2)
    try:
        origine_dict = eval(text, {"OrderedDict": OrderedDict})
        body = json.dumps(origine_dict, **param)
    except:
        body = json.dumps(text, **param)

    print(body)
    pyperclip.copy(body)



def main():
    Fire(run)
