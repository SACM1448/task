import bcrypt
from flask_jwt_extended import create_access_token, get_jwt
from app.models.user_model import UserModel
from app.models.token_blacklist import TokenBlacklist 

# Registro de usuario
def register_user(data):
    username = data['username']
    email = data['email']
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), salt).decode('utf-8')

    UserModel.create_user(username, email, hashed_password)

    return {"message": "User registered successfully"}, 201

# Inicio de sesión
def login_user(data):
    email = data['email']
    password = data['password'].encode('utf-8')

    user = UserModel.get_user_by_email(email)

    if user and bcrypt.checkpw(password, user['password_hash'].encode('utf-8')):
        token = create_access_token(identity=user['id'])
        return {"token": token}

    return {"message": "Invalid credentials"}, 401

# Cerrar sesión (Blacklist del token)
def logout_user():
    jti = get_jwt()["jti"]
    TokenBlacklist.blacklist_token(jti) 
    return {"message": "Logout successful"}, 200
