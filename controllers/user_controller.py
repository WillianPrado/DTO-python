# controllers/user_controller.py

from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from services.user_service import UserService
from dtos.user_dto import UserDTO, UserResponseDTO

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
        return "Erro ao salvar", 500
