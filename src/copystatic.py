#copystatic.py
import os
import shutil

def move_content(source_dir = "static", destination_dir = "public"):
    source_path = os.path.abspath(source_dir)
    destination_path = os.path.abspath(destination_dir)
    if not os.path.exists(source_path):
        raise NotADirectoryError(f"Directory to copy does not exist!")
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    shutil.rmtree(destination_path)
    os.mkdir(destination_path)
    copy_recursion(source_path, destination_path)

def copy_recursion(source, destination):
    file_list = os.listdir(source)
    for file_path in file_list:
        path = os.path.join(source, file_path)
        if os.path.isfile(path):
            shutil.copy(path, destination)
        elif os.path.isdir(path):
            new_destination = os.path.join(destination, file_path)
            if not os.path.exists(new_destination):
                os.mkdir(new_destination)
            copy_recursion(path, new_destination)