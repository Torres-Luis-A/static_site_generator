
from text_to_nodes import text_to_textnodes


def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('#'):
            return line[1:].strip()
        if line.startswith('# '):
            return line[2:].strip()
        else:
            raise ValueError("No title found in markdown")
        
def generate_page(from_path, template_path, to_path):
    print(f"Generating page from {from_path} to {to_path} using template {template_path}")
    with open(from_path, 'r') as f:
        markdown = f.read()
    with open(template_path, 'r') as f:
        template = f.read()
    
        