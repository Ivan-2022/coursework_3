from flask import Flask
from posts.views import posts_blueprint
from api.views import api_blueprint
import logging

app = Flask(__name__)

Log_Format = "%(asctime)s [%(levelname)s] %(message)s"

logging.basicConfig(filename="api.log",
                    filemode="w",
                    format=Log_Format,
                    level=logging.INFO,
                    encoding="UTF-8")

logger = logging.getLogger()
app.register_blueprint(posts_blueprint)

app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run()
