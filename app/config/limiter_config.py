from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity


def rate_limit_key():
    """
    Retorna el ID del usuario autenticado si existe, 
    de lo contrario usa la IP del cliente.
    """
    try:
        verify_jwt_in_request(optional=True)
        user_id = get_jwt_identity()
        if user_id:
            return str(user_id)
    except Exception:
        pass
    return get_remote_address()

# Inicializar el Limiter
limiter = Limiter(key_func=rate_limit_key)
