import os
import shutil
import sys

from copy_static import copy_static_to_public
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
default_basepath = "/"




def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_to_public(dir_path_static, dir_path_public)
    print("Generating pages...")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)






main()
