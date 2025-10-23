import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdowntoHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph
This is the same paragraph with an ![image](http://www.google.com)

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph\nThis is the same paragraph with an ![image](http://www.google.com)",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_type_heading(self):
        block = block_to_block_type("""### This is a block with heading""")
        self.assertEqual(BlockType.HEADING, block)

    def test_block_type_code(self):
        block = block_to_block_type("""```\nthis is a code block test\n```""")
        self.assertEqual(BlockType.CODE, block)

    def test_block_type_quote(self):
        block = block_to_block_type(""">this is a quote test
>this is another quote line""")
        self.assertEqual(BlockType.QUOTE, block)

    def test_block_type_unordered(self):
        block = block_to_block_type("""- this is an unordered list
- this is part of the unordered list""")
        self.assertEqual(BlockType.UNORDERED_LIST, block)

    def test_block_type_ordered(self):
        block = block_to_block_type("""1. this is an ordered list
2. this is another part of the ordered list""")
        self.assertEqual(BlockType.ORDERED_LIST, block)

    def test_block_type_paragraph(self):
        block = block_to_block_type("""This is a normal paragraph""")
        self.assertEqual(BlockType.PARAGRAPH, block)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()