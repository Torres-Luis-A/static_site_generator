import os

from generate_page import generate_page


def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    for filename in os.listdir(content_dir_path):
        full_path = os.path.join(content_dir_path, filename)  # build full path once
        if os.path.isfile(full_path) and filename.endswith('.md'):
            dest_path = os.path.join(dest_dir_path, filename[:-3] + '.html')
            generate_page(full_path, template_path, dest_path)
        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, os.path.join(dest_dir_path, filename))