from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys
from pathlib import Path

# Adiciona o diretório pai ao PATH para poder importar os modelos
sys.path.append(str(Path(__file__).resolve().parents[1]))

from database.models import Base

# URL do banco de dados
config = context.config

# Configura o logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Modelo de metadados para as migrações
target_metadata = Base.metadata

def get_url():
    """Retorna a URL do banco de dados das variáveis de ambiente"""
    return os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/dev_class")

def run_migrations_offline():
    """Executa migrações em modo 'offline'."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa migrações em modo 'online'."""
    configuration = config.get_section(config.config_ini_section)
    if not configuration:
        configuration = {}
    configuration["sqlalchemy.url"] = get_url()
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()