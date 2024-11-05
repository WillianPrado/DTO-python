from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from models.address import Address
from dtos.user_dto import UserListDTO

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        # Realiza a consulta e retorna diretamente um result set de dicionários
        stmt = (
            select(User.id, User.name, Address.zip_code)
            .join(User.address)
        )

        # Executa a consulta e usa `mappings` para retornar dicionários
        result = self.session.execute(stmt).mappings().all()

        # Converte os resultados em instâncias de UserListDTO
        return [
            UserListDTO(id=row["id"], name=row["name"], zip_code=row["zip_code"]).to_dict()
            for row in result
        ]

    def get_user_by_id(self, user_id) -> User:
        user =  self.session.query(User).filter(User.id == user_id).first()
        return user

    def create_user(self, user: User):
        self.session.add(user)  # Adiciona User e Address à sessão
        self.session.commit()  # Commit de User e Address juntos
        self.session.refresh(user)
        return user

    def update_user(self, user_id, name=None, email=None, address_id=None):
        user = self.get_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            if address_id:
                user.address_id = address_id
            self.session.commit()
        return user

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
        return user
