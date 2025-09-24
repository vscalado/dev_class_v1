# Este arquivo torna o diretório um pacote Python
from .auth import router as auth_router
from .converters import router as converters_router

__all__ = ['auth_router', 'converters_router']