from shutil import copyfile


def copy_file(source_path, final_path, name_file=None):
    if name_file is not None:
        final_path = final_path + name_file
    copyfile(source_path, final_path)
