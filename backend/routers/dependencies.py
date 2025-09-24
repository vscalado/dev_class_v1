from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")