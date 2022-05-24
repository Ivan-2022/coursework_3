import pytest
from posts.comments_utils import Comments
from config import COMMENT_PATH

comments_data = Comments


@pytest.fixture
def load_comments():
    path = COMMENT_PATH
    return comments_data(path)


def test_get_comments_by_post_id_type(load_comments):
    """Тест комментариев, тип данных (get_comments_by_post_id)"""
    comments = load_comments.get_comments_by_post_id(1)
    assert type(comments) == list, "Комментарии всех постов должны быть списком"
    assert type(comments[0]) == dict, "Комментарии одного поста должны быть словарем"


def test_get_comments_by_post_id_keys(load_comments):
    """Тест комментариев, ключи (get_comments_by_post_id)"""
    comment = load_comments.get_comments_by_post_id(1)[0]
    expected_keys = {"post_pk", "commenter_name", "comment", "pk"}
    keys = set(comment.keys())
    assert keys == expected_keys, "Полученные ключи не верны"


parameters_get_comments_by_post_id = [(1, {1, 2, 3, 4}), (2, {5, 6, 7, 8}), (0, set())]


@pytest.mark.parametrize("post_pk, pk", parameters_get_comments_by_post_id)
def test_get_comments_by_post_id(load_comments, post_pk, pk):
    """Тест поиска по пользователю (get_posts_by_user)"""
    comments = load_comments.get_comments_by_post_id(post_pk)
    comments_pk_set = set()
    for comment in comments:
        comments_pk_set.add(comment["pk"])
    assert comments_pk_set == pk, f"Найдены неверные комментарии к посту {post_pk}"
