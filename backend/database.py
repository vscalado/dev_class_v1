# Importações necessárias para trabalhar com MongoDB de forma assíncrona
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseModel

# Configurações do banco de dados
# Em um ambiente real, estas configurações viriam de variáveis de ambiente por segurança
MONGODB_URL = "mongodb://mongodb:27017"  # URL de conexão com o MongoDB
DATABASE_NAME = "dev_class_db"           # Nome do banco de dados

# Classe para gerenciar a conexão com o MongoDB
# Usamos uma classe para manter o estado da conexão durante toda a execução da aplicação
class MongoDB:
    client: Optional[AsyncIOMotorClient] = None  # Cliente de conexão com o MongoDB
    db: Optional[AsyncIOMotorClient] = None      # Referência ao banco de dados

# Instância global do gerenciador de banco de dados
db = MongoDB()

# Função assíncrona para estabelecer conexão com o MongoDB
# É chamada quando a aplicação inicia
async def connect_to_mongo():
    db.client = AsyncIOMotorClient(MONGODB_URL)
    db.db = db.client[DATABASE_NAME]

# Função assíncrona para fechar a conexão com o MongoDB
# É chamada quando a aplicação é encerrada
async def close_mongo_connection():
    if db.client:
        db.client.close()

# Modelo de dados para usuário no banco de dados
# Define a estrutura de como um usuário é armazenado no MongoDB
class UserInDB(BaseModel):
    email: str                    # Email do usuário (identificador único)
    hashed_password: str          # Senha criptografada
    name: str                     # Nome do usuário
    created_at: str              # Data de criação da conta
    last_login: Optional[str]    # Última vez que o usuário fez login
    settings: dict = {}          # Configurações personalizadas do usuário (opcional)