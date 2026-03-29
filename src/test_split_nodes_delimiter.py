import unittest
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [TextNode('Hello, world!', TextType.TEXT)]
        delimiter = ','
        text_type = TextType.BOLD
        expected = [
            TextNode('Hello', TextType.TEXT),
            TextNode(' world!', TextType.BOLD),
        ]
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_no_delimiter(self):
        old_nodes = [TextNode('Hello world!', TextType.TEXT)]
        delimiter = ';'
        text_type = TextType.BOLD
        # should just pass through unchanged, no error
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_image(self):
        old_nodes = [TextNode('This is an image: ![alt text](https://example.com/image.png)', TextType.TEXT)]
        expected = [
            TextNode('This is an image: ', TextType.TEXT),
            TextNode('alt text', TextType.IMAGE, 'https://example.com/image.png')
        ]
        result = split_nodes_image(old_nodes)
        self.assertEqual(result, expected)

    def test_split_nodes_link(self):
        old_nodes = [TextNode('This is a link: [Google](https://www.google.com)', TextType.TEXT)]
        expected = [
            TextNode('This is a link: ', TextType.TEXT),
            TextNode('Google', TextType.LINK, 'https://www.google.com')
        ]
        result = split_nodes_link(old_nodes)
        self.assertEqual(result, expected)