#!/bin/bash

# Instala as dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Espera o PostgreSQL inicializar
echo "Aguardando PostgreSQL..."
sleep 5

# Executa as migrações
echo "Executando migrações do banco de dados..."
alembic upgrade head

# Inicia a aplicação
echo "Iniciando a aplicação..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --reload