# models/user.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .address import Address, Base

class User(Base):
    __tablename__ = 'users'  # o nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    cpf = Column(String(19), nullable=True)
    email = Column(String(255), unique=True, nullable=True)
    address_id = Column(Integer, ForeignKey('addresses.id'))  # chave estrangeira para Address

    address = relationship("Address", backref="users")  # relacionamento com o modelo Address
    
    def format_cpf(self):
        # Verifica se o CPF existe e tem 11 dígitos
        if self.cpf and len(self.cpf) == 11:
            return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return self.cpf

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": "*********",
            "cpf": self.format_cpf(), 
            "email": self.email,
            "address": {
                "id": self.address.id,
                "street": self.address.street,
                "city": self.address.city,
                "state": self.address.state,
                "zip_code": self.address.zip_code
            } if self.address else None
        }
