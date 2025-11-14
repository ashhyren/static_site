import unittest

from extract import extract_title

class TestTextNode(unittest.TestCase):
    def test_title(self):
        md = """
# This is a header
"""

        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a header",
        )

if __name__ == "__main__":
    unittest.main()