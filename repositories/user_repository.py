# repositories/user_repository.py

from models.user import User

class UserRepository:
    def __init__(self):
        self.users = [
            User(1, "Alice", "alice@example.com"),
            User(2, "Bob", "bob@example.com"),
            User(3, "Charlie", "charlie@example.com"),
        ]
        self.next_id = 4  # Para gerar novos IDs automaticamente

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def create_user(self, name, email):
        user = User(self.next_id, name, email)
        self.users.append(user)
        self.next_id += 1  # Incrementar o ID para o próximo usuário
        return user
