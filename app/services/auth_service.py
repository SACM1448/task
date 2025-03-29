from app.models.user_model import UserModel
from app.models.token_blacklist import TokenBlacklist
import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, get_jwt

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
            token = create_access_token(identity=str(user['id']))
            return {"token": token}, 200  
        return {"message": "Invalid credentials"}, 401  


    @staticmethod
    def logout_user():
        jti = get_jwt()["jti"]
        TokenBlacklist.blacklist_token(jti)
        return {"message": "Logout successful"}, 200

    @staticmethod
    def update_user(user_id, username, email):
        user = UserModel.get_user_by_email(email)
        
        if user and str(user["id"]) != str(user_id):  
            return {"message": "Email already in use"}, 400

        UserModel.update_user(user_id, username, email)
        return {"message": "User updated successfully"}, 200


    @staticmethod
    def delete_user(user_id):
        UserModel.delete_user(user_id)
        return {"message": "User deleted successfully"}, 200

