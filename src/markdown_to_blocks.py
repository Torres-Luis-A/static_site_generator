from zmq import Enum

from tex_to_nodes import tex_to_nodes
from textnode import TextType
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from extract_markdown_images import extract_markdown_images, extract_markdown_links


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split('\n')
    for line in lines:
        line = line.strip()
        if not line:          # skip blank lines
            continue
        if line.startswith('### '):
            blocks.append({'type': 'heading3', 'content': tex_to_nodes(line[4:])})
        elif line.startswith('## '):
            blocks.append({'type': 'heading2', 'content': tex_to_nodes(line[3:])})
        elif line.startswith('# '):
            blocks.append({'type': 'heading1', 'content': tex_to_nodes(line[2:])})
        elif line.startswith('- '):
            blocks.append({'type': 'list_item', 'content': tex_to_nodes(line[2:])})
        else:
            blocks.append({'type': 'paragraph', 'content': tex_to_nodes(line)})
    return blocks
