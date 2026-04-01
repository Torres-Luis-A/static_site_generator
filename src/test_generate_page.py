import unittest


from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title\n\nThis is some content."
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")

    def test_extract_title_with_space(self):
        markdown = "# This is a title with space\n\nThis is some content."
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title with space")

    def test_extract_title_with_no_title(self):
        markdown = "This is some content without a title."
        with self.assertRaises(ValueError):
            extract_title(markdown)