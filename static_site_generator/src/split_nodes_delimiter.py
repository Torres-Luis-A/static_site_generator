
from textnode import TextType

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

