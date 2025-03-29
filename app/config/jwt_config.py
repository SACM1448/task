from flask_jwt_extended import JWTManager
from app.models.token_blacklist import TokenBlacklist

def configure_jwt(app):
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_data):
        jti = jwt_data["jti"]
        return TokenBlacklist.is_token_blacklisted(jti)

    return jwt
