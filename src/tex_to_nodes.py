

from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from extract_markdown_images import extract_markdown_images, extract_markdown_links
from textnode import TextType

def tex_to_nodes(tex):
    nodes = [{'text': tex, 'type': TextType.TEXT}]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes