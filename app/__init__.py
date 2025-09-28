# Inicialización del paquete app

from flask import Flask

from app.routes.home import home_bp
from app.routes.auth import auth_bp
from app.routes.tasks import tasks_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'  # cambia esto en producción
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    return app
