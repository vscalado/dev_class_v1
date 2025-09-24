# Arquivo principal da aplicação
# Aqui configuramos o FastAPI e todas as suas funcionalidades principais

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, converters
from database.models import create_tables

# Cria a aplicação FastAPI com um título personalizado
app = FastAPI(title="Curso Dev API")

# Configuração do CORS para o ambiente de produção
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dev-class.onrender.com"],  # Frontend URL no Render.com
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Evento executado quando a aplicação inicia
@app.on_event("startup")
async def startup_event():
    # Cria as tabelas se não existirem
    create_tables()

# Registro das rotas da aplicação
# Cada módulo (auth e converters) tem suas próprias rotas
app.include_router(
    auth.router,                  # Rotas de autenticação
    prefix="/api/auth",           # Prefixo para todas as rotas de auth
    tags=["auth"]                 # Tag para agrupar na documentação
)
app.include_router(
    converters.router,            # Rotas dos conversores
    prefix="/api/converters",     # Prefixo para todas as rotas de conversores
    tags=["converters"]           # Tag para agrupar na documentação
)

# Rota básica para verificar se a API está funcionando
@app.get("/")
async def root():
    return {"message": "Bem-vindo à API do Curso Dev!"}