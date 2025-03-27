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
