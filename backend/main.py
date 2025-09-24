# Importações do FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler

# Importações do sistema
from datetime import datetime
import os

# Importações locais
from routers import auth, converters
from database.models import create_tables, Base, engine

# Cria a aplicação FastAPI
app = FastAPI(
    title="Portal de Conversores API",
    description="API do projeto didático de conversores e calculadoras",
    version="1.0.0"
)

# Configuração do CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://dev-class.onrender.com",
    "https://dev-class-web.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Eventos do ciclo de vida da aplicação
@app.on_event("startup")
async def startup_event():
    """Executado quando a aplicação inicia"""
    # Cria todas as tabelas do banco de dados
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown_event():
    """Executado quando a aplicação é encerrada"""
    # Pode ser usado para limpeza de recursos
    pass

# Tratamento de exceções global
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log do erro (em produção usar um logger apropriado)
    print(f"Erro não tratado: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno do servidor"}
    )

# Registro das rotas
app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Autenticação"]
)
app.include_router(
    converters.router,
    prefix="/api/converters",
    tags=["Conversores"]
)

# Rota de verificação de saúde
@app.get("/api/health")
async def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": app.version
    }

# Rota raiz
@app.get("/")
async def root():
    """Endpoint raiz com informações básicas sobre a API"""
    return {
        "title": app.title,
        "version": app.version,
        "docs": "/docs",
        "redoc": "/redoc"
    }