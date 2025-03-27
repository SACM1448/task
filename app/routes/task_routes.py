from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.task_controller import TaskController 
task_bp = Blueprint("task_bp", __name__)

@task_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    data = request.json
    response, status = TaskController.create_task(data)
    return jsonify(response), status

@task_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    response, status = TaskController.get_tasks()
    return jsonify(response), status

@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task_status(task_id):
    data = request.json
    response, status = TaskController.update_task_status(task_id, data)
    return jsonify(response), status

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    response, status = TaskController.delete_task(task_id)
    return jsonify(response), status
