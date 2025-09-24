# Backend - API de Conversores

Backend do projeto de conversores, desenvolvido com FastAPI e MongoDB para fins didáticos.

## 📁 Estrutura do Projeto

```
backend/
├── routers/
│   ├── auth.py           # Rotas de autenticação
│   └── converters.py     # Rotas dos conversores
├── main.py              # Arquivo principal
├── database.py          # Configuração do MongoDB
├── requirements.txt     # Dependências
└── Dockerfile          # Configuração do container
```

## 🚀 Como Rodar

### Com Docker (Recomendado)
O backend está configurado para rodar em um container Docker junto com MongoDB:
```bash
docker-compose up --build
```

### Sem Docker (Desenvolvimento)
1. Crie um ambiente virtual:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode o servidor:
```bash
uvicorn main:app --reload
```

## 📚 Documentação da API

Com o servidor rodando, acesse:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔑 Endpoints

### Autenticação
- `POST /api/auth/register` - Registro de usuário
- `POST /api/auth/login` - Login de usuário

### Conversores
- `POST /api/converters/length` - Conversão de comprimento
- `POST /api/converters/volume` - Conversão de volume

## 💾 Banco de Dados

Utilizamos MongoDB para armazenar:
- Dados dos usuários
- Histórico de conversões
- Preferências e configurações

### Modelo de Usuário
```python
{
    "email": str,
    "hashed_password": str,
    "name": str,
    "created_at": str,
    "last_login": str,
    "settings": dict
}
```

## 🔒 Segurança

1. **Autenticação**
   - Senhas hasheadas com bcrypt
   - Tokens JWT para sessão
   - Proteção contra força bruta

2. **API**
   - Validação de dados com Pydantic
   - CORS configurado
   - Rate limiting (em desenvolvimento)

## 🔍 Debug e Desenvolvimento

1. **Logs do FastAPI**
   - Requisições detalhadas
   - Erros com traceback
   - Performance metrics

2. **MongoDB**
   - Interface web em http://localhost:8081
   - Shell do MongoDB para queries
   - Backup automático dos dados

## 📝 Notas

- Código em inglês (padrão da indústria)
- Comentários em português para aprendizado
- Documentação automática com Swagger
- Desenvolvimento modular e extensível

## 🔄 Fluxo de Desenvolvimento

1. Implementar rotas em `routers/`
2. Testar com Swagger UI
3. Integrar com frontend
4. Verificar logs e erros
5. Documentar alterações