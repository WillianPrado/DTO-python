# models/address.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Address(Base):
    __tablename__ = 'addresses'  # o nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    state = Column(String(255), nullable=True)
    zip_code = Column(String(20), unique=True, nullable=True)
