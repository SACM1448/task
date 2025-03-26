from database import get_db_connection

class Task:
    @staticmethod
    def create_task(user_id, title, description):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (user_id, title, description) VALUES (%s, %s, %s)", 
                       (user_id, title, description))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_tasks_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks WHERE user_id=%s", (user_id,))
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        return tasks

    @staticmethod
    def update_task_status(task_id, status):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status=%s WHERE id=%s", (status, task_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_task(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
