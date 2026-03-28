import unittest


from markdown_to_blocks import markdown_to_blocks
from textnode import TextType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# Heading 1\n\n## Heading 2\n\n### Heading 3\n\n- List item 1\n- List item 2\n\nParagraph text."
        expected = [
            {'type': 'heading1', 'content': [{'text': 'Heading 1', 'type': TextType.TEXT}]},
            {'type': 'heading2', 'content': [{'text': 'Heading 2', 'type': TextType.TEXT}]},
            {'type': 'heading3', 'content': [{'text': 'Heading 3', 'type': TextType.TEXT}]},
            {'type': 'list_item', 'content': [{'text': 'List item 1', 'type': TextType.TEXT}]},
            {'type': 'list_item', 'content': [{'text': 'List item 2', 'type': TextType.TEXT}]},
            {'type': 'paragraph', 'content': [{'text': 'Paragraph text.', 'type': TextType.TEXT}]}
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

        def test_markdown_to_blocks_with_images_and_links(self):
            markdown = "This is a paragraph with an image ![alt text](https://example.com/image.png) and a link [Google](https://www.google.com)."
            expected = [
                {'type': 'paragraph', 'content': [
                    {'text': 'This is a paragraph with an image ', 'type': TextType.TEXT},
                    {'text': 'alt text', 'type': TextType.IMAGE, 'url': 'https://example.com/image.png'},
                    {'text': ' and a link ', 'type': TextType.TEXT},
                    {'text': 'Google', 'type': TextType.LINK, 'url': 'https://www.google.com'}
                ]}
            ]
            result = markdown_to_blocks(markdown)
            self.assertEqual(result, expected)
