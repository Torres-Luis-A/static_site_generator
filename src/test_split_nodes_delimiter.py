import unittest

from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            {'text': 'Hello, world!', 'type': TextType.TEXT},

        ]
        delimiter = ','
        text_type = TextType.BOLD
        expected = [
            {'text': 'Hello', 'type': TextType.BOLD},
            {'text': ',', 'type': TextType.TEXT},
            {'text': ' world!', 'type': TextType.BOLD},

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

    def test_split_nodes_image(self):
        old_nodes = [
            {'text': 'This is an image: ![alt text](https://example.com/image.png)', 'type': TextType.TEXT}
        ]
        expected = [
            {'text': 'This is an image: ', 'type': TextType.TEXT},
            {'text': 'alt text', 'type': TextType.IMAGE, 'url': 'https://example.com/image.png'}
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, expected)
    
    def test_split_nodes_link(self):
        old_nodes = [
            {'text': 'This is a link: [Google](https://www.google.com)', 'type': TextType.TEXT}
        ]
        expected = [
            {'text': 'This is a link: ', 'type': TextType.TEXT},
            {'text': 'Google', 'type': TextType.LINK, 'url': 'https://www.google.com'}
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, expected)
    