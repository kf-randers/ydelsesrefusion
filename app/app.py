import os
from flask import Flask
from healthcheck import HealthCheck

DEBUG = os.getenv('DEBUG', False)

def create_app():
    app = Flask(__name__)
    health = HealthCheck()
    app.add_url_rule("/healthz", "healthcheck", view_func=lambda: health.run())
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG, host='0.0.0.0', port=8080)