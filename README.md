# Portal de Conversores - Projeto Didático

Este é um projeto didático para ensino de desenvolvimento web, consistindo em um portal de conversores com autenticação.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Docker
- Docker Compose
- Git

### Passos para Execução

1. Clone o repositório:
```bash
git clone [url-do-repositorio]
cd dev_class
```

2. Inicie os containers:
```bash
docker-compose up --build
```

3. Acesse:
- Frontend: http://localhost
- Backend API: http://localhost:8000
- Documentação API: http://localhost:8000/docs

## 📁 Estrutura do Projeto

```
dev_class/
├── frontend/           # Interface do usuário
├── backend/            # API e lógica de negócio
└── docker-compose.yml  # Configuração dos containers
```

## 📚 Documentação

- [Frontend](./frontend/README.md)
- [Backend](./backend/README.md)

## 🛠️ Tecnologias Utilizadas

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)
- Nginx

### Backend
- Python 3.9
- FastAPI
- MongoDB
- JWT para autenticação

## 🔄 Fluxo de Trabalho

1. Frontend faz requisições para API
2. Backend processa e valida dados
3. MongoDB armazena informações
4. Respostas são tratadas e exibidas

## 👥 Funcionalidades para Usuários

1. **Público**
   - Registro de conta
   - Login
   - Visualização da página inicial

2. **Autenticado**
   - Acesso aos conversores
   - Histórico de conversões
   - Perfil do usuário

## 💡 Conceitos Abordados

- Desenvolvimento Web Full Stack
- APIs RESTful
- Autenticação e Segurança
- Banco de Dados NoSQL
- Docker e Containers
- Frontend Responsivo

## 🐛 Debug e Desenvolvimento

### Logs
```bash
# Ver logs de todos os serviços
docker-compose logs

# Ver logs específicos
docker-compose logs frontend
docker-compose logs backend
docker-compose logs mongodb
```

### Reiniciar Serviços
```bash
# Reiniciar tudo
docker-compose restart

# Reiniciar serviço específico
docker-compose restart frontend
docker-compose restart backend
```

## 📝 Notas de Desenvolvimento

- Código em inglês (padrão da indústria)
- Comentários em português para aprendizado
- Foco em boas práticas
- Estrutura escalável