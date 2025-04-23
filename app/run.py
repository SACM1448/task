from flask import Flask
from app.config.limiter_config import limiter
from app.routes.auth_routes import auth
from app.routes.task_routes import task_bp
from app.config.config import SECRET_KEY
from app.config.jwt_config import configure_jwt 

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = SECRET_KEY

jwt = configure_jwt(app)
limiter.init_app(app) 
# Registrar Blueprints
app.register_blueprint(auth)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=False)
