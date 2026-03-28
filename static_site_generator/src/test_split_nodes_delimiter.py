import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            {'text': 'Hello, world!', 'type': TextType.TEXT},
            {'text': 'This is a test.', 'type': TextType.TEXT}
        ]
        delimiter = ','
        text_type = TextType.BOLD
        expected = [
            {'text': 'Hello', 'type': TextType.BOLD},
            {'text': ',', 'type': TextType.TEXT},
            {'text': ' world!', 'type': TextType.BOLD},
            {'text': 'This is a test.', 'type': TextType.TEXT}
        ]
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_no_delimiter(self):
        old_nodes = [
            {'text': 'Hello, world!', 'type': TextType.TEXT}
        ]
        delimiter = ';'
        text_type = TextType.BOLD
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, delimiter, text_type)