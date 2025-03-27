from app.config.database import get_db_connection
import bcrypt

class UserModel:
    @staticmethod
    def create_user(username, email, password):
        hashed_password = UserModel.hash_password(password)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)", 
                       (username, email, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def update_user(user_id, username, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username=%s, email=%s WHERE id=%s", 
                       (username, email, user_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def verify_password(stored_password, provided_password):
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

    @staticmethod
    def change_password(user_id, new_password):
        conn = get_db_connection()
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("UPDATE users SET password_hash=%s WHERE id=%s", (hashed_password, user_id))
        conn.commit()
        cursor.close()
        conn.close()
