from app.services.auth_service import AuthService

class AuthController:
    @staticmethod
    def register_user(data):
        return AuthService.register_user(data['username'], data['email'], data['password'])

    @staticmethod
    def login_user(data):
        return AuthService.login_user(data['email'], data['password'])


    @staticmethod
    def logout_user():
        return AuthService.logout_user()

    @staticmethod
    def update_user(user_id, data):
        username = data.get("username")  
        email = data.get("email")

        if not username or not email:
            return {"message": "Missing required fields"}, 400

        return AuthService.update_user(user_id, username, email)

    @staticmethod
    def delete_user(user_id):
        return AuthService.delete_user(user_id)

   