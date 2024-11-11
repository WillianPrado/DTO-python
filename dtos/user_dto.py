# dtos/user_dto.py
from pydantic import BaseModel, EmailStr, Field, validator,ConfigDict
from dtos.address_dto import AddressDTO  # Importa o AddressDTO

from typing import Optional
import re
class UserDTO(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    password: str = Field(..., min_length=6, max_length=100, description="Senha do usuário")
    cpf: str = Field(..., description="CPF do usuário")
    address: Optional[AddressDTO] = None 
    address_id: Optional[int] = Field(None, description="ID do endereço existente")  # Novo campo opcional

    # Validador personalizado para o campo `name`
    @validator('name')
    def name_length(cls, value):
        if len(value) < 1:
            raise ValueError("Nome do usuário muito curto.")
        return value
    # Validador para o CPF
    @validator('cpf')
    def cpf_validator(cls, value):
        # Remove todos os caracteres não numéricos
        value = re.sub(r'\D', '', value)

        # Verifica se o CPF tem 11 dígitos
        if len(value) != 11:
            raise ValueError("CPF deve conter 11 numeros.")

        # Verifica se todos os dígitos são iguais (exemplo: 111.111.111-11 não é válido)
        if value == value[0] * 11:
            raise ValueError("CPF inválido.")

        # Validação dos dígitos verificadores
        if not cls.is_valid_cpf(value):
            raise ValueError("CPF inválido.")

        return value

    @staticmethod
    def is_valid_cpf(cpf):
        # Cálculo do primeiro dígito verificador
        sum_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digit_1 = (sum_1 * 10 % 11) % 10
        if digit_1 != int(cpf[9]):
            return False

        # Cálculo do segundo dígito verificador
        sum_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digit_2 = (sum_2 * 10 % 11) % 10
        if digit_2 != int(cpf[10]):
            return False

        return True
    

class UserUpdateDTO(BaseModel):
    name: str = Field(..., max_length=100, description="Nome do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    address: Optional[AddressDTO]
    password: Optional[str] =  Field(..., min_length=6, max_length=100, description="Senha do usuário")
    cpf: Optional[str] = Field(None, description="CPF")

    # Validador personalizado para o campo `name`
    @validator('name')
    def name_length(cls, value):
        if len(value) < 1:
            raise ValueError("Nome do usuário muito curto.")
        return value
    
    @validator('cpf')
    def name_length(cls, value):
        if value or value == '':
            raise ValueError("Não é possivel modificar CPF")
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
