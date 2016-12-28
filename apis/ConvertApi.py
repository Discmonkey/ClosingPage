import requests
import time
import zipfile

class ConvertApi:

    def convert_powerpoint(self, file_stream, file_path_to):
        request_url = 'https://do.convertapi.com/PowerPoint2Image'

        form_data = {
            'ApiKey': '686241460',
            'AlternativeParser': False,
            'OutputFormat': 'jpg',
            'JpgQuality': 20,
            'StoreFile': False,
            'Timeout': 10
        }

        filename = '/Users/maxg/PycharmProjects/ClosingPage/static/img/phase-one/test.zip'
        files = {'file': file_stream}

        res = requests.post(request_url, data=form_data, files=files)
        print(res.status_code)
        with open(filename, 'wb') as fd:
            for chunk in res.iter_content(chunk_size=128):
                fd.write(chunk)

    def extract_images(self, extract_path):
        with zipfile.ZipFile('/Users/maxg/PycharmProjects/ClosingPage/'
                             'static/img/phase-one/test.zip') as z:
            z.extractall('/Users/maxg/PycharmProjects/ClosingPage/'
                         'static/img/phase-one/target')



if __name__ == '__main__':
    ca = ConvertApi()
    t1 = time.time()
    ca.convert_powerpoint('a', 'b')

    print(time.time() - t1)
