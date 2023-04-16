from pprint import pprint
import requests
import os

# Задача №1

# def test_request():
    
#     url = "https://akabab.github.io/superhero-api/api/all.json"
    
#     response = requests.get(url)
#     data = response.json()
#     heroes =  {}
#     for super_hero in data:
#         if super_hero['name'] == "Hulk" :
#             heroes[super_hero['name']] = super_hero["powerstats"]['intelligence']
#         elif super_hero['name'] == "Captain America":
#             heroes[super_hero['name']] = super_hero["powerstats"]['intelligence']
#         elif super_hero['name'] == "Thanos":
#             heroes[super_hero['name']] = super_hero["powerstats"]['intelligence']
    
#     heroes_sort = sorted(heroes.items(), reverse=True)

#     print(*heroes_sort[0])
    
# if __name__ == '__main__':
#     test_request()


# Задача №2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
# Запрашиваем ссылку для загрузки файла
    def _get_upload_link(self, disk_file_path):
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": 'true'}
        response = requests.get(url=file_url, headers=headers, params=params)
        return response.json()

# Загружаем файл по запрошенной ссылке       
    def upload(self, disk_file_path: str, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        data = self._get_upload_link(disk_file_path=disk_file_path)
        url = data.get('href')
        response = requests.put(url=url, data=open(file_name, 'rb'))

        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получаем путь к загружаемому файлу и токен от пользователя
    path_to_file = r"C:\Users\Admin\Desktop\requests-hw\for_upload_yadisk\to_yadisk.txt"
    token = ""
    # Имя папки загрузки и имя загружаемого файла 
    file_path = 'netology'
    file_name = 'to_yadisk.txt'
    
    uploader = YaUploader(token)
    uploader.upload(f"{file_path}/{file_name}", path_to_file)
