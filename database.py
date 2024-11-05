# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Dados de conexão
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "Willian"
DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = "3306"
DATABASE_NAME = "user"

# Alterando o driver para pymysql
DATABASE_URL = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()
