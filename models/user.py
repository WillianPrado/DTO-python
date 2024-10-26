# models/user.py
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        
from pydantic import BaseModel, EmailStr, Field

class UserModel(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="O nome é obrigatório e não pode exceder 100 caracteres.")
    email: EmailStr = Field(..., description="O email é obrigatório e deve ser válido.")
    password: str = Field(..., min_length=6, max_length=100, description="A senha é obrigatória e deve ter entre 6 e 100 caracteres.")
