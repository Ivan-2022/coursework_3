from flask import Blueprint, render_template, abort, request
import logging
from posts.posts_utils import Posts
from posts.comments_utils import Comments
from config import POST_PATH, COMMENT_PATH


posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")

posts_data = Posts(POST_PATH)
comments = Comments(COMMENT_PATH)


@posts_blueprint.route("/")
def page_index():
    logging.info("Запрошены все посты")
    posts = posts_data.get_posts_all()
    return render_template("index.html", posts=posts)


@posts_blueprint.route("/search/")
def page_search():
    logging.info("Выполняется поиск по ключевому слову")
    s = request.args.get("s", "")
    if s != "":
        posts = posts_data.search_for_posts(s)
        posts_count = len(posts)
    else:
        posts = []
        posts_count = 0

    return render_template("search.html", s=s, posts=posts, posts_count=posts_count)


@posts_blueprint.route("/users/<username>/")
def page_get_posts_by_user(username):
    logging.info("Возвращаем посты определенного пользователя")
    posts = posts_data.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)


@posts_blueprint.route("/posts/<int:post_pk>/")
def page_post_one(post_pk):
    logging.info(f"открытие одного поста по его идентификатору pk {post_pk}")
    try:
        post = posts_data.get_post_by_pk(post_pk)
        comments_post = comments.get_comments_by_post_id(post_pk)
    except ValueError:
        return "Не удалось открыть пост по его идентификатору"
    else:
        comments_count = len(comments_post)
        if post is None:
            abort(404)
        return render_template("post.html", post=post, comments_post=comments_post, comments_count=comments_count)


@posts_blueprint.errorhandler(404)
def post_error(e):
    return "Такой пост не найден", 404
