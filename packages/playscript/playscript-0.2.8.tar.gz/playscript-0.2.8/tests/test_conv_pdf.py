import unittest

from playscript.conv.pdf import _get_h2_letter


class TestH2Letter(unittest.TestCase):
    """柱 (レベル2) につく文字の生成のテスト
    """
    def test_h2_letter(self):
        self.assertEqual(_get_h2_letter(0), '')
        self.assertEqual(_get_h2_letter(1), 'A')
        self.assertEqual(_get_h2_letter(26), 'Z')
        self.assertEqual(_get_h2_letter(27), 'AA')
        self.assertEqual(_get_h2_letter(52), 'AZ')
        self.assertEqual(_get_h2_letter(677), 'ZA')
        self.assertEqual(_get_h2_letter(702), 'ZZ')
        self.assertEqual(_get_h2_letter(703), 'AAA')
