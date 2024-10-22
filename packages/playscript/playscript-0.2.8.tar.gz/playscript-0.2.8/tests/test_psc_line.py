import unittest

from playscript import PScLineType, PScLine


class TestCharacterLine(unittest.TestCase):
    '''Testing if CHARACTER line is created properly
    '''
    def test_from_text(self):
        line_type = PScLineType.CHARACTER

        text = '名前 説明'
        line = PScLine.from_text(line_type, text)
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, '説明')

        text = '名前　説明'
        line = PScLine.from_text(line_type, text)
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, '説明')

        text = '名前\t説明'
        line = PScLine.from_text(line_type, text)
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, '説明')


class TestDialogueLine(unittest.TestCase):
    '''Testing if DIALOGUE line is created properly
    '''
    def test_from_text(self):
        line_type = PScLineType.DIALOGUE

        text = '名前 セリフ'
        line = PScLine.from_text(line_type, text)
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, 'セリフ')

        text = '名前「セリフ」'
        line = PScLine.from_text(line_type, text)
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, 'セリフ')

        text = '名前 「セリフ」'
        line = PScLine.from_text(line_type, text)
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, 'セリフ')

        text = '名前「セリフ'
        line = PScLine.from_text(line_type, text)
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, 'セリフ')

        text = 'セリフ'
        line = PScLine.from_text(line_type, text, default_name='名前')
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, 'セリフ')

        text = '「セリフ」'
        line = PScLine.from_text(line_type, text, default_name='名前')
        self.assertEqual(line.name, '名前')
        self.assertEqual(line.text, 'セリフ')
