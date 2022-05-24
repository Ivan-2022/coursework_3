import json
from json import JSONDecodeError

from exceptions import DataJsonError


class Comments:
    """Класс для работы с комментариями"""
    def __init__(self, path):
        self.path = path

    def load_json_comments(self):
        """
        Получаем данные из json файла
        """
        try:
            with open(self.path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                return data

        except (FileNotFoundError, JSONDecodeError):
            raise DataJsonError

    def get_comments_by_post_id(self, post_pk):
        """
        Возвращает комментарии определенного поста
        """
        comments = self.load_json_comments()
        comments_found = []
        for comment in comments:
            if comment["post_pk"] == post_pk:
                comments_found.append(comment)
        return comments_found
