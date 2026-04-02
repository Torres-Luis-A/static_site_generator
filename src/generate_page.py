
import os

from textnode import TextNode, TextType, text_node_to_html_node
from markdown_to_blocks import markdown_to_html_node 
from htmlnode import ParentNode


def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No title found in markdown")
        
def generate_page(from_path, template_path, dest_path,basepath):
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, 'r') as f:
        markdown = f.read()
    with open(template_path, 'r') as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    markdown_to_html = html_node.to_html()
    title = extract_title(markdown)
    html = (template
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", markdown_to_html)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )
    with open(dest_path, 'w') as f:
        f.write(html)
    
    
        