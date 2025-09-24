from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# Pega a URL do banco de dados das variáveis de ambiente
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./dev_class.db')

# Ajusta a URL se necessário para o PostgreSQL no Render.com
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Sessão para operações no banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Função para obter uma sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()