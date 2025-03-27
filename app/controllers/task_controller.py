from flask_jwt_extended import get_jwt_identity
from app.services.task_service import TaskService

class TaskController:
    @staticmethod
    def create_task(data):
        user_id = get_jwt_identity()
        return TaskService.create_task(user_id, data.get("title"), data.get("description", ""))

    @staticmethod
    def get_tasks():
        user_id = get_jwt_identity()
        return TaskService.get_tasks(user_id)

    @staticmethod
    def update_task_status(task_id, data):
        user_id = get_jwt_identity()
        return TaskService.update_task_status(user_id, task_id, data.get("status"))

    @staticmethod
    def delete_task(task_id):
        user_id = get_jwt_identity()
        return TaskService.delete_task(user_id, task_id)
