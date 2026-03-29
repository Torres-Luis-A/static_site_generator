import unittest

from markdown_to_blocks import block_to_block_type, markdown_to_blocks, BlockType, markdown_to_html_node
from textnode import TextNode, TextType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = "# Heading 1\n\n## Heading 2\n\n### Heading 3\n\n- List item 1\n- List item 2\n\nParagraph text."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(len(html_node.children), 5)  # h1, h2, h3, ul, p

    def test_markdown_to_html_node_with_images_and_links(self):
        markdown = "This is a paragraph with an image ![alt text](https://example.com/image.png) and a link [Google](https://www.google.com)."
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.tag, "div")
        self.assertEqual(len(html_node.children), 1)
        paragraph_node = html_node.children[0]
        self.assertEqual(paragraph_node.tag, "p")
        self.assertEqual(len(paragraph_node.children), 5)  # text, img, text, a, trailing "."