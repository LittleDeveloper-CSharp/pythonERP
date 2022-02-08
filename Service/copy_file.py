import os
from shutil import copyfile


def copy_file(source_path, final_path, name_file=None):
    if name_file is not None:
        final_path = final_path + name_file
    path_module = os.path.abspath(__file__).split('\\')
    path_module = '\\'.join(path_module[0:(len(path_module) - 1)])

    full_path = os.path.join(path_module, final_path)

    path = os.path.abspath(full_path)
    copyfile(source_path, path)
