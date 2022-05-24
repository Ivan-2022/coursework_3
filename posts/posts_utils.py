import json
from json import JSONDecodeError

from exceptions import DataJsonError


class Posts:
    """Класс для работы с постами"""
    def __init__(self, path):
        self.path = path

    def load_json_data(self):
        """
        Получаем данные из json файла
        """
        try:
            with open(self.path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                return data

        except (FileNotFoundError, JSONDecodeError):
            raise DataJsonError

    def get_posts_all(self):
        """
        Возвращает посты
        """
        posts = self.load_json_data()
        return posts

    def get_posts_by_user(self, user_name):
        """
        Возвращает посты определенного пользователя
        """
        posts = self.get_posts_all()
        posts_found = []
        for post in posts:
            if post["poster_name"].lower() == user_name.lower():
                posts_found.append(post)

        return posts_found

    def search_for_posts(self, query):
        """
        Возвращает список постов по ключевому слову
        """
        posts = self.get_posts_all()
        posts_found = []
        for post in posts:
            if query.lower() in post["content"].lower():
                posts_found.append(post)
        return posts_found

    def get_post_by_pk(self, pk):
        """
        Возвращает один пост по его идентификатору
        """
        posts = self.get_posts_all()
        for post in posts:
            if post["pk"] == pk:
                return post
