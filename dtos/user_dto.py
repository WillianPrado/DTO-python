# dtos/user_dto.py
from pydantic import BaseModel, EmailStr, Field, validator,ConfigDict
from dtos.address_dto import AddressDTO  # Importa o AddressDTO

from typing import Optional
import re
class UserDTO(BaseModel):
    name: str = Field(..., max_length=100, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=6, max_length=100, description="Senha do usuário")
    address: Optional[AddressDTO]
    # model_config = ConfigDict(from_attributes=True)  # Adiciona o campo AddressDTO para validação de endereço

    # Validador personalizado para o campo `name`
    @validator('name')
    def name_length(cls, value):
        if len(value) < 1:
            raise ValueError("Nome do usuário muito curto.")
        return value
class UserListDTO:
    def __init__(self, id, name, zip_code):
        self.id = id
        self.name = name
        self.zip_code = zip_code

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "zip_code": self.zip_code
        }
class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Optional[AddressDTO]
    model_config = ConfigDict(from_attributes=True) 
