# controllers/user_controller.py

from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from services.user_service import UserService
from models.user import UserModel

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

@user_controller.route('/users', methods=['POST'])
def create_user():
    try:
        # Tenta criar uma instância de UserModel, que valida os dados automaticamente
        user_data = UserModel(**request.get_json())
        
        # Se os dados forem válidos, cria o usuário
        user = user_service.create_user(user_data.name, user_data.email)
        
        # Retorna o usuário criado
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

    except ValidationError as e:
        # Retorna os erros de validação em caso de dados inválidos
        return jsonify(e.errors()), 400
