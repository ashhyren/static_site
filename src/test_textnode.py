import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_n_eq(self):
        node = ("This is a text node", TextType.ITALIC, "http://www.boot.dev")
        node2 = ("This is a text node", TextType.LINK, "http://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq1(self):
        node=TextNode("Test",TextType.IMAGE)
        node2=TextNode("Test",TextType.IMAGE, None)
        self.assertEqual(node,node2)


if __name__ == "__main__":
    unittest.main()