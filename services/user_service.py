# services/user_service.py

from repositories.user_repository import UserRepository
from dtos.user_dto import UserDTO, UserResponseDTO
from models.user import User
from models.address import Address
from database import SessionLocal  # Assumindo que você tem uma configuração de sessão

class UserService:
    def __init__(self):
        # Inicializar uma nova sessão para o repositório
        self.session = SessionLocal()
        self.user_repository = UserRepository(self.session)

    def get_all_users(self):
        # Retorna todos os usuários do repositório
        users = self.user_repository.get_all_users()
        return users

    def get_user_by_id(self, user_id):
        # Chama o repositório para obter o usuário pelo ID
        import pdb;pdb.set_trace()
        user = self.user_repository.get_user_by_id(user_id)
        if user :
            user = user.to_dict()
        return user if user else None

    def create_user(self, user_data: UserDTO):
        # Cria o objeto Address
        address = Address(
            street=user_data.address.street,
            city=user_data.address.city,
            state=user_data.address.state,
            zip_code=user_data.address.zip_code
        )
        
        # Cria o objeto User e associa o endereço
        user = User(
            name=user_data.name,
            email=user_data.email,
            address=address  # Associa o Address ao User
        )

        try:
            saved_user = self.user_repository.create_user(user)
            response = saved_user.to_dict()
            return response
        finally:
            self.session.close()

    def __del__(self):
        # Fecha a sessão ao finalizar o serviço
        self.session.close()
