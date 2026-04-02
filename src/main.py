import os
import shutil

from copy_static import copy_static_to_public
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_to_public(dir_path_static, dir_path_public)
    print("Generating pages...")
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content", "./template.html", "./public")






main()
