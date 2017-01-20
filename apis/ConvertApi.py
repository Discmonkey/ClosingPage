import requests
import time
import zipfile
from controllers.File import FileController
import os

class ConvertApi:

    def convert_pdf(self, path_to_file, target_path):

        request_url = 'https://do.convertapi.com/Pdf2Image'

        form_data = {
            'ApiKey': '686241460',
            'AlternativeParser': False,
            'OutputFormat': 'jpg',
            'JpgQuality': 10,
            'StoreFile': False,
            'Timeout': 10
        }
        with open(path_to_file, 'rb') as file_stream:
            files = {'file': file_stream}

            res = requests.post(request_url, data=form_data, files=files)
            print(res.status_code)
            with open(target_path, 'wb') as fd:
                for chunk in res.iter_content(chunk_size=128):
                    fd.write(chunk)

    def convert_powerpoint(self, path_to_file, target_path):
        request_url = 'https://do.convertapi.com/PowerPoint2Image'

        form_data = {
            'ApiKey': '686241460',
            'AlternativeParser': False,
            'OutputFormat': 'jpg',
            'JpgQuality': 10,
            'StoreFile': False,
            'Timeout': 10
        }
        with open(path_to_file, 'rb') as file_stream:
            files = {'file': file_stream}

            res = requests.post(request_url, data=form_data, files=files)
            print(res.status_code)
            with open(target_path, 'wb') as fd:
                for chunk in res.iter_content(chunk_size=128):
                    fd.write(chunk)

    def extract_images(self, extract_path, target_path):
        with zipfile.ZipFile(extract_path) as z:
            z.extractall(target_path)

    def convert_and_extract(self, filename, relative_path, base_path, file_type):
        # convert to zip file, filename - no extension + .zip
        file_no_ext = filename.rsplit('.', 1)[0]
        file_path = os.path.join(base_path, relative_path, file_no_ext)

        if file_type == 'ppt':
            self.convert_powerpoint(file_path + '.ppt', file_path + '.zip')
        elif file_type == 'pdf':
            self.convert_pdf(file_path + '.pdf', file_path + '.zip')

        FileController.create_directory(file_path)
        self.extract_images(file_path + '.zip', file_path)

        return list(map(lambda x: os.path.join(relative_path, file_no_ext, x),
                        FileController.get_dir_contents(file_path)))

if __name__ == '__main__':
    ca = ConvertApi()
    t1 = time.time()
    ca.convert_powerpoint('a', 'b')

    print(time.time() - t1)
