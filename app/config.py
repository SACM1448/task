from dotenv import load_dotenv
import os
import sys

# Cargar variables de entorno
load_dotenv()

# Obtener variables de entorno con validación
def get_env_variable(var_name, default=None, required=True):
    value = os.getenv(var_name, default)
    if required and not value:
        print(f"❌ Error: La variable de entorno '{var_name}' no está definida o está vacía.")
        sys.exit(1)  # Detener ejecución si falta una variable requerida
    return value

# Configuración de base de datos
DB_CONFIG = {
    "host": get_env_variable("DB_HOST"),
    "user": get_env_variable("DB_USER"),
    "password": get_env_variable("DB_PASSWORD", default="", required=False),
    "database": get_env_variable("DB_NAME")
}

# Clave secreta para JWT
SECRET_KEY = get_env_variable("SECRET_KEY")
