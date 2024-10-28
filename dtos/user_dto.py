# dtos/user_dto.py
from pydantic import BaseModel, EmailStr, Field
from dtos.address_dto import AddressDTO  # Importa o AddressDTO

class AddressDTO(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
    address: dict  

class UserDTO(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=6, max_length=100, description="Senha do usuário")
    address: AddressDTO  # Adiciona o campo AddressDTO para validação de endereço

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: AddressDTO
