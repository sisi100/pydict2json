# pydict2json

PythonでDict型をprintしたときの出力を、json形式に整形してクリップボードに入れてくれるCLIアプリ


## 使用例

```sh
$ python -c 'from collections import OrderedDict;print(dict(key1=OrderedDict({"hoge1":123, "hoge2":"abc"}),key2="def"))'
{'key2': 'def', 'key1': OrderedDict([('hoge1', 123), ('hoge2', 'abc')])}

$ pydict2json "{'key2': 'def', 'key1': OrderedDict([('hoge1', 123), ('hoge2', 'abc')])}"
{
  "key2": "def",
  "key1": {
    "hoge1": 123,
    "hoge2": "abc"
  }
}
```

## インストール

```sh
$ pip3 install -e .
```
