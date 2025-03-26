from flask_jwt_extended import get_jwt_identity
from models.task_model import Task

class TaskController:
    @staticmethod
    def create_task(data):
        user_id = get_jwt_identity()
        title = data.get("title")
        description = data.get("description", "")

        if not title:
            return {"error": "Title is required"}, 400

        Task.create_task(user_id, title, description)
        return {"message": "Task created successfully"}, 201

    @staticmethod
    def get_tasks():
        user_id = get_jwt_identity()
        tasks = Task.get_tasks_by_user(user_id)
        return tasks, 200

    @staticmethod
    def update_task_status(task_id, data):
        status = data.get("status")
        if status is None:
            return {"error": "Status is required"}, 400

        Task.update_task_status(task_id, status)
        return {"message": "Task status updated"}, 200

    @staticmethod
    def delete_task(task_id):
        Task.delete_task(task_id)
        return {"message": "Task deleted"}, 200
