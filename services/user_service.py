# services/user_service.py

from repositories.user_repository import UserRepository
from dtos.user_dto import UserDTO
from models.user import UserModel

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, user_data: UserDTO):
        user = UserModel( 
            id=55, 
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
            address=user_data.address.dict()  # Converte AddressDTO em dicionário
        )
        # Aqui você salvaria `user` no repositório ou banco de dados
        return user
