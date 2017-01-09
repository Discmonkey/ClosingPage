import requests
import time
import zipfile
from controllers.File import FileController
import os

class ConvertApi:

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

    def convert_and_extract(self, filename, relative_path, base_path):
        # convert to zip file, filename - no extension + .zip

        file_path = os.path.join(base_path, relative_path, filename.rsplit('.', 1)[0])

        self.convert_powerpoint(file_path + '.ppt', file_path + '.zip')
        FileController.create_directory(file_path)
        self.extract_images(file_path + '.zip', file_path)

        num_images = FileController.count_directory(file_path)
        return_arr = []

        for i in range(1, num_images + 1):
            return_arr.append(os.path.join(relative_path, 'file_page') + str(i))

        return return_arr







if __name__ == '__main__':
    ca = ConvertApi()
    t1 = time.time()
    ca.convert_powerpoint('a', 'b')

    print(time.time() - t1)
