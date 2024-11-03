# dtos/user_dto.py
from pydantic import BaseModel, EmailStr, Field, validator
from dtos.address_dto import AddressDTO  # Importa o AddressDTO

from typing import Optional
import re


class AddressDTO(BaseModel):
    street: Optional[str] = Field(None, min_length=3, max_length=100, description="Nome da rua")
    city: Optional[str] = Field(None, min_length=2, max_length=50, description="Cidade")
    state: str = Field(..., min_length=2, max_length=50, description="Estado")
    zip_code: str = Field(..., description="Código postal")

    # Validador para o campo zip_code
    @validator('zip_code')
    def validate_zip_code(cls, value):
        # Exemplo de regex para validar CEP no formato brasileiro NNNNN-NNN
        if not re.match(r'^\d{5}-\d{3}$', value):
            raise ValueError("CEP inválido. O formato correto é NNNNN-NNN.")
        return value

    # Validador para o campo state
    @validator('state')
    def validate_state(cls, value):
        if len(value) != 2 and not value.isalpha():
            raise ValueError("Estado inválido. Deve ser o código do estado com 2 letras ou o nome completo.")
        return value

class UserDTO(BaseModel):
    name: str = Field(..., max_length=100, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=6, max_length=100, description="Senha do usuário")
    address: AddressDTO  # Adiciona o campo AddressDTO para validação de endereço

    # Validador personalizado para o campo `name`
    @validator('name')
    def name_length(cls, value):
        if len(value) < 1:
            raise ValueError("Nome do usuário muito curto.")
        return value

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: AddressDTO
