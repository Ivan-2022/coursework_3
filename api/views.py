from flask import Blueprint, jsonify
import logging
from posts.posts_utils import Posts
from posts.comments_utils import Comments
from config import POST_PATH, COMMENT_PATH

api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")

posts_data = Posts(POST_PATH)
comments = Comments(COMMENT_PATH)


@api_blueprint.route("/api/posts/")
def page_index():
    logging.info("Запрошены все посты через API")
    posts = posts_data.get_posts_all()
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_pk>/")
def page_post_one(post_pk):
    logging.info(f"открытие одного поста по его идентификатору pk {post_pk} через API")
    post = posts_data.get_post_by_pk(post_pk)
    return jsonify(post)
