from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.auth_controller import AuthController

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    response, status = AuthController.register_user(data) 
    return jsonify(response), status

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    response, status = AuthController.login_user(data)  
    return jsonify(response), status

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response, status = AuthController.logout_user()
    return jsonify(response), status

@auth.route('/update', methods=['PUT'])
@jwt_required()
def update_user():
    user_id = str(get_jwt_identity())  
    data = request.json
    response, status = AuthController.update_user(user_id, data)
    return jsonify(response), status


@auth.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_user():
    user_id = get_jwt_identity()
    response, status = AuthController.delete_user(user_id)
    return jsonify(response), status

@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    return jsonify({"message": f"Hola usuario {user_id}, tienes acceso a este recurso."})
