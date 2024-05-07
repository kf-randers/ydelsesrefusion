from flask import Flask
from healthcheck import HealthCheck

from utils.config import DEBUG
from utils.logging import get_logger


def create_app():
    app = Flask(__name__)
    health = HealthCheck()
    app.add_url_rule("/healthz", "healthcheck", view_func=lambda: health.run())
    return app


logger = get_logger(__name__)
app = create_app()


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=DEBUG, host='0.0.0.0', port=8080)
