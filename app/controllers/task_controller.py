from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.task_model import Task

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.json
    Task.create_task(user_id, data['title'], data.get('description', ''))
    return jsonify({"message": "Task created successfully"}), 201

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.get_tasks_by_user(user_id)
    return jsonify(tasks)

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task_status(task_id):
    data = request.json
    Task.update_task_status(task_id, data['status'])
    return jsonify({"message": "Task status updated"})

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    Task.delete_task(task_id)
    return jsonify({"message": "Task deleted"})
