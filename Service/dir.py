import os

__source_path = "../Resources/"


def create_image_dir(dir_name):
    os.mkdir(__source_path+"/image/"+dir_name)


def create_doc_dir(dir_name):
    os.mkdir(__source_path+"/docs/"+dir_name)


def rename_dir(dir_name, new_dir_name):
    os.renames(dir_name, new_dir_name)


def get_dir():
    return os.getcwd()
