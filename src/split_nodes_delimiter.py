from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            new_nodes.append(node)  # no delimiter? just pass through
            continue
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            if part:
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        text = node.text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            if image_markdown in text:
                parts = text.split(image_markdown, 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                text = parts[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        text = node.text
        for link_text, url in links:
            link_markdown = f"[{link_text}]({url})"
            if link_markdown in text:
                parts = text.split(link_markdown, 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                text = parts[1]
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes