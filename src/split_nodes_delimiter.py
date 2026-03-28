
from textnode import TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node['type'] != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node['text']:
            raise ValueError(f"Delimiter '{delimiter}' not found in text: {node['text']}")
        parts = node['text'].split(delimiter)
        for i, part in enumerate(parts):
            if part:
                new_nodes.append({'text': part, 'type': text_type})
            if i < len(parts) - 1:
                new_nodes.append({'text': delimiter, 'type': TextType.TEXT})
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node['type'] != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node['text'])
        if not images:
            new_nodes.append(node)
            continue
        text = node['text']
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            if image_markdown in text:
                parts = text.split(image_markdown)
                for i, part in enumerate(parts):
                    if part:
                        new_nodes.append({'text': part, 'type': TextType.TEXT})
                    if i < len(parts) - 1:
                        new_nodes.append({'text': alt_text, 'type': TextType.IMAGE, 'url': url})
                break
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node['type'] != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node['text'])
        if not links:
            new_nodes.append(node)
            continue
        text = node['text']
        for link_text, url in links:
            link_markdown = f"[{link_text}]({url})"
            if link_markdown in text:
                parts = text.split(link_markdown)
                for i, part in enumerate(parts):
                    if part:
                        new_nodes.append({'text': part, 'type': TextType.TEXT})
                    if i < len(parts) - 1:
                        new_nodes.append({'text': link_text, 'type': TextType.LINK, 'url': url})
                break
    return new_nodes