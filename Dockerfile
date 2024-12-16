# Etapa 1: Construção do ambiente
FROM python:3.11-slim AS builder

# Define variáveis importantes
ENV PYTHONDONTWRITEBYTECODE 1  # Evita a criação de arquivos .pyc
ENV PYTHONUNBUFFERED 1        # Faz o Python exibir logs em tempo real

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt /app/

# Instala dependências do Python em um ambiente virtual
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Etapa 2: Imagem final
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o ambiente virtual da etapa anterior
COPY --from=builder /opt/venv /opt/venv

# Adiciona o diretório `venv` ao PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copia o código do projeto para a imagem
COPY . /app/

# Expõe a porta que o Gunicorn vai usar
EXPOSE 8000

# Comando para inicializar a aplicação
CMD ["gunicorn", "tecommerce.wsgi:application", "--bind", "0.0.0.0:8000"]
