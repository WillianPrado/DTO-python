from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
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
        try:
            self.session.add(user)  # Adiciona User e Address à sessão
            self.session.commit()  # Commit de User e Address juntos
            self.session.refresh(user)
            return user
        except IntegrityError as e:
            
            # Verifica se o erro está relacionado a duplicidade de `zip_code`
            if "Duplicate entry" in str(e) and "zip_code" in str(e):
                raise ValueError("Este CEP já está cadastrado.")
            if "Duplicate entry" in str(e) and "email" in str(e):
                raise ValueError("Este E-mail já está cadastrado.")
            else:
                raise

    
    def update_user(self, user_id, user_data):
        # Busca o usuário pelo ID
        user = self.session.query(User).filter_by(id=user_id).one_or_none()
        
        if user is None:
            return None  # Retorna None se o usuário não for encontrado
        
        # Atualiza os campos do usuário
        user.name = user_data.name
        if user.password == user_data.password:
            raise ValueError("A senha não pode ser a mesma")
        
        user.email = user_data.email
        user.password = user_data.password
        

        # Atualiza os campos do endereço
        user.address.street = user_data.address.street
        user.address.city = user_data.address.city
        user.address.state = user_data.address.state
        user.address.zip_code = user_data.address.zip_code

        self.session.commit()  # Commit para salvar as alterações no banco
        self.session.refresh(user)  # Atualiza o objeto user com os dados persistidos
        return user
    
    def delete_user(self, user_id):
        # Cria uma consulta para excluir o usuário pelo ID
        stmt = delete(User).where(User.id == user_id)
        result = self.session.execute(stmt)
        
        # Confirma a transação para aplicar a exclusão
        self.session.commit()
        
        # Verifica se alguma linha foi afetada (ou seja, se o usuário existia)
        return result.rowcount > 0