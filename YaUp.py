import requests


class YaUploader:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token: str):
        self.token = token

    def general_headers(self):
        return {'Authorization': self.token}

    def get_upload_link(self, name_file: str):
        headers = self.general_headers()
        params = {'path': name_file, 'overwrite': True}
        URL = f'{self.host}/v1/disk/resources/upload'
        response = requests.get(URL, params=params, headers=headers).json()
        return response.get('href')

    def upload_file(self, name_file, file_path, ):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        link = self.get_upload_link(name_file)
        headers = self.general_headers()
        requests.put(link, data=open(file_path, 'rb'), headers=headers)


if __name__ == '__main__':
    path_to_file = 'Text.txt'
    with open('file.txt') as file_object:
        token = file_object.read()
    uploader = YaUploader(token)
    result = uploader.upload_file('/hi.txt', path_to_file)
