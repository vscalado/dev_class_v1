# Frontend - Portal de Conversores

Este é o frontend do projeto de conversores, desenvolvido com HTML, CSS e JavaScript puro para fins didáticos.

## 📁 Estrutura do Projeto

```
frontend/
├── css/
│   └── style.css          # Estilos da aplicação
├── js/
│   ├── app.js            # Lógica principal e navegação
│   ├── auth.js           # Funções de autenticação
│   └── converters.js     # Lógica dos conversores
├── index.html            # Página principal
├── Dockerfile            # Configuração do container
└── nginx.conf           # Configuração do servidor web
```

## 🚀 Como Rodar

### Com Docker (Recomendado)
O frontend está configurado para rodar em um container Docker junto com o backend.
Na pasta raiz do projeto (acima do frontend), execute:
```bash
docker-compose up --build
```

### Sem Docker (Desenvolvimento)
Para desenvolvimento local, você pode usar qualquer servidor web simples. Por exemplo:

1. Com Python:
```bash
python -m http.server 8080
```

2. Com Node.js (necessário instalar `http-server`):
```bash
npx http-server
```

## 🔍 Funcionalidades

1. **Sistema de Autenticação**
   - Página de login
   - Página de cadastro
   - Validações de formulário

2. **Dashboard**
   - Menu de conversores
   - Área protegida (requer login)
   - Interface responsiva

3. **Conversores**
   - Comprimento (m, cm, km)
   - Volume (l, ml, m³)
   - Interface intuitiva para conversões

## 💡 Conceitos Abordados

- HTML semântico
- CSS responsivo
- JavaScript modular
- Manipulação do DOM
- Eventos e listeners
- Validação de formulários
- Integração com API
- LocalStorage para autenticação

## 🔄 Fluxo de Desenvolvimento

1. Modificar HTML em `index.html`
2. Estilizar componentes em `css/style.css`
3. Implementar lógica em arquivos JS apropriados
4. Testar no navegador
5. Verificar responsividade

## 🐛 Debug e Desenvolvimento

1. Use o console do navegador (F12) para:
   - Ver erros de JavaScript
   - Testar funcionalidades
   - Verificar requisições

2. Use o inspetor de elementos para:
   - Verificar HTML
   - Debugar CSS
   - Testar responsividade

## 📝 Notas

- O código está em inglês (padrão da indústria)
- Comentários em português para facilitar o aprendizado
- Foco em código limpo e bem estruturado
- Sem frameworks para melhor entendimento dos fundamentos