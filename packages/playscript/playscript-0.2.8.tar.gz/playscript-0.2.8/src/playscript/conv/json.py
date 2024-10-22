import json

from .. import PScLineType, PScLine, PSc


class _PScObjEncoder(json.JSONEncoder):
    """Convert PSc object to a dict structure.
    """

    def default(self, obj):
        if isinstance(obj, PSc):
            return {
                'class': 'PSc',
                'title': obj.title,
                'author': obj.author,
                'chars': obj.chars,
                'lines': obj.lines,
            }
        else:
            return super().default(obj)


class _PScLineObjEncoder(json.JSONEncoder):
    """Convert PScLine object to a dict structure.
    """

    def default(self, obj):
        if isinstance(obj, PScLine):
            line_dict = {
                'class': 'PScLine',
                'type': obj.type.name,
            }
            if hasattr(obj, 'name'):
                line_dict['name'] = obj.name
            if hasattr(obj, 'text'):
                line_dict['text'] = obj.text
            return line_dict
        else:
            return super().default(obj)


class _PScEncoder(_PScObjEncoder, _PScLineObjEncoder):
    """Encode whole PSc object to a JSON string.
    """
    pass


def psc_dump(psc, fp, cls=_PScEncoder, ensure_ascii=False, **kwargs):
    """台本オブジェクトをシリアライズして JSON ファイルに書き出す

    Parameters
    ----------
    psc : PSc
        台本オブジェクト
    fp : file-like
        出力先ファイル (ストリーム)
    cls : class
        エンコードに使うクラス
    ensure_ascii : bool
        ASCII 文字に限定するかどうか
    **kwargs
        json.dump に渡すキーワード引数
    """
    kwargs['cls'] = cls
    kwargs['ensure_ascii'] = ensure_ascii
    json.dump(psc, fp, **kwargs)


def psc_dumps(psc, cls=_PScEncoder, ensure_ascii=False, **kwargs):
    """台本オブジェクトをシリアライズして JSON 文字列に書き出す

    Parameters
    ----------
    psc : PSc
        台本オブジェクト
    cls : class
        エンコードに使うクラス
    ensure_ascii : bool
        ASCII 文字に限定するかどうか
    **kwargs
        json.dumps に渡すキーワード引数

    Returns
    -------
    JSON 文字列 : str
    """
    kwargs['cls'] = cls
    kwargs['ensure_ascii'] = ensure_ascii
    return json.dumps(psc, **kwargs)


def _psc_dict_hook(obj):
    """Decode a dict with entry class:PSc into PSc object.
    """
    if type(obj) == dict and obj.get('class') == 'PSc':
        title = obj.get('title', '')
        author = obj.get('author', '')
        chars = obj.get('chars', [])
        lines = obj.get('lines', [])

        sc = PSc(title=title, author=author, chars=chars, lines=lines)
        return sc
    else:
        return obj


def _psc_line_dict_hook(obj):
    """Decode a dict with entry class:PScLine into PScLine object.
    """
    if type(obj) == dict and obj.get('class') == 'PScLine':
        line_type = PScLineType[obj['type']]
        name = obj.get('name')
        text = obj.get('text')

        line = PScLine(line_type, name=name, text=text)
        return line
    else:
        return obj


def _psc_hook(obj):
    """Decode any dict contained in encoded PSc object.
    """
    hooks = [_psc_dict_hook, _psc_line_dict_hook]
    for hook in hooks:
        obj = hook(obj)
    return obj


def psc_load(fp, object_hook=_psc_hook, **kwargs):
    """JSON ファイルをデシリアライズして台本オブジェクトを生成する

    Parameters
    ----------
    fp : file-like
        JSON ファイル (ストリーム)
    object_hook : function
        デコードに使うフック関数
    **kwargs
        json.load に渡すキーワード引数

    Returns
    -------
    台本オブジェクト : PSc
    """
    kwargs['object_hook'] = object_hook
    return json.load(fp, **kwargs)


def psc_loads(s, object_hook=_psc_hook, **kwargs):
    """JSON 文字列をデシリアライズして台本オブジェクトを生成する

    Parameters
    ----------
    s : str
        JSON 文字列
    object_hook : function
        デコードに使うフック関数
    **kwargs
        json.loads に渡すキーワード引数

    Returns
    -------
    台本オブジェクト : PSc
    """
    kwargs['object_hook'] = object_hook
    return json.loads(s, **kwargs)
