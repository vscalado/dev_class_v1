# Importações do FastAPI
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Importações do SQLAlchemy
from sqlalchemy.orm import Session

# Importações do Pydantic
from pydantic import BaseModel, EmailStr

# Outras importações
from typing import Optional
from datetime import datetime, timedelta
import os

# Importações de segurança
from jose import JWTError, jwt
from passlib.context import CryptContext

# Importações locais
from database.models import User
from database import get_db

# Configurações de segurança
SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta_aqui")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração do hash de senhas - usando pbkdf2_sha256 para evitar problemas com bcrypt
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Configuração do OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

# Router
router = APIRouter()

# Modelos Pydantic
class UserBase(BaseModel):
    email: EmailStr
    name: str
    
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None

# Funções auxiliares
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
        
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

# Rotas
@router.post("/register", response_model=Token)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica se já existe um usuário com este email
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado"
        )
    
    # Cria o novo usuário
    db_user = User(
        email=user.email,
        name=user.name,
        hashed_password=get_password_hash(user.password),
        created_at=datetime.utcnow()
    )
    
    # Salva no banco
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Cria e retorna o token de acesso
    access_token = create_access_token(data={"sub": user.email})
    return Token(access_token=access_token)

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Busca o usuário
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais incorretas"
        )

    # Verifica a senha
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais incorretas"
        )

    # Atualiza último login
    user.last_login = datetime.utcnow()
    db.commit()
    
    # Cria e retorna o token
    access_token = create_access_token(data={"sub": user.email})
    return Token(access_token=access_token)

@router.get("/me", response_model=UserBase)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user