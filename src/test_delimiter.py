import unittest

from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode(
            "This is text with a **bold block** word", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ],
        )

    def test_text(self):
        node = TextNode(
            "This is text with text", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter([node], None, TextType.TEXT),
            [
                TextNode("This is text with text", TextType.TEXT)
            ],
        )

    def test_italic(self):
        node = TextNode(
            "_italic block_ word", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter([node], "_", TextType.ITALIC),
            [
                TextNode("italic block", TextType.ITALIC),
                TextNode(" word", TextType.TEXT)
            ],
        )

    def test_multiple(self):
        node = TextNode(
            "This is a text with **multiple** bolded **statements**", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("This is a text with ", TextType.TEXT),
                TextNode("multiple", TextType.BOLD),
                TextNode(" bolded ", TextType.TEXT),
                TextNode("statements", TextType.BOLD)
            ],
        )

    def test_multiples_2(self):
        node = [
            TextNode(
            "This is a statement with _italic text_", TextType.TEXT
            ),
            TextNode(
            "This is a _statement_ with italic text", TextType.TEXT
            ),
            TextNode(
            "This is a statement with _italic_ text", TextType.TEXT
            )
        ]
        self.assertEqual(
            split_nodes_delimiter(node, "_", TextType.ITALIC),
            [
                TextNode("This is a statement with ", TextType.TEXT),
                TextNode("italic text", TextType.ITALIC),
                TextNode("This is a ", TextType.TEXT),
                TextNode("statement", TextType.ITALIC),
                TextNode(" with italic text", TextType.TEXT),
                TextNode("This is a statement with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT)
            ],
        )

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()