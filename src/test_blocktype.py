import unittest

from blocktype import BlockType, block_to_block_type


class TestBlocktype(unittest.TestCase):
    def test_para(self):
        text = "this is just basic text with ` some ``` symbols in here"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(text),expected)

    def test_code(self):
        text = "``` symbols in here ```"
        expected = BlockType.CODE
        self.assertEqual(block_to_block_type(text),expected)

    def test_quote(self):
        text = "> symbols in here \n> dsfwwaa"
        expected = BlockType.QUOTE
        self.assertEqual(block_to_block_type(text),expected)

    def test_heading(self):
        text = "### dfgdaa ```"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(text),expected)

    def test_unordered(self):
        text = "- asdaae \n- asdacc -- \n- a"
        expected = BlockType.UNLIST
        self.assertEqual(block_to_block_type(text),expected)

    def test_list(self):
        text = "1. sdfff\n2. aaaa\n3. asttg"
        expected = BlockType.LIST
        self.assertEqual(block_to_block_type(text),expected)

 
if __name__ == "__main__":
    unittest.main()
