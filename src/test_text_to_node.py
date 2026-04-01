import unittest

from text_to_nodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTexToNodes(unittest.TestCase):
    def test_tex_to_nodes(self):
        tex = "This is a link: [Google](https://www.google.com) and an image: ![alt text](https://example.com/image.png)"
        expected = [
            TextNode('This is a link: ', TextType.TEXT),
            TextNode('Google', TextType.LINK, 'https://www.google.com'),
            TextNode(' and an image: ', TextType.TEXT),
            TextNode('alt text', TextType.IMAGE, 'https://example.com/image.png')
        ]
        result = text_to_textnodes(tex)
        self.assertEqual(result, expected)

    def test_tex_to_nodes_no_links_or_images(self):
        tex = "This is just plain text."
        expected = [
            TextNode('This is just plain text.', TextType.TEXT)
        ]
        result = text_to_textnodes(tex)
        self.assertEqual(result, expected)

    def test_tex_to_nodes_only_links(self):
        tex = "This is a link: [Google](https://www.google.com)"
        expected = [
            TextNode('This is a link: ', TextType.TEXT),
            TextNode('Google', TextType.LINK, 'https://www.google.com')
        ]
        result = text_to_textnodes(tex)
        self.assertEqual(result, expected)