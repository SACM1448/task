from app.config.database import get_db_connection

class TokenBlacklist:
    @staticmethod
    def blacklist_token(jti):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO blacklisted_tokens (token) VALUES (%s)", (jti,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def is_token_blacklisted(jti):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM blacklisted_tokens WHERE token = %s", (jti,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
