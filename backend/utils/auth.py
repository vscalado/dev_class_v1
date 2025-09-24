"""
Utilitários para autenticação e segurança
"""
from datetime import datetime, timedelta
import os
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from database.models import User, get_db
from sqlalchemy.orm import Session

# Configurações
SECRET_KEY = os.getenv("SECRET_KEY", "desenvolvimento_local_apenas")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Instância do CryptContext para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_hashed_password(password: str) -> str:
    """
    Gera o hash de uma senha
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se uma senha corresponde ao hash
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(email: str, expires_delta: Optional[timedelta] = None) -> str:
    """
    Cria um token JWT
    """
    to_encode = {"sub": email}
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """
    Obtém o usuário atual baseado no token JWT
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decodifica o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
        
    # Busca o usuário no banco
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
        
    return user