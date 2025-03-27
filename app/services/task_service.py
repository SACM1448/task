from app.models.task_model import Task

class TaskService:
    @staticmethod
    def create_task(user_id, title, description=""):
        if not title:
            return {"error": "Title is required"}, 400

        Task.create_task(user_id, title, description)
        return {"message": "Task created successfully"}, 201

    @staticmethod
    def get_tasks(user_id):
        tasks = Task.get_tasks_by_user(user_id)
        return tasks, 200

    @staticmethod
    def update_task_status(user_id, task_id, status):
        task = Task.get_task_by_id(task_id)

        if not task:
            return {"error": "Task not found"}, 404
        if task["user_id"] != user_id:
            return {"error": "Unauthorized"}, 403
        if status is None:
            return {"error": "Status is required"}, 400

        Task.update_task_status(task_id, status)
        return {"message": "Task status updated"}, 200

    @staticmethod
    def delete_task(user_id, task_id):
        task = Task.get_task_by_id(task_id)

        if not task:
            return {"error": "Task not found"}, 404
        if task["user_id"] != user_id:
            return {"error": "Unauthorized"}, 403

        Task.delete_task(task_id)
        return {"message": "Task deleted"}, 200
