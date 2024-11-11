# controllers/user_controller.py

from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from services.user_service import UserService
from dtos.user_dto import UserDTO, UserUpdateDTO
from flask import Blueprint, jsonify

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user_data = UserDTO(**data)  # Cria o DTO UserDTO com os dados da requisição
        response = user_service.create_user(user_data)  # Passa o objeto UserDTO        
        
        return jsonify(response), 201  # Retorna o JSON serializável
    except ValidationError as e:
        error_messages = [{"loc": err["loc"], "msg": err["msg"], "type": err["type"]} for err in e.errors()]
        return jsonify({"error": error_messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    try:
        # Obtém os dados diretamente do serviço
        users = user_service.get_all_users()
        
        # Retorna a resposta em JSON sem conversão adicional
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        # Chama o serviço para obter o usuário pelo ID
        user = user_service.get_user_by_id(user_id)
        
        if user is None:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify(user), 200  # Retorna o usuário como JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Chama o serviço para excluir o usuário pelo ID
        success = user_service.delete_user(user_id)
        
        if success:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        user_data = UserUpdateDTO(**data)  # Cria o DTO UserDTO com os dados da requisição
        response = user_service.update_user(user_id, user_data)  # Passa o id e o objeto UserDTO
        
        if response:
            return jsonify(response), 200  # Retorna o JSON serializável
        else:
            return jsonify({"error": "User not found"}), 404
    except ValidationError as e:
        error_messages = [{"loc": err["loc"], "msg": err["msg"], "type": err["type"]} for err in e.errors()]
        return jsonify({"error": error_messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
