# dtos/address_dto.py
from pydantic import BaseModel, Field
from typing import Optional

class AddressDTO(BaseModel):
    street: str = Field(..., max_length=100, description="Rua do endereço")
    city: str = Field(..., max_length=50, description="Cidade do endereço")
    state: str = Field(..., max_length=50, description="Estado do endereço")
    zip_code: Optional[str] = Field(None, max_length=20, min_length=5, description="CEP do endereço")  # Agora é realmente opcional