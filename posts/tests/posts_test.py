import pytest
from posts.posts_utils import Posts
from config import POST_PATH

posts_data = Posts


@pytest.fixture
def load_posts():
    path = POST_PATH
    return posts_data(path)


def test_get_posts_all_type(load_posts):
    """Тест постов, тип данных (get_posts_all)"""
    posts = load_posts.get_posts_all()
    assert type(posts) == list, "Посты должны быть списком"
    assert type(posts[0]) == dict, "Каждый пост должен быть словарем"


def test_get_posts_all_keys(load_posts):
    """Тест постов, ключи (get_posts_all)"""
    posts = load_posts.get_posts_all()
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    for post in posts:
        keys = post.keys()
        assert set(keys) == expected_keys, "Полученные ключи не верны"


def test_get_posts_by_user_keys(load_posts):
    """Тест поиска по ключевому слову, ключи (get_posts_by_user)"""
    post = load_posts.get_posts_by_user("leo")[0]
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    keys = set(post.keys())
    assert keys == expected_keys, "Полученные ключи не верны"


parameters_get_posts_by_user = [("leo", {1, 5}), ("johnny", {2, 6}), ("hank", {3, 7})]


@pytest.mark.parametrize("poster_name, post_pk", parameters_get_posts_by_user)
def test_get_posts_by_user(load_posts, poster_name, post_pk):
    """Тест поиска по пользователю (get_posts_by_user)"""
    posts = load_posts.get_posts_by_user(poster_name)
    post_pk_set = set()
    for post in posts:
        post_pk_set.add(post["pk"])
    assert post_pk_set == post_pk, "Найдены неверные посты пользователя"


def test_search_for_posts_keys(load_posts):
    """Тест поиска по ключевому слову, ключи (search_for_posts)"""
    post = load_posts.search_for_posts("пирог")[0]
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    keys = set(post.keys())
    assert keys == expected_keys, "Полученные ключи не верны"


parameters_search_for_posts = [("пирог", {1}), ("колонны", {2}), ("ржавые", {3})]


@pytest.mark.parametrize("query, post_pk", parameters_search_for_posts)
def test_search_for_posts(load_posts, query, post_pk):
    """Тест поиска по ключевому слову (search_for_posts)"""
    posts = load_posts.search_for_posts(query)
    post_pk_set = set()
    for post in posts:
        post_pk_set.add(post["pk"])
    assert post_pk_set == post_pk, "Некорректный поиск по ключевому слову"


def test_get_post_by_pk_type(load_posts):
    """Тест одного поста, тип данных (get_post_by_pk)"""
    post = load_posts.get_post_by_pk(1)
    assert type(post) == dict, "Пост должен быть словарем"


def test_get_post_by_pk_keys(load_posts):
    """Тест одного поста, ключи (get_post_by_pk)"""
    post = load_posts.get_post_by_pk(1)
    expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    keys = set(post.keys())
    assert keys == expected_keys, "Полученные ключи не верны"


parameters_get_post_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]  # не забыть переписать на range


@pytest.mark.parametrize("post_pk", parameters_get_post_by_pk)
def test_get_post_by_pk_correct(load_posts, post_pk):
    """Тест одного поста, номер pk (get_post_by_pk)"""
    post = load_posts.get_post_by_pk(post_pk)
    assert post["pk"] == post_pk, "Номер полученного поста не соответствует номеру запрошенного поста"
