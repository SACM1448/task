from app.models.user_model import UserModel
from app.models.token_blacklist import TokenBlacklist
import bcrypt
from flask_jwt_extended import create_access_token, get_jwt

class AuthService:
    @staticmethod
    def register_user(username, email, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        UserModel.create_user(username, email, hashed_password)
        return {"message": "User registered successfully"}, 201

    @staticmethod
    def login_user(email, password):
        user = UserModel.get_user_by_email(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            token = create_access_token(identity=user['id'])
            return {"token": token}
        return {"message": "Invalid credentials"}, 401

    @staticmethod
    def logout_user():
        jti = get_jwt()["jti"]
        TokenBlacklist.blacklist_token(jti)
        return {"message": "Logout successful"}, 200
