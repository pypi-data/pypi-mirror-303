import unittest
import json

from playscript import PScLineType, PScLine, PSc
from playscript.conv.json import psc_dumps, psc_loads


class TestEncoder(unittest.TestCase):
    """Testing if PSc object is encoded properly
    """
    def test_encode_play_sc(self):
        lines = []

        lines.append(PScLine(
            line_type=PScLineType.TITLE,
            text='タイトル'))

        lines.append(PScLine(
            line_type=PScLineType.AUTHOR,
            text='著者名'))

        lines.append(PScLine(
            line_type=PScLineType.CHARSHEADLINE,
            text='登場人物'))

        lines.append(PScLine(
            line_type=PScLineType.CHARACTER,
            name='キャラクタ'))

        lines.append(PScLine(
            line_type=PScLineType.H1,
            text='柱'))

        lines.append(PScLine(
            line_type=PScLineType.DIRECTION,
            text='ト書き'
        ))

        lines.append(PScLine(
            line_type=PScLineType.DIALOGUE,
            name='名前',
            text='セリフ'
        ))

        psc = PSc.from_lines(lines)
        s = psc_dumps(psc)

        sc_dict = {
            "class": "PSc",
            "title": "",
            "author": "",
            "chars": [],
            "lines": [
                {"class": "PScLine", "type": "TITLE", "text": "タイトル"},
                {"class": "PScLine", "type": "AUTHOR", "text": "著者名"},
                {"class": "PScLine", "type": "CHARSHEADLINE",
                    "text": "登場人物"},
                {"class": "PScLine", "type": "CHARACTER",
                    "name": "キャラクタ"},
                {"class": "PScLine", "type": "H1", "text": "柱"},
                {"class": "PScLine", "type": "DIRECTION", "text": "ト書き"},
                {"class": "PScLine", "type": "DIALOGUE", "name": "名前",
                    "text": "セリフ"}
            ]
        }
        sc_str = json.dumps(sc_dict, ensure_ascii=False)
        self.assertEqual(s, sc_str)


class TestDecoder(unittest.TestCase):
    """Testing if PSc object is decoded properly
    """
    def test_decode_play_sc(self):
        sc_dict = {
            "class": "PSc",
            "title": "",
            "author": "",
            "chars": [],
            "lines": [
                {"class": "PScLine", "type": "TITLE", "text": "タイトル"},
                {"class": "PScLine", "type": "AUTHOR", "text": "著者名"},
                {"class": "PScLine", "type": "CHARSHEADLINE",
                    "text": "登場人物"},
                {"class": "PScLine", "type": "CHARACTER",
                    "name": "キャラクタ"},
                {"class": "PScLine", "type": "H1", "text": "柱"},
                {"class": "PScLine", "type": "DIRECTION", "text": "ト書き"},
                {"class": "PScLine", "type": "DIALOGUE", "name": "名前",
                    "text": "セリフ"}
            ]
        }
        sc_str = json.dumps(sc_dict, ensure_ascii=False)

        psc = psc_loads(sc_str)

        self.assertIsInstance(psc, PSc)
        self.assertEqual(psc.title, '')
        self.assertEqual(psc.author, '')
        self.assertEqual(psc.chars, [])
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
