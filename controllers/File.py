import os, os.path
from shutil import copyfile, copy, rmtree
import string
import random

class FileController:

    def __init__(self, allowed_files):
        self.allowed_files = allowed_files

    @staticmethod
    def create_directory(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def get_dir_contents(path):
        return os.listdir(path)

    @staticmethod
    def count_directory(path):
        return len(os.listdir(path))

    @staticmethod
    def copy_file(src, dst):
        copyfile(src, dst)

    @staticmethod
    def copy_directory(src, dst):
        copy(src, dst)

    @staticmethod
    def get_file_ext(filename):
        if '.' in filename:
            return filename.rsplit('.', 1)[1].lower()
        return ''

    def is_file_allowed(self, filename):
        return self.get_file_ext(filename) in self.allowed_files

    @staticmethod
    def gen_rand_string(n=3, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(n))

    @staticmethod
    def create_file_name(filename):
        arr = filename.rsplit('.', 1)
        arr[0] = arr[0] + '-' + FileController.gen_rand_string(3)
        return '.'.join(arr)

    @staticmethod
    def remove_file(root_path, file_path):
        real_root = os.path.realpath(root_path)
        real_path = os.path.realpath(os.path.join(real_root, file_path))
        if not real_path.startswith(os.path.join(real_root, 'static')):
            return False  # don't allow malicious users to delete arbitrary files
        os.remove(real_path)
        name, ext = os.path.splitext(real_path)
        if ext == '.ppt' or ext == '.pdf':
            # remove the corresponding zip and directory
            os.remove(name + '.zip')
            rmtree(name)
        return True



