# Importações necessárias para autenticação e gerenciamento de usuários
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
import jwt
from passlib.context import CryptContext
from database.models import User, get_db

# Configuração do passlib para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criação do roteador para endpoints de autenticação
router = APIRouter()

# Configurações de segurança
# Em um ambiente real, estas chaves estariam em variáveis de ambiente
SECRET_KEY = "sua_chave_secreta"  # Chave para gerar tokens JWT
ALGORITHM = "HS256"               # Algoritmo usado para gerar tokens

# Modelo de dados para criação de usuário
# Define os campos necessários para registrar um novo usuário
class UserCreate(BaseModel):
    email: EmailStr    # Garantimos que é um email válido
    password: str      # Senha em texto puro (será criptografada)
    name: str         # Nome do usuário

# Modelo de dados para login
# Define os campos necessários para fazer login
class UserLogin(BaseModel):
    email: EmailStr    # Email do usuário
    password: str      # Senha do usuário

# Modelo para o token de autenticação
# Define a estrutura do token retornado após login
class Token(BaseModel):
    access_token: str   # Token JWT
    token_type: str    # Tipo do token (Bearer)

# Modelo para resposta com dados do usuário
# Define quais dados do usuário são retornados nas requisições
class UserResponse(BaseModel):
    email: str         # Email do usuário
    name: str          # Nome do usuário
    created_at: str    # Data de criação da conta

# Função para criar o token JWT de acesso
# Recebe os dados do usuário e retorna um token válido por 30 minutos
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)  # Token expira em 30 minutos
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para criar o hash da senha
# Recebe a senha em texto puro e retorna o hash seguro
def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()  # Gera um salt aleatório
    return bcrypt.hashpw(password.encode(), salt).decode()

# Função para verificar se a senha está correta
# Compara a senha fornecida com o hash armazenado
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

# Endpoint para registrar um novo usuário
# Recebe os dados do usuário e retorna os dados cadastrados
@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    # Verifica se já existe um usuário com este email
    if await db.db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    # Cria o documento do usuário com a senha criptografada
    user_doc = UserInDB(
        email=user.email,
        hashed_password=get_password_hash(user.password),  # Criptografa a senha
        name=user.name,
        created_at=datetime.utcnow().isoformat(),  # Data atual em formato ISO
    )
    
    # Salva o novo usuário no banco de dados
    await db.db.users.insert_one(user_doc.dict())
    
    # Retorna os dados do usuário (sem a senha)
    return UserResponse(
        email=user.email,
        name=user.name,
        created_at=user_doc.created_at
    )

# Modelo para listar usuários (removendo dados sensíveis)
class UserList(BaseModel):
    email: str
    name: str
    created_at: str
    last_login: Optional[str]

# Endpoint para debug/manutenção - listar todos os usuários
# Este endpoint não deve ser exposto em produção ou deve ter autenticação de admin
@router.get("/debug/users", response_model=list[UserList], tags=["debug"])
async def list_users():
    """
    Lista todos os usuários cadastrados (apenas para debug/manutenção).
    Retorna apenas informações não sensíveis dos usuários.
    """
    users = []
    cursor = db.db.users.find({})
    async for user in cursor:
        users.append(UserList(
            email=user["email"],
            name=user["name"],
            created_at=user["created_at"],
            last_login=user.get("last_login")
        ))
    return users

# Endpoint para fazer login
# Recebe email e senha, retorna um token de acesso se as credenciais estiverem corretas
@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    # Busca o usuário pelo email no banco de dados
    user_doc = await db.db.users.find_one({"email": user.email})
    if not user_doc:
        raise HTTPException(status_code=400, detail="Email não encontrado")
    
    # Verifica se a senha fornecida corresponde à senha armazenada
    if not verify_password(user.password, user_doc["hashed_password"]):
        raise HTTPException(status_code=400, detail="Senha incorreta")
    
    # Atualiza a data/hora do último login do usuário
    await db.db.users.update_one(
        {"email": user.email},
        {"$set": {"last_login": datetime.utcnow().isoformat()}}
    )
    
    # Gera um novo token JWT para o usuário
    # O token contém o email do usuário e expira em 30 minutos
    access_token = create_access_token(
        data={"sub": user.email}  # 'sub' é o campo padrão para o identificador do usuário
    )
    
    # Retorna o token de acesso
    return Token(access_token=access_token, token_type="bearer")