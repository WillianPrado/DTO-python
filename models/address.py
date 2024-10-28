# models/address.py
from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str = Field(..., max_length=100, description="Rua do endereço")
    city: str = Field(..., max_length=50, description="Cidade do endereço")
    state: str = Field(..., max_length=50, description="Estado do endereço")
    zip_code: str = Field(..., max_length=20, description="CEP do endereço")
