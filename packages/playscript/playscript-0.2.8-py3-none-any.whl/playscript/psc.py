"""台本オブジェクトを構成するクラス群
"""
import re
import warnings
from enum import Enum


class PScLineType(Enum):
    """台本行の種類
    """
    TITLE = 0                   # Title
    AUTHOR = 1                  # Author name
    CHARSHEADLINE = 2           # Headline of character list
    CHARACTER = 3               # Character
    H1 = 4                      # Headline of scene (level 1)
    H2 = 5                      # Headline of scene (level 2)
    H3 = 6                      # Headline of scene (level 3)
    DIRECTION = 7               # Direction
    DIALOGUE = 8                # Dialogue
    ENDMARK = 9                 # End mark
    COMMENT = 10                # Comment
    EMPTY = 11                  # Empty line
    CHARACTER_CONTINUED = 12    # Following lines of Character
    DIRECTION_CONTINUED = 13    # Following lines of Direction
    DIALOGUE_CONTINUED = 14     # Following lines of Dialogue
    COMMENT_CONTINUED = 15      # Foloowing lines of Comment


class PScLine:
    """台本行クラス
    """
    # Opening and closing brackets for text in dialogue lines.
    # More than one characters can be set and matched as each.
    # In addition, space character is used as name-text delimiter implicitly.
    _dlg_brackets = ('「', '」')

    def __init__(self, line_type, name=None, text=None):
        """コンストラクタ

        Parameters
        ----------
        line_type : PScLineType
            行の種類
        name : str
            登場人物行、セリフ行の名前部分
        text : str
            テキスト部分
        """
        try:
            self.type = PScLineType(line_type)
        except ValueError:
            raise TypeError(
                "Argument 'line_type' should be a PScLineType member.")

        # 登場人物行またはセリフ行なら、name 属性が必須
        if self.type in (PScLineType.CHARACTER, PScLineType.DIALOGUE):
            if not name:
                raise ValueError(
                    "Argument 'name' is required "
                    "for type CHARACTER or DIALOGUE.")

        # 空行でも登場人物行でもなければ、text 属性が必須
        if self.type not in (PScLineType.EMPTY, PScLineType.CHARACTER):
            if not text:
                raise ValueError(
                    "Argument 'text' is required "
                    "for the other types than EMPTY or CHARACTER.")

        if name:
            self.name = name
        if text:
            self.text = text

    @classmethod
    def from_text(cls, line_type, text, *, default_name='*',
                  dlg_brackets=None):
        """行の種類と文字列から、台本行オブジェクトを作る

        Parameters
        ----------
        line_type : PScLineType
            行の種類
        text : str
            行を表す文字列
        default_name : str
            名前部分を切り出せない場合に使う名前
        dlg_brackets : list-like[str]
            開き括弧とみなす文字と、閉じ括弧とみなす文字

        Returns
        -------
        台本行オブジェクト : PScLine
        """
        # Delimiter of name and text in character lines.
        # (Colon or space followed by extra spaces.)
        chr_delimiter = re.compile(r'[:\s]\s*')

        if not dlg_brackets:
            dlg_brackets = cls._dlg_brackets

        # Delimiter of name and text in dialogue lines.
        # (Bracket or space following extra spaces.)
        dlg_delimiter = re.compile(f'\\s*[\\s{dlg_brackets[0]}]')

        text = text.strip()

        if line_type == PScLineType.CHARACTER:
            # Split text to name and text.
            if not chr_delimiter.search(text):
                name, text = text, ''
            else:
                name, text = chr_delimiter.split(text, maxsplit=1)
            return cls(line_type, name=name, text=text)

        if line_type == PScLineType.DIALOGUE:
            name = ''
            # Split text to name and text.
            if dlg_delimiter.search(text):
                name, text = dlg_delimiter.split(text, maxsplit=1)

            if not name:
                name = default_name

            # Remove closing bracket at end.
            if text[-1] in dlg_brackets[1]:
                text = text[:-1]

            return cls(line_type, name=name, text=text)

        # TODO: line_type が数字や文字列だった場合に対応する？

        return cls(line_type, text=text)

    def __str__(self):
        attrs = [self.type.name]
        if hasattr(self, 'name'):
            attrs.append(repr(self.name))
        if hasattr(self, 'text'):
            attrs.append(repr(self.text))
        attrs_str = ', '.join(attrs)
        return f'{type(self).__name__}({attrs_str})'


class PSc:
    """台本クラス
    """
    def __init__(self, title='', author='', chars=[], lines=[]):
        """コンストラクタ

        Parameters
        ----------
        title : str
            題名
        author : str
            著者名
        chars : list-like[str]
            登場人物のリスト
        lines : list-like[PScLine]
            台本行オブジェクトのリスト (イテラブル)
        """
        self.title = title
        self.author = author
        self.chars = chars
        # lines could be a generator while self.lines should be a list.
        self.lines = list(lines)

    @classmethod
    def from_lines(cls, lines):
        """台本行オブジェクトのリストから台本オブジェクトを作る

        Parameters
        ----------
        lines : list-like[PScLine]
            台本行オブジェクトのリスト (イテラブル)

        Returns
        -------
        台本オブジェクト : PSc
        """
        return cls(lines=lines)

    @classmethod
    def lines_from_types_and_texts(cls, line_types, texts):
        """行の種類と文字列から、台本行オブジェクトのリストを作る

        このメソッドは非推奨です。
        代わりに `lines_from_types_and_texts` 関数を使ってください。
        """
        msg = "`PSc.lines_from_types_and_texts` is deprecated. " \
            "Use the bare function `lines_from_types_and_texts` instead."
        warnings.warn(msg, DeprecationWarning, stacklevel=2)

        return lines_from_types_and_texts(line_types, texts)


def lines_from_types_and_texts(line_types, texts):
    """行の種類と文字列から、台本行オブジェクトのリストを作る

    Parameters
    ----------
    line_types : list-like[PScLineType]
        行の種類のリスト (イテラブル)
    texts : list-like[str]
        行のテキストのリスト (イテラブル)

    Returns
    -------
    台本行オブジェクトのリスト : list[PScLine]
    """
    lines = []
    for line_type, text in zip(line_types, texts):
        line = PScLine.from_text(line_type, text)
        lines.append(line)
    return lines
