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
        user = user_service.create_user(user_data)  # Passa o objeto UserDTO
        
        # Criação do objeto UserResponseDTO e conversão para dicionário
        response = UserResponseDTO(
            id=user.id, 
            name=user.name, 
            email=user.email, 
            address=user.address.dict() # Certifique-se de que address já esteja em formato de dicionário
        ).dict()
        
        return jsonify(response), 201  # Retorna o JSON serializável
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
