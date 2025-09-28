# Aquí van las rutas de la aplicación

from app.routes.home import home_bp
from app.routes.auth import auth_bp
from app.routes.tasks import tasks_bp

# Para registrar los blueprints en la app principal:
# app.register_blueprint(home_bp)
# app.register_blueprint(auth_bp)
# app.register_blueprint(tasks_bp)