# Imagem base
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requisitos
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Torna o script de início executável
RUN chmod +x start.sh

# Expõe a porta da aplicação
EXPOSE 8000

# Inicia a aplicação
CMD ["./start.sh"]