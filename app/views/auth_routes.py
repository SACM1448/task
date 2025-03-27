from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.auth_controller import register_user, login_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    return jsonify(*register_user(data))

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    return jsonify(*login_user(data))

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify(*logout_user())

@auth.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    return jsonify({"message": f"Hola usuario {user_id}, tienes acceso a este recurso."})
