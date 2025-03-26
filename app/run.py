from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.auth_controller import auth
from controllers.task_controller import task_bp
from config import SECRET_KEY

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = SECRET_KEY
jwt = JWTManager(app)

app.register_blueprint(auth)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)
