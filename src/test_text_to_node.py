import unittest

from tex_to_nodes import tex_to_nodes
from textnode import TextType

class TestTexToNodes(unittest.TestCase):
    def test_tex_to_nodes(self):
        tex = "This is a link: [Google](https://www.google.com) and an image: ![alt text](https://example.com/image.png)"
        expected = [
            {'text': 'This is a link: ', 'type': TextType.TEXT},
            {'text': 'Google', 'type': TextType.LINK, 'url': 'https://www.google.com'},
            {'text': ' and an image: ', 'type': TextType.TEXT},
            {'text': 'alt text', 'type': TextType.IMAGE, 'url': 'https://example.com/image.png'}
        ]
        result = tex_to_nodes(tex)
        self.assertEqual(result, expected)

    def test_tex_to_nodes_no_links_or_images(self):
        tex = "This is just plain text."
        expected = [
            {'text': 'This is just plain text.', 'type': TextType.TEXT}
        ]
        result = tex_to_nodes(tex)
        self.assertEqual(result, expected)
    
    def test_tex_to_nodes_only_links(self):
        tex = "This is a link: [Google](https://www.google.com)"
        expected = [
            {'text': 'This is a link: ', 'type': TextType.TEXT},
            {'text': 'Google', 'type': TextType.LINK, 'url': 'https://www.google.com'}
        ]
        result = tex_to_nodes(tex)
        self.assertEqual(result, expected)

        