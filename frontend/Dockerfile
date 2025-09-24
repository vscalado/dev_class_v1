# Dockerfile para o Frontend
FROM nginx:alpine

# Remove a configuração padrão do nginx
RUN rm -f /etc/nginx/conf.d/default.conf

# Copia nossa configuração personalizada
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copia os arquivos do frontend para o diretório de conteúdo do nginx
COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]