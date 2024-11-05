# models/user.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .address import Address, Base

class User(Base):
    __tablename__ = 'users'  # o nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, nullable=True)
    address_id = Column(Integer, ForeignKey('addresses.id'))  # chave estrangeira para Address

    address = relationship("Address", backref="users")  # relacionamento com o modelo Address

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": {
                "id": self.address.id,
                "street": self.address.street,
                "city": self.address.city,
                "state": self.address.state,
                "zip_code": self.address.zip_code
            } if self.address else None
        }
