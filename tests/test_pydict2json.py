import json
from collections import OrderedDict
from copy import copy
from decimal import Decimal
from typing import Tuple

import pytest

import pydict2json


def clear_text(text: str):
    """改行と空白を削除する"""
    lines = text.splitlines()
    return "".join(lines).replace(" ", "")


def dummy_data() -> str:
    # 期待値
    dummy_1 = {
        "hoge": 1234,
        "hoge_ordered_dict": {"key1": 1, "key2": "a"},
        "hoge_decimal": "348559.097765",
    }
    json_text = clear_text(json.dumps(dummy_1))

    # テスト用のテキストデータ
    dummy_2 = copy(dummy_1)
    dummy_2.update(
        {
            "hoge_ordered_dict": OrderedDict(dummy_1["hoge_ordered_dict"]),
            "hoge_decimal": Decimal(dummy_1["hoge_decimal"]),
        }
    )
    python_dict_text = dummy_2.__str__()
    return python_dict_text, json_text


@pytest.mark.parametrize("python_dict_text, json_text", [dummy_data()])
def test_success(python_dict_text: str, json_text: str):
    assert json_text == clear_text(pydict2json.text_to_json(python_dict_text))
