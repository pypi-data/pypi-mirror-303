import textwrap
import unittest

from playscript import PScLineType, PScLine, PSc
from playscript.conv.fountain import psc_from_fountain


class TestParser(unittest.TestCase):
    """Testing if string is parsed as fountain properly
    """
    def test_parse(self):
        s = textwrap.dedent('''\
            Title: タイトル
            Author: 著者名

            # 登場人物

            キャラクタ

            # 柱

            ト書き

            @名前
            セリフ

            > エンドマーク
        ''')

        psc = psc_from_fountain(s)

        self.assertIsInstance(psc, PSc)
        self.assertEqual(psc.title, 'タイトル')
        self.assertEqual(psc.author, '著者名')
        self.assertEqual(psc.chars, ['名前'])
        self.assertIsInstance(psc.lines, list)

        lines = psc.lines

        self.assertIsInstance(lines[0], PScLine)
        self.assertEqual(lines[0].type, PScLineType.TITLE)
        self.assertEqual(lines[0].text, 'タイトル')

        self.assertIsInstance(lines[1], PScLine)
        self.assertEqual(lines[1].type, PScLineType.AUTHOR)
        self.assertEqual(lines[1].text, '著者名')

        self.assertIsInstance(lines[2], PScLine)
        self.assertEqual(lines[2].type, PScLineType.CHARSHEADLINE)
        self.assertEqual(lines[2].text, '登場人物')

        self.assertIsInstance(lines[3], PScLine)
        self.assertEqual(lines[3].type, PScLineType.CHARACTER)
        self.assertEqual(lines[3].name, 'キャラクタ')

        self.assertIsInstance(lines[4], PScLine)
        self.assertEqual(lines[4].type, PScLineType.H1)
        self.assertEqual(lines[4].text, '柱')

        self.assertIsInstance(lines[5], PScLine)
        self.assertEqual(lines[5].type, PScLineType.DIRECTION)
        self.assertEqual(lines[5].text, 'ト書き')

        self.assertIsInstance(lines[6], PScLine)
        self.assertEqual(lines[6].type, PScLineType.DIALOGUE)
        self.assertEqual(lines[6].name, '名前')
        self.assertEqual(lines[6].text, 'セリフ')

        self.assertIsInstance(lines[7], PScLine)
        self.assertEqual(lines[7].type, PScLineType.ENDMARK)
        self.assertEqual(lines[7].text, 'エンドマーク')
