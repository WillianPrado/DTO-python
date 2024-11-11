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
        # import pdb;pdb.set_trace()
        user = self.user_repository.get_user_by_id(user_id)
        if user :
            user = user.to_dict()
        return user if user else None

    def create_user(self, user_data: UserDTO):
        # Verifica se o `address_id` foi fornecido
        address = None
        if user_data.address_id:
            # Busca o endereço pelo `address_id`
            address = self.session.query(Address).filter_by(id=user_data.address_id).one_or_none()
            if address is None:
                raise ValueError("Endereço não encontrado com o ID fornecido.")
        else:
            # Cria um novo endereço se `address_id` não foi fornecido
            address = Address(
                street=user_data.address.street,
                city=user_data.address.city,
                state=user_data.address.state,
                zip_code=user_data.address.zip_code
            )

        # Cria o objeto User e associa o endereço (existente ou novo)
        user = User(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
            cpf=user_data.cpf,
            address=address  # Associa o Address ao User
        )

        try:
            saved_user = self.user_repository.create_user(user)
            response = saved_user.to_dict()
            return response
        finally:
            self.session.close()

    def delete_user(self, user_id):
        # Chama o repositório para excluir o usuário pelo ID
        return self.user_repository.delete_user(user_id)
    
    def update_user(self, user_id, user_data: User):
        # Chama o repositório para atualizar o usuário pelo ID e os novos dados
        updated_user = self.user_repository.update_user(user_id, user_data)
        
        # Retorna o usuário atualizado ou None se não encontrado
        return updated_user.to_dict() if updated_user else None
